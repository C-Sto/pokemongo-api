#!/usr/bin/python
import argparse
import logging
import time
import sys
import traceback
from math import sqrt

from custom_exceptions import GeneralPogoException
from custom_exceptions import NoBallException

from api import PokeAuthSession
from location import Location

from pokedex import pokedex
from inventory import items


def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # no logging.basicConfig(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def displayProfile(sess):
    '''
    Displays profile information to the log output
    :param sess: session duh
    :return:
    '''
    s = ""
    s += sess.getProfile().player_data.username
    s += " Level:"
    inv = sess.getInventory()
    stats = inv.stats
    s += str(stats.level)
    s += " XP to next: "
    s += str(stats.next_level_xp - stats.experience)
    s += " Pokedex: "
    s += str(stats.unique_pokedex_entries)+"/151"
    s += " Party size: "
    s += str(len(inv.party))
    s += " Strongest: "
    if len(inv.party) > 0:
        s += str(getStrongestPokeInPartyString(inv.party))
    else:
        s += "NA"
    logging.info("(PROFILE)\t-\t"+s)


def getStrongestPokeInParty(party):
    '''
    returns the poke with the highest cp in the party. there is probably a better way of doing this
    :param party:
    :return:
    '''
    strongest = 0
    ret = 0
    for poke in party:
        if poke.cp > strongest:
            strongest = poke.cp
            ret = poke
    return ret


def getStrongestPokeInPartyString(party):
    '''
    just gets a string for nice printing :3
    :param party:
    :return:
    '''
    poke = getStrongestPokeInParty(party)
    return str(pokedex[poke.pokemon_id]) + " " + str(poke.cp) +" CP"


def findNearPokemon(session):
    '''
    gets all 'wild' pokemon, does not include lured or incense pokes :(
    :param session:
    :return: list of wild pokemon objects or whatever
    '''
    cells = session.getMapObjects()
    pokemons = []
    for cell in cells.map_cells:
        pokemons += [p for p in cell.wild_pokemons]
    return pokemons


def pickBestBallToUse(bag, encounter, thresh=0.5):
    '''
    Takes in your ball bag, the encounter and works out which ball to use and returns it. Returns false if you got no
    ballz.
    :param bag: session.checkInventory().bag pls
    :param encounter: encounter object
    :param thresh: probability threshold to use a lower ball. set this lower to use more of the shitty balls
    :return: false if no balls, otherwise the ball to use (enum)
    '''
    enc_cap_prob = encounter.capture_probability.capture_probability
    # default to first ball
    if hasattr(bag, 'items.ULTRA_BALL') and bag[items.ULTRA_BALL] > 0:
        ball = items.ULTRA_BALL
    elif hasattr(bag, 'items.GREAT_BALL') and bag[items.GREAT_BALL] > 0:
        ball = items.GREAT_BALL
    elif bag[items.POKE_BALL] > 0:
        ball = items.POKE_BALL
    else:
        # no balls bro
        return False

    # use highest ball, or lowest ball over thresh
    useball = ball
    # oh god I can't believe I wrote this
    while ball > 0:  # ball is an enum, 1=poke 2=great, 3=ultra (fuck that better not change)
        if bag[ball] < 1:  # ignore if we don't have any of the lower ball
            ball -= 1
        if enc_cap_prob[ball-1] > thresh:  # check if the ball is likely to work
            useball = ball  # yay, we can not use an ultra
        ball -= 1  # on to the next ball

    return useball


# Wrap both for ease
def encounterAndCatch(session, pokemon, thresholdP=0.5, limit=5, delay=1):
    '''
    re-written, I assme it still works, it kinda worked before
    :param session: session
    :param pokemon: the pokemon to catch
    :param thresholdP:
    :param limit:
    :param delay:
    :return:
    '''

    # Start encounter
    encounter = session.encounterPokemon(pokemon)
    bag = session.checkInventory().bag
    # give the guy a berry if first probability is kinda low (indicates tricky)
    try:
        if encounter.capture_probability.capture_probability[0] < 0.35:
            logging.info("(ENCOUNTER)\t-\tUsing a %s", items[items.RAZZ_BERRY])
            session.useItemCapture(items.RAZZ_BERRY, pokemon)
    except Exception as e:
        print e
    bestBall = pickBestBallToUse(bag, encounter, thresholdP)

    # no balls yo
    if not bestBall:
        raise NoBallException("(ENCOUNTER)\t-\tOut of usable balls")

    # Only use 5 balls because reasons
    count = 0

    # Attempt catch
    while True:
        # Try to catch it!!
        logging.info("(ENCOUNTER)\t-\tUsing a %s" % items[bestBall])
        attempt = session.catchPokemon(pokemon, bestBall)

        # Success or run away
        if attempt.status == 1:
            return attempt

        # CATCH_FLEE is bad news
        if attempt.status == 3:
            if count == 0:
                logging.info("(ENCOUNTER)\t-\tPossible soft ban.")
            else:
                logging.info("Pokemon fleed at %dth attempt" % (count + 1))
            return attempt

        # Only try up to x attempts
        count += 1
        if count >= limit:
            logging.info("(ENCOUNTER)\t-\tOver catch limit")
            return None
        time.sleep(delay)

        # update bag
        bag = session.checkInventory().bag

        # update ball
        bestBall = pickBestBallToUse(bag, encounter, thresholdP)


# Catch a pokemon at a given point
def walkAndCatch(session, pokemon, speed):
    if pokemon:
        logging.info("(ENCOUNTER)\t-\tCatching %s:" % pokedex[pokemon.pokemon_data.pokemon_id])
        session.walkTo(pokemon.latitude, pokemon.longitude, speed)
        r = encounterAndCatch(session, pokemon)
        if r.status == 1:
            pokes = session.checkInventory().party
            caughtpoke = {}
            for poke in pokes:
                if r.captured_pokemon_id == poke.id:
                    caughtpoke = poke
                    break
            logging.info("(ENCOUNTER)\t-\tCaught " + pokedex[caughtpoke.pokemon_id]+" with "+str(caughtpoke.cp)+" CP")
            return True
        else:
            logging.info("(ENCOUNTER)\t-\tGot away")
            return False


# Basic solution to spinning all forts.
# Since traveling salesman problem, not
# true solution. But at least you get
# those step in
def sortCloseForts(session):
    # Sort nearest forts (pokestop)
    cells = session.getMapObjects()
    latitude, longitude, _ = session.getCoordinates()
    ordered_forts = []
    for cell in cells.map_cells:
        for fort in cell.forts:
            dist = Location.getDistance(
                latitude,
                longitude,
                fort.latitude,
                fort.longitude
            )
            if fort.type == 1:
                ordered_forts.append({'distance': dist, 'fort': fort})

    ordered_forts = sorted(ordered_forts, key=lambda k: k['distance'])
    return [instance['fort'] for instance in ordered_forts]


# Find the fort closest to user that hasn't been used
def findClosestFort(session):
    # Find nearest fort (pokestop)
    for fort in sortCloseForts(session):
        if(fort.cooldown_complete_timestamp_ms > int(time.time()*1000)):
            continue
        return fort
    return False


# Walk to fort and spin
def walkAndSpin(session, fort, speed):
    # No fort, demo == over
    if fort:
        details = session.getFortDetails(fort)
        logging.info("(POKESTOP)\t-\tSpinning the Fort \"%s\":" % details.name)

        # Walk over
        session.walkTo(fort.latitude, fort.longitude, speed)
        # Give it a spin
        fortResponse = session.getFortSearch(fort)
        logging.info("(POKESTOP)\t-\tXP: %d" % fortResponse.experience_awarded)
        if fortResponse.experience_awarded > 0:
            return fortResponse
    logging.info("(POKESTOP)\t-\tAlmost certainly softban :(")
    return False

def spinQuiet(session, fort):
    # No fort, demo == over
    if fort:
        fortResponse = session.getFortSearch(fort)
        if fortResponse.experience_awarded > 0:
            return True
    return False


# A very brute force approach to evolving
def evolveAllPokemon(session):
    inventory = session.checkInventory()
    logging.info("Evolving some of your pokes... hope you don't mind")
    for pokemon in inventory.party:
        if pokedex.evolves[pokemon.pokemon_id] == 0:  # ignore pokes that don't evolve
            continue
        # check to see if we has enough candy to evolve it
        candy = inventory.candies
        if candy[pokedex.family[pokemon.pokemon_id]] >= pokedex.evolves[pokemon.pokemon_id]:
            poke_status = session.evolvePokemon(pokemon)
            logging.debug("EVOLVED : {}".format(poke_status))
            time.sleep(0.5)


def smartEvolveAllPokemon(session, comparison="cp", remaining=1):
    """
    Evolves all pokes that it can, evolves best of type decided by comparison. Will leave remaining pokemon
    :param session: duh
    :param comparison: either cp or iv
    :param remaining: number of pokemon to leave un-evolved.
                      this should be lower than the numtokeep value in the clean method
    :return: nothing
    """
    assert(comparison == "cp" or comparison == "iv")
    inventory = session.checkInventory()
    logging.info("(EVOLVE)\t-\tGonna try evolve sum doodz")

    for x in range(151):
        pokez = getPokesByID(inventory.party, x)
        if len(pokez) <= remaining:
            continue

        pokemon = pokez[0]
        candy = inventory.candies[pokedex.family[pokemon.pokemon_id]]
        candyreq = pokedex.evolves[pokemon.pokemon_id]
        if candy < candyreq or candyreq == 0:
            continue
        ordered = sorted(pokez, key=lambda k: k.cp, reverse=False) if (comparison=="cp")\
                    else sorted(pokez, key=lambda k: checkPerfPercent(k), reverse=False)
        # evolve, starting at the best
        x = 0
        while candy >= candyreq and x < len(pokez)-remaining:
            candy = candy-candyreq
            poke_status = session.evolvePokemon(pokemon)
            logging.info("(EVOLVE)\t-\t"+pokedex[pokemon.pokemon_id]+"->"+pokedex[poke_status.evolved_pokemon_data.pokemon_id])
            time.sleep(0.5)
            x += 1




def checkPerfPercent(poke):
    # thx to pokemon rocket api for perfectpercent calc

    # stam, atk, def
    stam,atk,defense = pokedex.baseStats[poke.pokemon_id]
    max_cp = (atk+15) * sqrt(defense+15) * sqrt(stam+15)
    min_cp = atk * sqrt(defense) * sqrt(stam)
    cur = (atk+poke.individual_attack)*sqrt(defense+poke.individual_defense)*sqrt(stam+poke.individual_stamina)

    return ((cur-min_cp) / (max_cp-min_cp))*100


def cleanPokemonSpecies(session, species, numToKeep = 1, comparison="both", cp_thresh = 2000, iv_thresh=95):
    """
    Clean pokemon of given species - removes low cp/ev pokemon.

    :param session: session, duh
    :param species: an enum (pokedex.<POKEMON>), corresponds 0-151 of pokedex number
    :param numToKeep: number of comparison type pokes to keep (both will keep top x of each)
    :param comparison: comparison type, cp, iv, or both
    :param cp_thresh: cutoff for keeping regardless of iv (set to 10,000 to ignore)
    :param iv_thresh: cutoff for keeping regardless of cp (set to 101 to ignore)
    :return: iv_thresh: cutoff for keeping
    """
    # check input is valid
    assert(comparison == "cp" or comparison == "iv" or comparison == "both")
    party = session.checkInventory().party
    # get all pokes of id
    pokz = getPokesByID(party, species)
    keepers = set()
    if len(pokz) < numToKeep:
        return

    if comparison == "cp" or comparison == "both":
        # order by iv
        ordered_pokz = sorted(pokz, key=lambda k: k.cp, reverse=True)

        # remove all but best x CP

        # find best x cp
        for x in range(numToKeep):
            keepers.add(ordered_pokz[x].id)

        # keep above cp_thresh
        for x in ordered_pokz:
            if x.cp > cp_thresh:
                keepers.add(x.id)
            else:
                break

    if comparison == "iv" or comparison == "both":
        # order by iv
        ordered_pokz= sorted(pokz, key=lambda k: checkPerfPercent(k), reverse=True)

        # remove all but best x IV

        # find best x IV
        for x in range(numToKeep):
            keepers.add(ordered_pokz[x].id)

        # keep above iv_thresh
        for x in ordered_pokz:
            if checkPerfPercent(x) > iv_thresh:
                keepers.add(x.id)
            else:
                break

    # remove everything except for keepers
    for poke in pokz:
        if poke.id in keepers:
            continue
        logging.info("(POKEMANAGE)\t-\tReleasing: "+pokedex[poke.pokemon_id]+" "+str(poke.cp)+" CP "+str(checkPerfPercent(poke))+"% IV")
        session.releasePokemon(poke)


# Set an egg to an incubator
def setEgg(session):
    inventory = session.checkInventory()

    # If no eggs, nothing we can do
    if len(inventory.eggs) == 0:
        return None

    egg = inventory.eggs[0]
    incubator = inventory.incubators[0]
    return session.setEgg(incubator, egg)


def cleanInventory(session):
    recycled = 0
    bag = session.checkInventory().bag

    # Clear out all of a crtain type
    tossable = [items.POTION, items.SUPER_POTION, items.REVIVE]
    for toss in tossable:
        if toss in bag and bag[toss]:
            session.recycleItem(toss, bag[toss])
            recycled+=1

    # Limit a certain type
    limited = {
        items.POKE_BALL: 30,
        items.GREAT_BALL: 40,
        items.ULTRA_BALL: 100,
        items.RAZZ_BERRY: 30,
        items.HYPER_POTION: 30,
        items.MAX_POTION: 30,
        items.MAX_REVIVE: 10,
        items.MASTER_BALL: 300
    }
    for limit in limited:
        try:
            if limit in bag and bag[limit] > limited[limit]:
                session.recycleItem(limit, bag[limit] - limited[limit])
                recycled+=1
        except:
            print "fuckin"
            pass
    logging.info("(ITEM MANAGE)\t-\tCleaned out Inventory, "+str(recycled)+" items recycled.")


def getPokesByID(party, id):
    ret = []
    for poke in party:
        if poke.pokemon_id == id:
            ret.append(poke)
    return ret


def cleanAllPokes(session):
    logging.info("(POKEMANAGE)\t-\tCleaning out Pokes...")
    for poke in range(0,151):
        cleanPokemonSpecies(session, poke, numToKeep=1, comparison="both")


def catch_demPokez(pokez, sess, whatup_cunt):
    if walkAndCatch(sess, pokez, whatup_cunt):
        return True
    else:
        return False


def enough_time_left(pokzzzzzzzzz):
    return min(sorted(pokzzzzzzzzz, key=lambda p: p.time_till_hidden_ms)) > 1000


def location_jumper(locs, session):
    for loc in locs:

        pass


def check_softban(session, fort, speed):
    #  should probably invert this :/
    return walkAndSpin(session, fort, speed)


def spinnyspinnyspinny(session, fort):
    for i in range(51):
        spinQuiet(session, fort)


def safe_catch(pokies, session, speed):  # NOT CAMEL CASE COZ PEP8 U FUCKERS
    """
    Performs a safe catch of good pokemanz by catching the shithouse ones first and only approaching the mad dogs once
    it's safe to do so (i.e. after you've catch_successed a shithouse one)
    """
    epicpokes = []
    shitpokes = []
    for pokemon in pokies:
        if pokedex.getRarityById(pokemon.pokemon_data.pokemon_id) >= 4:  # if rare pokemanzzzz
            epicpokes.append(pokemon)
        else:
            shitpokes.append(pokemon)
    if epicpokes:
        logging.info("(SWARL)\t-\tSOME EPIC POKES EYYYYY:{}"
                     .format(", ".join([repr(cunt.pokemon_data).strip("\n") for cunt in epicpokes])))
    if shitpokes:
        logging.info("(SWARL)\t-\tTHESE POKES ARE SOMEWHAT UNDESIRABLE:{}"
                     .format(", ".join([repr(cunt.pokemon_data).strip("\n") for cunt in shitpokes])))
    if epicpokes:
        while True:
            try:
                asshole = shitpokes.pop()
                if catch_demPokez(asshole, session, speed):
                    break
                else:
                    if not check_softban(session, findClosestFort(session), speed):
                        spinnyspinnyspinny(session, findClosestFort(session))
                    continue
            except IndexError:
                logging.info("(SWARL)\t-\tRan out of bad pokez")
                if enough_time_left(pokies):
                    return False
                else:
                    logging.info("(SWARL)\t-\twell heregoesnothing - no time to waste...")
                    break
        for spaz in epicpokes:
            catch_demPokez(spaz, session, speed)
    for pokemon in shitpokes:
        catch_demPokez(pokemon, session, speed)
    return True


def do_a_pokeman(session, bag, speed):
    if bag[items.POKE_BALL] > 0 or (hasattr(bag, 'items.GREAT_BALL') and bag[items.GREAT_BALL] > 0) or (hasattr(bag, 'items.ULTRA_BALL') and bag[items.ULTRA_BALL] > 0):
        coutn = 1
        while True:
            coutn += 1  # lol at this being added now
            if safe_catch(findNearPokemon(session), session, speed):
                break
            elif coutn > 13:
                break


def grab_some_fkn_pokeballz(session, speed):
    fort = findClosestFort(session)
    if fort:
        if not walkAndSpin(session, fort, speed):
            if not check_softban(session, fort, speed):
                spinnyspinnyspinny(session, fort)
    else:
        logging.info("(TRAVEL)\t-\tNo Forts found? wut")


# cambot :D
def camBot(session, speed):

    startlat, startlon, startalt = session.getCoordinates()
    cooldown = 10
    speed *= 0.277778  # convert to m/s

    while True:
        try:
            lat, lon, alt = session.getCoordinates()
            displayProfile(session)
            dist = Location.getDistance(startlat, startlon,lat, lon)
            logging.info("(TRAVEL)\t-\tDistance from start: "+str(dist))
            if dist > 5000:
                print "(TRAVEL)\t-\tWalking back to start to stay in area"
                session.walkTo(startlat, startlon, speed)
            # check for pokeballs (don't try to catch if we have none)
            bag = session.getInventory().bag
            grab_some_fkn_pokeballz(session, speed)
            smartEvolveAllPokemon(session)
            do_a_pokeman(session, bag, speed)
            cleanAllPokes(session)
            cleanInventory(session)
            setEgg(session)

        # check distance from start
        # Catch problems and reauthenticate
        except GeneralPogoException as e:
            logging.critical('GeneralPogoException raised: %s', e)
            session = poko_session.reauthenticate(session)
            time.sleep(cooldown)

        except NoBallException as e:
            grab_some_fkn_pokeballz(session, speed)

        except Exception as e:
            logging.critical('Exception raised: %s', e)
            traceback.print_exc()
            session = poko_session.reauthenticate(session)
            time.sleep(cooldown)

# Entry point
# Start off authentication and demo
if __name__ == '__main__':
    setupLogger()
    speed = 150  # km/h
    logging.debug('Logger set up')

    # Read in args
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", help="Auth Service", required=True)
    parser.add_argument("-u", "--username", help="Username", required=True)
    parser.add_argument("-p", "--password", help="Password", required=True)
    parser.add_argument("-l", "--location", help="Location")
    parser.add_argument("-g", "--geo_key", help="GEO API Secret")
    parser.add_argument("-s", "--speed", help="Speed")
    args = parser.parse_args()

    # Check service
    if args.auth not in ['ptc', 'google']:
        logging.error('Invalid auth service {}'.format(args.auth))
        sys.exit(-1)
    if args.speed:
        speed = int(args.speed)
    while True:
        try:
            # Create PokoAuthObject
            poko_session = PokeAuthSession(
                args.username,
                args.password,
                args.auth,
                geo_key=args.geo_key
            )

            # Authenticate with a given location
            # Location is not inherent in authentication
            # But is important to session
            if args.location:
                session = poko_session.authenticate(locationLookup=args.location)
            else:
                session = poko_session.authenticate()

            # Time to show off what we can do
            if session:
                camBot(session, speed)

            else:
                logging.critical('Session not created successfully')
        except Exception as e:
            logging.critical("Something tried to shut us down, logging in again after 20 secs")
            logging.critical(e)
            time.sleep(20)  # pretty sure this is in seconds
