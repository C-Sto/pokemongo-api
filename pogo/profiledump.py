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
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # '%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def checkPerfPercent(poke):
    # thx to pokemon rocket api for perfectpercent calc

    # stam, atk, def
    stam,atk,defense = pokedex.baseStats[poke.pokemon_id]
    max_cp = (atk+15) * sqrt(defense+15) * sqrt(stam+15)
    min_cp = atk * sqrt(defense) * sqrt(stam)
    cur = (atk+poke.individual_attack)*sqrt(defense+poke.individual_defense)*sqrt(stam+poke.individual_stamina)
    return ((cur-min_cp) / (max_cp-min_cp))*100


def getPokesByID(party, id):
    ret = []
    for poke in party:
        if poke.pokemon_id == id:
            ret.append(poke)
    return ret


def printProfile(session):
    prof = session.getProfile().player_data
    stats = session.getInventory().stats
    print "Level: "+str(stats.level)+" XP: "+str(stats.experience)
    print "Profile Details: "
    s = "Pokemon Storage Capacity: "
    s += str(prof.max_pokemon_storage)
    s += "\tItem Storage Capacity: "
    s += str(prof.max_item_storage)
    s += "\tStardust: "
    s += str(prof.currencies[1].amount)
    print s

def printPokes(session):
    print "Pokemon: "
    print "Name\tCP\tIV Perfection\tStamina\tAttack\tDefense\tCandy".expandtabs(15)
    party = session.checkInventory().party
    candy = session.checkInventory().candies
    for i in range(151):
        pokz = getPokesByID(party, i)
        if len(pokz) > 0:
            for pok in pokz:
                s = pokedex[pok.pokemon_id]
                s += "\t" + str(pok.cp) + "\t" + str(int(checkPerfPercent(pok))) + "%"
                s += "\t" + str(pok.individual_stamina) + "\t" +str(pok.individual_attack) + "\t" + str(pok.individual_defense)
                s += "\t" + str(candy[pokedex.family[pok.pokemon_id]])
                print s.expandtabs(15)
    pass

def printInv(session):
    print "Items:"
    bag = session.checkInventory().bag
    for thing in bag:
        print (items[thing]+":\t" + str(bag[thing])).expandtabs(30)
    pass
# Entry point
# Start off authentication and demo
if __name__ == '__main__':
    setupLogger()

    # Read in args
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", help="Auth Service", required=True)
    parser.add_argument("-u", "--username", help="Username", required=True)
    parser.add_argument("-p", "--password", help="Password", required=True)
    args = parser.parse_args()

    # Check service
    if args.auth not in ['ptc', 'google']:
        logging.error('Invalid auth service {}'.format(args.auth))
        sys.exit(-1)

    while True:
        try:
            # Create PokoAuthObject
            poko_session = PokeAuthSession(
                args.username,
                args.password,
                args.auth
            )

            session = poko_session.authenticate()

            # Time to show off what we can do
            if session:
                printProfile(session)
                printPokes(session)
                printInv(session)
                exit()
            else:
                logging.critical('Session not created successfully')
        except Exception as e:
            logging.critical("Something tried to shut us down, logging in again after 20 secs")
            logging.critical(e)
            time.sleep(20)  # pretty sure this is in seconds
