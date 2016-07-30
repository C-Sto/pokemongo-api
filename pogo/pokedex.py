import inspect


class Pokedex(dict):

    # Enum pokemonIds
    MISSINGNO = 0
    BULBASAUR = 1
    IVYSAUR = 2
    VENUSAUR = 3
    CHARMANDER = 4
    CHARMELEON = 5
    CHARIZARD = 6
    SQUIRTLE = 7
    WARTORTLE = 8
    BLASTOISE = 9
    CATERPIE = 10
    METAPOD = 11
    BUTTERFREE = 12
    WEEDLE = 13
    KAKUNA = 14
    BEEDRILL = 15
    PIDGEY = 16
    PIDGEOTTO = 17
    PIDGEOT = 18
    RATTATA = 19
    RATICATE = 20
    SPEAROW = 21
    FEAROW = 22
    EKANS = 23
    ARBOK = 24
    PIKACHU = 25
    RAICHU = 26
    SANDSHREW = 27
    SANDSLASH = 28
    NIDORAN_FEMALE = 29
    NIDORINA = 30
    NIDOQUEEN = 31
    NIDORAN_MALE = 32
    NIDORINO = 33
    NIDOKING = 34
    CLEFAIRY = 35
    CLEFABLE = 36
    VULPIX = 37
    NINETALES = 38
    JIGGLYPUFF = 39
    WIGGLYTUFF = 40
    ZUBAT = 41
    GOLBAT = 42
    ODDISH = 43
    GLOOM = 44
    VILEPLUME = 45
    PARAS = 46
    PARASECT = 47
    VENONAT = 48
    VENOMOTH = 49
    DIGLETT = 50
    DUGTRIO = 51
    MEOWTH = 52
    PERSIAN = 53
    PSYDUCK = 54
    GOLDUCK = 55
    MANKEY = 56
    PRIMEAPE = 57
    GROWLITHE = 58
    ARCANINE = 59
    POLIWAG = 60
    POLIWHIRL = 61
    POLIWRATH = 62
    ABRA = 63
    KADABRA = 64
    ALAKAZAM = 65
    MACHOP = 66
    MACHOKE = 67
    MACHAMP = 68
    BELLSPROUT = 69
    WEEPINBELL = 70
    VICTREEBEL = 71
    TENTACOOL = 72
    TENTACRUEL = 73
    GEODUDE = 74
    GRAVELER = 75
    GOLEM = 76
    PONYTA = 77
    RAPIDASH = 78
    SLOWPOKE = 79
    SLOWBRO = 80
    MAGNEMITE = 81
    MAGNETON = 82
    FARFETCHD = 83
    DODUO = 84
    DODRIO = 85
    SEEL = 86
    DEWGONG = 87
    GRIMER = 88
    MUK = 89
    SHELLDER = 90
    CLOYSTER = 91
    GASTLY = 92
    HAUNTER = 93
    GENGAR = 94
    ONIX = 95
    DROWZEE = 96
    HYPNO = 97
    KRABBY = 98
    KINGLER = 99
    VOLTORB = 100
    ELECTRODE = 101
    EXEGGCUTE = 102
    EXEGGUTOR = 103
    CUBONE = 104
    MAROWAK = 105
    HITMONLEE = 106
    HITMONCHAN = 107
    LICKITUNG = 108
    KOFFING = 109
    WEEZING = 110
    RHYHORN = 111
    RHYDON = 112
    CHANSEY = 113
    TANGELA = 114
    KANGASKHAN = 115
    HORSEA = 116
    SEADRA = 117
    GOLDEEN = 118
    SEAKING = 119
    STARYU = 120
    STARMIE = 121
    MR_MIME = 122
    SCYTHER = 123
    JYNX = 124
    ELECTABUZZ = 125
    MAGMAR = 126
    PINSIR = 127
    TAUROS = 128
    MAGIKARP = 129
    GYARADOS = 130
    LAPRAS = 131
    DITTO = 132
    EEVEE = 133
    VAPOREON = 134
    JOLTEON = 135
    FLAREON = 136
    PORYGON = 137
    OMANYTE = 138
    OMASTAR = 139
    KABUTO = 140
    KABUTOPS = 141
    AERODACTYL = 142
    SNORLAX = 143
    ARTICUNO = 144
    ZAPDOS = 145
    MOLTRES = 146
    DRATINI = 147
    DRAGONAIR = 148
    DRAGONITE = 149
    MEWTWO = 150
    MEW = 151

    rarity = {}
    evolves = {}

    def __init__(self):
        super(dict, self).__init__(self)

        # Some reflection, based on upperconsts.
        attributes = inspect.getmembers(Pokedex, lambda attr :not(inspect.isroutine(attr)))
        for attr in attributes:
            if attr[0].isupper():
                self[attr[1]] = attr[0]

        # Ideally go back and lint for line lengths
        self.rarity[Rarity.MYTHIC] = [self.MEW]
        self.rarity[Rarity.LEGENDARY] = [
            self.ZAPDOS, self.MOLTRES, self.MEWTWO, self.ARTICUNO
        ]
        self.rarity[Rarity.EPIC] = [
            self.DITTO, self.VENUSAUR, self.TAUROS, self.DRAGONITE, self.CLEFABLE,
            self.CHARIZARD, self.BLASTOISE
        ]
        self.rarity[Rarity.VERY_RARE] = [
            self.WEEPINBELL, self.WARTORTLE, self.VILEPLUME, self.VICTREEBEL,
            self.VENOMOTH, self.VAPOREON, self.SLOWBRO, self.RAICHU, self.POLIWRATH,
            self.PINSIR, self.PIDGEOT, self.OMASTAR, self.NIDOQUEEN, self.NIDOKING,
            self.MUK, self.MAROWAK, self.LAPRAS, self.KANGASKHAN, self.KABUTOPS, self.IVYSAUR,
            self.GYARADOS, self.GOLEM, self.GENGAR, self.EXEGGUTOR, self.DRAGONAIR, self.DEWGONG,
            self.CHARMELEON, self.BEEDRILL, self.ALAKAZAM
        ]
        self.rarity[Rarity.RARE] = [
            self.WIGGLYTUFF, self.WEEZING, self.TENTACRUEL, self.TANGELA,
            self.STARMIE, self.SNORLAX, self.SCYTHER, self.SEAKING, self.SEADRA,
            self.RHYDON, self.RAPIDASH, self.PRIMEAPE, self.PORYGON, self.POLIWHIRL,
            self.PARASECT, self.ONIX, self.OMANYTE, self.NINETALES, self.NIDORINO,
            self.NIDORINA, self.MR_MIME, self.MAGMAR, self.MACHOKE, self.MACHAMP,
            self.LICKITUNG, self.KINGLER, self.JOLTEON, self.HYPNO, self.HITMONCHAN,
            self.GLOOM, self.GOLDUCK, self.FLAREON, self.FEAROW, self.FARFETCHD,
            self.ELECTABUZZ, self.DUGTRIO, self.DRATINI, self.DODRIO, self.CLOYSTER,
            self.CHANSEY, self.BUTTERFREE, self.ARCANINE, self.AERODACTYL
        ]
        self.rarity[Rarity.UNCOMMON] = [
            self.VULPIX, self.TENTACOOL, self.STARYU, self.SQUIRTLE, self.SPEAROW,
            self.SHELLDER, self.SEEL, self.SANDSLASH, self.RHYHORN, self.RATICATE,
            self.PSYDUCK, self.PONYTA, self.PIKACHU, self.PIDGEOTTO, self.PERSIAN,
            self.METAPOD, self.MAGNETON, self.KOFFING, self.KADABRA, self.KABUTO,
            self.KAKUNA, self.JYNX, self.JIGGLYPUFF, self.HORSEA, self.HITMONLEE,
            self.HAUNTER, self.GROWLITHE, self.GRIMER, self.GRAVELER, self.GOLBAT,
            self.EXEGGCUTE, self.ELECTRODE, self.CUBONE, self.CLEFAIRY, self.CHARMANDER,
            self.BULBASAUR, self.ARBOK, self.ABRA
        ]
        self.rarity[Rarity.COMMON] = [
            self.WEEDLE, self.VOLTORB, self.VENONAT, self.SLOWPOKE, self.SANDSHREW,
            self.POLIWAG, self.PARAS, self.ODDISH, self.NIDORAN_MALE, self.NIDORAN_FEMALE,
            self.MEOWTH, self.MANKEY, self.MAGNEMITE, self.MAGIKARP, self.MACHOP, self.KRABBY,
            self.GOLDEEN, self.GEODUDE, self.GASTLY, self.EEVEE, self.EKANS, self.DROWZEE,
            self.DODUO, self.DIGLETT, self.CATERPIE, self.BELLSPROUT
        ]
        self.rarity[Rarity.CRITTER] = [self.ZUBAT, self.PIDGEY, self.RATTATA]

        self.evolves = {
            self.MISSINGNO: 0, self.BULBASAUR: 25, self.IVYSAUR: 100, self.VENUSAUR: 0,
            self.CHARMANDER: 25, self.CHARMELEON: 100, self.CHARIZARD: 0, self.SQUIRTLE: 25,
            self.WARTORTLE: 100, self.BLASTOISE: 0, self.CATERPIE: 12, self.METAPOD: 50,
            self.BUTTERFREE: 0, self.WEEDLE: 12, self.KAKUNA: 50, self.BEEDRILL: 0, self.PIDGEY: 12,
            self.PIDGEOTTO: 50, self.PIDGEOT: 0, self.RATTATA: 25, self.RATICATE: 0, self.SPEAROW: 50,
            self.FEAROW: 0, self.EKANS: 50, self.ARBOK: 0, self.PIKACHU: 50, self.RAICHU: 0,
            self.SANDSHREW: 50, self.SANDSLASH: 0, self.NIDORAN_FEMALE: 25, self.NIDORINA: 100,
            self.NIDOQUEEN: 0, self.NIDORAN_MALE: 25, self.NIDORINO: 100, self.NIDOKING: 0,
            self.CLEFAIRY: 50, self.CLEFABLE: 0, self.VULPIX: 50, self.NINETALES: 0, self.JIGGLYPUFF: 50,
            self.WIGGLYTUFF: 0, self.ZUBAT: 50, self.GOLBAT: 0, self.ODDISH: 25, self.GLOOM: 100,
            self.VILEPLUME: 0, self.PARAS: 50, self.PARASECT: 0, self.VENONAT: 50, self.VENOMOTH: 0,
            self.DIGLETT: 50, self.DUGTRIO: 0, self.MEOWTH: 50, self.PERSIAN: 0, self.PSYDUCK: 50,
            self.GOLDUCK: 0, self.MANKEY: 50, self.PRIMEAPE: 0, self.GROWLITHE: 50, self.ARCANINE: 0,
            self.POLIWAG: 25, self.POLIWHIRL: 100, self.POLIWRATH: 0, self.ABRA: 25, self.KADABRA: 100,
            self.ALAKAZAM: 0, self.MACHOP: 25, self.MACHOKE: 100, self.MACHAMP: 0, self.BELLSPROUT: 25,
            self.WEEPINBELL: 100, self.VICTREEBEL: 0, self.TENTACOOL: 50, self.TENTACRUEL: 0,
            self.GEODUDE: 25, self.GRAVELER: 100, self.GOLEM: 0, self.PONYTA: 50, self.RAPIDASH: 0,
            self.SLOWPOKE: 50, self.SLOWBRO: 0, self.MAGNEMITE: 50, self.MAGNETON: 0, self.FARFETCHD: 0,
            self.DODUO: 50, self.DODRIO: 0, self.SEEL: 50, self.DEWGONG: 0, self.GRIMER: 50, self.MUK: 0,
            self.SHELLDER: 50, self.CLOYSTER: 0, self.GASTLY: 25, self.HAUNTER: 100, self.GENGAR: 0,
            self.ONIX: 0, self.DROWZEE: 50, self.HYPNO: 0, self.KRABBY: 50, self.KINGLER: 0, self.VOLTORB: 50,
            self.ELECTRODE: 0, self.EXEGGCUTE: 50, self.EXEGGUTOR: 0, self.CUBONE: 50, self.MAROWAK: 0,
            self.HITMONLEE: 0, self.HITMONCHAN: 0, self.LICKITUNG: 0, self.KOFFING: 50, self.WEEZING: 0,
            self.RHYHORN: 50, self.RHYDON: 0, self.CHANSEY: 0, self.TANGELA: 0, self.KANGASKHAN: 0,
            self.HORSEA: 50, self.SEADRA: 0, self.GOLDEEN: 50, self.SEAKING: 0, self.STARYU: 50, self.STARMIE: 0,
            self.MR_MIME: 0, self.SCYTHER: 0, self.JYNX: 0, self.ELECTABUZZ: 0, self.MAGMAR: 0, self.PINSIR: 0,
            self.TAUROS: 0, self.MAGIKARP: 400, self.GYARADOS: 0, self.LAPRAS: 0, self.DITTO: 0, self.EEVEE: 25,
            self.VAPOREON: 0, self.JOLTEON: 0, self.FLAREON: 0, self.PORYGON: 0, self.OMANYTE: 50, self.OMASTAR: 0,
            self.KABUTO: 50, self.KABUTOPS: 0, self.AERODACTYL: 0, self.SNORLAX: 0, self.ARTICUNO: 0,
            self.ZAPDOS: 0, self.MOLTRES: 0, self.DRATINI: 25, self.DRAGONAIR: 100, self.DRAGONITE: 0,
            self.MEWTWO: 0, self.MEW: 0
        }

        self.family = {
            self.MISSINGNO: self.MISSINGNO, self.BULBASAUR: self.BULBASAUR, self.IVYSAUR: self.BULBASAUR, self.VENUSAUR: self.BULBASAUR,
            self.CHARMANDER: self.CHARMANDER, self.CHARMELEON: self.CHARMANDER, self.CHARIZARD: self.CHARMANDER, self.SQUIRTLE: self.SQUIRTLE,
            self.WARTORTLE: self.SQUIRTLE, self.BLASTOISE: self.SQUIRTLE, self.CATERPIE: self.CATERPIE, self.METAPOD: self.CATERPIE,
            self.BUTTERFREE: self.CATERPIE, self.WEEDLE: self.WEEDLE, self.KAKUNA: self.WEEDLE, self.BEEDRILL: self.WEEDLE, self.PIDGEY: self.PIDGEY,
            self.PIDGEOTTO: self.PIDGEY, self.PIDGEOT: self.PIDGEY, self.RATTATA: self.RATTATA, self.RATICATE: self.RATTATA, self.SPEAROW: self.SPEAROW,
            self.FEAROW: self.SPEAROW, self.EKANS: self.EKANS, self.ARBOK: self.EKANS, self.PIKACHU: self.PIKACHU, self.RAICHU: self.PIKACHU,
            self.SANDSHREW: self.SANDSHREW, self.SANDSLASH: self.SANDSHREW, self.NIDORAN_FEMALE: self.NIDORAN_FEMALE, self.NIDORINA: self.NIDORAN_FEMALE,
            self.NIDOQUEEN: self.NIDORAN_FEMALE, self.NIDORAN_MALE: self.NIDORAN_MALE, self.NIDORINO: self.NIDORAN_MALE, self.NIDOKING: self.NIDORAN_MALE,
            self.CLEFAIRY: self.CLEFAIRY, self.CLEFABLE: self.CLEFAIRY, self.VULPIX: self.VULPIX, self.NINETALES: self.VULPIX, self.JIGGLYPUFF: self.JIGGLYPUFF,
            self.WIGGLYTUFF: self.JIGGLYPUFF, self.ZUBAT: self.ZUBAT, self.GOLBAT: self.ZUBAT, self.ODDISH: self.ODDISH, self.GLOOM: self.ODDISH,
            self.VILEPLUME: self.ODDISH, self.PARAS: self.PARAS, self.PARASECT: self.PARAS, self.VENONAT: self.VENONAT, self.VENOMOTH: self.VENONAT,
            self.DIGLETT: self.DIGLETT, self.DUGTRIO: self.DIGLETT, self.MEOWTH: self.MEOWTH, self.PERSIAN: self.MEOWTH, self.PSYDUCK: self.PSYDUCK,
            self.GOLDUCK: self.PSYDUCK, self.MANKEY: self.MANKEY, self.PRIMEAPE: self.MANKEY, self.GROWLITHE: self.GROWLITHE, self.ARCANINE: self.GROWLITHE,
            self.POLIWAG: self.POLIWAG, self.POLIWHIRL: self.POLIWAG, self.POLIWRATH: self.POLIWAG, self.ABRA: self.ABRA, self.KADABRA: self.ABRA,
            self.ALAKAZAM: self.ABRA, self.MACHOP: self.MACHOP, self.MACHOKE: self.MACHOP, self.MACHAMP: self.MACHOP, self.BELLSPROUT: self.BELLSPROUT,
            self.WEEPINBELL: self.BELLSPROUT, self.VICTREEBEL: self.BELLSPROUT, self.TENTACOOL: self.TENTACOOL, self.TENTACRUEL: self.TENTACOOL,
            self.GEODUDE: self.GEODUDE, self.GRAVELER: self.GEODUDE, self.GOLEM: self.GEODUDE, self.PONYTA: self.PONYTA, self.RAPIDASH: self.PONYTA,
            self.SLOWPOKE: self.SLOWPOKE, self.SLOWBRO: self.SLOWPOKE, self.MAGNEMITE: self.MAGNEMITE, self.MAGNETON: self.MAGNEMITE, self.FARFETCHD: self.FARFETCHD,
            self.DODUO: self.DODUO, self.DODRIO: self.DODUO, self.SEEL: self.SEEL, self.DEWGONG: self.SEEL, self.GRIMER: self.GRIMER, self.MUK: self.GRIMER,
            self.SHELLDER: self.SHELLDER, self.CLOYSTER: self.SHELLDER, self.GASTLY: self.GASTLY, self.HAUNTER: self.GASTLY, self.GENGAR: self.GASTLY,
            self.ONIX: self.ONIX, self.DROWZEE: self.DROWZEE, self.HYPNO: self.DROWZEE, self.KRABBY: self.KRABBY, self.KINGLER: self.KRABBY, self.VOLTORB: self.VOLTORB,
            self.ELECTRODE: self.VOLTORB, self.EXEGGCUTE: self.EXEGGCUTE, self.EXEGGUTOR: self.EXEGGCUTE, self.CUBONE: self.CUBONE, self.MAROWAK: self.CUBONE,
            self.HITMONLEE: self.HITMONLEE, self.HITMONCHAN: self.HITMONCHAN, self.LICKITUNG: self.LICKITUNG, self.KOFFING: self.KOFFING, self.WEEZING: self.KOFFING,
            self.RHYHORN: self.RHYHORN, self.RHYDON: self.RHYHORN, self.CHANSEY: self.CHANSEY, self.TANGELA: self.TANGELA, self.KANGASKHAN: self.KANGASKHAN,
            self.HORSEA: self.HORSEA, self.SEADRA: self.HORSEA, self.GOLDEEN: self.GOLDEEN, self.SEAKING: self.GOLDEEN, self.STARYU: self.STARYU, self.STARMIE: self.STARYU,
            self.MR_MIME: self.MR_MIME, self.SCYTHER: self.SCYTHER, self.JYNX: self.JYNX, self.ELECTABUZZ: self.ELECTABUZZ, self.MAGMAR: self.MAGMAR, self.PINSIR: self.PINSIR,
            self.TAUROS: self.TAUROS, self.MAGIKARP: self.MAGIKARP, self.GYARADOS: self.MAGIKARP, self.LAPRAS: self.LAPRAS, self.DITTO: self.DITTO, self.EEVEE: self.EEVEE,
            self.VAPOREON: self.EEVEE, self.JOLTEON: self.EEVEE, self.FLAREON: self.EEVEE, self.PORYGON: self.PORYGON, self.OMANYTE: self.OMANYTE, self.OMASTAR: self.OMANYTE,
            self.KABUTO: self.KABUTO, self.KABUTOPS: self.KABUTO, self.AERODACTYL: self.AERODACTYL, self.SNORLAX: self.SNORLAX, self.ARTICUNO: self.ARTICUNO,
            self.ZAPDOS: self.ZAPDOS, self.MOLTRES: self.MOLTRES, self.DRATINI: self.DRATINI, self.DRAGONAIR: self.DRATINI, self.DRAGONITE: self.DRATINI,
            self.MEWTWO: self.MEWTWO, self.MEW: self.MEW
        }

        self.baseStats = {
                0: [0,0,0],
                1:  [90, 126, 126],
                2:  [120, 156, 158],
                3:  [160, 198, 200],
                4:  [78, 128, 108],
                5:  [116, 160, 140],
                6:  [156, 212, 182],
                7:  [88, 112, 142],
                8:  [118, 144, 176],
                9:  [158, 186, 222],
                10:  [90, 62, 66],
                11:  [100, 56, 86],
                12:  [120, 144, 144],
                13:  [80, 68, 64],
                14:  [90, 62, 82],
                15:  [130, 144, 130],
                16:  [80, 94, 90],
                17:  [126, 126, 122],
                18:  [166, 170, 166],
                19:  [60, 92, 86],
                20:  [110, 146, 150],
                21:  [80, 102, 78],
                22:  [130, 168, 146],
                23:  [70, 112, 112],
                24:  [120, 166, 166],
                25:  [70, 124, 108],
                26:  [120, 200, 154],
                27:  [100, 90, 114],
                28:  [150, 150, 172],
                29:  [110, 100, 104],
                30:  [140, 132, 136],
                31:  [180, 184, 190],
                32:  [92, 110, 94],
                33:  [122, 142, 128],
                34:  [162, 204, 170],
                35:  [140, 116, 124],
                36:  [190, 178, 178],
                37:  [76, 106, 118],
                38:  [146, 176, 194],
                39:  [230, 98, 54],
                40:  [280, 168, 108],
                41:  [80, 88, 90],
                42:  [150, 164, 164],
                43:  [90, 134, 130],
                44:  [120, 162, 158],
                45:  [150, 202, 190],
                46:  [70, 122, 120],
                47:  [120, 162, 170],
                48:  [120, 108, 118],
                49:  [140, 172, 154],
                50:  [20, 108, 86],
                51:  [70, 148, 140],
                52:  [80, 104, 94],
                53:  [130, 156, 146],
                54:  [100, 132, 112],
                55:  [160, 194, 176],
                56:  [80, 122, 96],
                57:  [130, 178, 150],
                58:  [110, 156, 110],
                59:  [180, 230, 180],
                60:  [80, 108, 98],
                61:  [130, 132, 132],
                62:  [180, 180, 202],
                63:  [50, 110, 76],
                64:  [80, 150, 112],
                65:  [110, 186, 152],
                66:  [140, 118, 96],
                67:  [160, 154, 144],
                68:  [180, 198, 180],
                69:  [100, 158, 78],
                70:  [130, 190, 110],
                71:  [160, 222, 152],
                72:  [80, 106, 136],
                73:  [160, 170, 196],
                74:  [80, 106, 118],
                75:  [110, 142, 156],
                76:  [160, 176, 198],
                77:  [100, 168, 138],
                78:  [130, 200, 170],
                79:  [180, 110, 110],
                80:  [190, 184, 198],
                81:  [50, 128, 138],
                82:  [100, 186, 180],
                83:  [104, 138, 132],
                84:  [70, 126, 96],
                85:  [120, 182, 150],
                86:  [130, 104, 138],
                87:  [180, 156, 192],
                88:  [160, 124, 110],
                89:  [210, 180, 188],
                90:  [60, 120, 112],
                91:  [100, 196, 196],
                92:  [60, 136, 82],
                93:  [90, 172, 118],
                94:  [120, 204, 156],
                95:  [70, 90, 186],
                96:  [120, 104, 140],
                97:  [170, 162, 196],
                98:  [60, 116, 110],
                99:  [110, 178, 168],
                100:  [80, 102, 124],
                101:  [120, 150, 174],
                102:  [120, 110, 132],
                103:  [190, 232, 164],
                104:  [100, 102, 150],
                105:  [120, 140, 202],
                106:  [100, 148, 172],
                107:  [100, 138, 204],
                108:  [180, 126, 160],
                109:  [80, 136, 142],
                110:  [130, 190, 198],
                111:  [160, 110, 116],
                112:  [210, 166, 160],
                113:  [500, 40, 60],
                114:  [130, 164, 152],
                115:  [210, 142, 178],
                116:  [60, 122, 100],
                117:  [110, 176, 150],
                118:  [90, 112, 126],
                119:  [160, 172, 160],
                120:  [60, 130, 128],
                121:  [120, 194, 192],
                122:  [80, 154, 196],
                123:  [140, 176, 180],
                124:  [130, 172, 134],
                125:  [130, 198, 160],
                126:  [130, 214, 158],
                127:  [130, 184, 186],
                128:  [150, 148, 184],
                129:  [40, 42, 84],
                130:  [190, 192, 196],
                131:  [260, 186, 190],
                132:  [96, 110, 110],
                133:  [110, 114, 128],
                134:  [260, 186, 168],
                135:  [130, 192, 174],
                136:  [130, 238, 178],
                137:  [130, 156, 158],
                138:  [70, 132, 160],
                139:  [140, 180, 202],
                140:  [60, 148, 142],
                141:  [120, 190, 190],
                142:  [160, 182, 162],
                143:  [320, 180, 180],
                144:  [180, 198, 242],
                145:  [180, 232, 194],
                146:  [180, 242, 194],
                147:  [82, 128, 110],
                148:  [122, 170, 152],
                149:  [182, 250, 212],
                150:  [212, 284, 202],
                151:  [200, 220, 220]
        }

    def getRarityByName(self, name):
        return self.RarityById(self[name])

    def getRarityById(self, pokemonId):
        for rarity in self.rarity:
            if pokemonId in self.rarity[rarity]:
                return rarity


class Rarity(object):
    CRITTER = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    EPIC = 5
    LEGENDARY = 6
    MYTHIC = 7

pokedex = Pokedex()
