from util import ConstReflect


class Rarity(ConstReflect):
    """Enums for pokemon rarity. sort of subjective."""
    CRITTER = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    EPIC = 5
    LEGENDARY = 6
    MYTHIC = 7


class Pokedex(ConstReflect):
    """Class to contain static Pokemon data"""

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

    _evolves = {
        MISSINGNO: 0, BULBASAUR: 25, IVYSAUR: 100, VENUSAUR: 0,
        CHARMANDER: 25, CHARMELEON: 100, CHARIZARD: 0, SQUIRTLE: 25,
        WARTORTLE: 100, BLASTOISE: 0, CATERPIE: 12, METAPOD: 50,
        BUTTERFREE: 0, WEEDLE: 12, KAKUNA: 50, BEEDRILL: 0, PIDGEY: 12,
        PIDGEOTTO: 50, PIDGEOT: 0, RATTATA: 25, RATICATE: 0, SPEAROW: 50,
        FEAROW: 0, EKANS: 50, ARBOK: 0, PIKACHU: 50, RAICHU: 0,
        SANDSHREW: 50, SANDSLASH: 0, NIDORAN_FEMALE: 25, NIDORINA: 100,
        NIDOQUEEN: 0, NIDORAN_MALE: 25, NIDORINO: 100, NIDOKING: 0,
        CLEFAIRY: 50, CLEFABLE: 0, VULPIX: 50, NINETALES: 0, JIGGLYPUFF: 50,
        WIGGLYTUFF: 0, ZUBAT: 50, GOLBAT: 0, ODDISH: 25, GLOOM: 100,
        VILEPLUME: 0, PARAS: 50, PARASECT: 0, VENONAT: 50, VENOMOTH: 0,
        DIGLETT: 50, DUGTRIO: 0, MEOWTH: 50, PERSIAN: 0, PSYDUCK: 50,
        GOLDUCK: 0, MANKEY: 50, PRIMEAPE: 0, GROWLITHE: 50, ARCANINE: 0,
        POLIWAG: 25, POLIWHIRL: 100, POLIWRATH: 0, ABRA: 25, KADABRA: 100,
        ALAKAZAM: 0, MACHOP: 25, MACHOKE: 100, MACHAMP: 0, BELLSPROUT: 25,
        WEEPINBELL: 100, VICTREEBEL: 0, TENTACOOL: 50, TENTACRUEL: 0,
        GEODUDE: 25, GRAVELER: 100, GOLEM: 0, PONYTA: 50, RAPIDASH: 0,
        SLOWPOKE: 50, SLOWBRO: 0, MAGNEMITE: 50, MAGNETON: 0, FARFETCHD: 0,
        DODUO: 50, DODRIO: 0, SEEL: 50, DEWGONG: 0, GRIMER: 50, MUK: 0,
        SHELLDER: 50, CLOYSTER: 0, GASTLY: 25, HAUNTER: 100, GENGAR: 0,
        ONIX: 0, DROWZEE: 50, HYPNO: 0, KRABBY: 50, KINGLER: 0, VOLTORB: 50,
        ELECTRODE: 0, EXEGGCUTE: 50, EXEGGUTOR: 0, CUBONE: 50, MAROWAK: 0,
        HITMONLEE: 0, HITMONCHAN: 0, LICKITUNG: 0, KOFFING: 50, WEEZING: 0,
        RHYHORN: 50, RHYDON: 0, CHANSEY: 0, TANGELA: 0, KANGASKHAN: 0,
        HORSEA: 50, SEADRA: 0, GOLDEEN: 50, SEAKING: 0, STARYU: 50, STARMIE: 0,
        MR_MIME: 0, SCYTHER: 0, JYNX: 0, ELECTABUZZ: 0, MAGMAR: 0, PINSIR: 0,
        TAUROS: 0, MAGIKARP: 400, GYARADOS: 0, LAPRAS: 0, DITTO: 0, EEVEE: 25,
        VAPOREON: 0, JOLTEON: 0, FLAREON: 0, PORYGON: 0, OMANYTE: 50,
        OMASTAR: 0, KABUTO: 50, KABUTOPS: 0, AERODACTYL: 0, SNORLAX: 0,
        ARTICUNO: 0, ZAPDOS: 0, MOLTRES: 0, DRATINI: 25, DRAGONAIR: 100,
        DRAGONITE: 0, MEWTWO: 0, MEW: 0
    }

    _families = {
        BULBASAUR: BULBASAUR, IVYSAUR: BULBASAUR, VENUSAUR: BULBASAUR,
        CHARMANDER: CHARMANDER, CHARMELEON: CHARMANDER, CHARIZARD: CHARMANDER,
        SQUIRTLE: SQUIRTLE, WARTORTLE: SQUIRTLE, BLASTOISE: SQUIRTLE,
        CATERPIE: CATERPIE, METAPOD: CATERPIE, BUTTERFREE: CATERPIE,
        WEEDLE: WEEDLE, KAKUNA: WEEDLE, BEEDRILL: WEEDLE, PIDGEY: PIDGEY,
        PIDGEOTTO: PIDGEY, PIDGEOT: PIDGEY, RATTATA: RATTATA,
        RATICATE: RATTATA, SPEAROW: SPEAROW, FEAROW: SPEAROW, EKANS: EKANS,
        ARBOK: EKANS, PIKACHU: PIKACHU, RAICHU: PIKACHU, SANDSHREW: SANDSHREW,
        SANDSLASH: SANDSHREW, NIDORAN_FEMALE: NIDORAN_FEMALE,
        NIDORINA: NIDORAN_FEMALE, NIDOQUEEN: NIDORAN_FEMALE,
        NIDORAN_MALE: NIDORAN_MALE, NIDORINO: NIDORAN_MALE,
        NIDOKING: NIDORAN_MALE, CLEFAIRY: CLEFAIRY, CLEFABLE: CLEFAIRY,
        VULPIX: VULPIX, NINETALES: VULPIX, JIGGLYPUFF: JIGGLYPUFF,
        WIGGLYTUFF: JIGGLYPUFF, ZUBAT: ZUBAT, GOLBAT: ZUBAT, ODDISH: ODDISH,
        GLOOM: ODDISH, VILEPLUME: ODDISH, PARAS: PARAS, PARASECT: PARAS,
        VENONAT: VENONAT, VENOMOTH: VENONAT, DIGLETT: DIGLETT,
        DUGTRIO: DIGLETT, MEOWTH: MEOWTH, PERSIAN: MEOWTH, PSYDUCK: PSYDUCK,
        GOLDUCK: PSYDUCK, MANKEY: MANKEY, PRIMEAPE: MANKEY,
        GROWLITHE: GROWLITHE, ARCANINE: GROWLITHE, POLIWAG: POLIWAG,
        POLIWHIRL: POLIWAG, POLIWRATH: POLIWAG, ABRA: ABRA, KADABRA: ABRA,
        ALAKAZAM: ABRA, MACHOP: MACHOP, MACHOKE: MACHOP, MACHAMP: MACHOP,
        BELLSPROUT: BELLSPROUT, WEEPINBELL: BELLSPROUT, VICTREEBEL: BELLSPROUT,
        TENTACOOL: TENTACOOL, TENTACRUEL: TENTACOOL, GEODUDE: GEODUDE,
        GRAVELER: GEODUDE, GOLEM: GEODUDE, PONYTA: PONYTA, RAPIDASH: PONYTA,
        SLOWPOKE: SLOWPOKE, SLOWBRO: SLOWPOKE, MAGNEMITE: MAGNEMITE,
        MAGNETON: MAGNEMITE, FARFETCHD: FARFETCHD, DODUO: DODUO, DODRIO: DODUO,
        SEEL: SEEL, DEWGONG: SEEL, GRIMER: GRIMER, MUK: GRIMER,
        SHELLDER: SHELLDER, CLOYSTER: SHELLDER, GASTLY: GASTLY,
        HAUNTER: GASTLY, GENGAR: GASTLY, ONIX: ONIX, DROWZEE: DROWZEE,
        HYPNO: DROWZEE, KRABBY: KRABBY, KINGLER: KRABBY, VOLTORB: VOLTORB,
        ELECTRODE: VOLTORB, EXEGGCUTE: EXEGGCUTE, EXEGGUTOR: EXEGGCUTE,
        CUBONE: CUBONE, MAROWAK: CUBONE, HITMONLEE: HITMONLEE,
        HITMONCHAN: HITMONCHAN, LICKITUNG: LICKITUNG, KOFFING: KOFFING,
        WEEZING: KOFFING, RHYHORN: RHYHORN, RHYDON: RHYHORN, CHANSEY: CHANSEY,
        TANGELA: TANGELA, KANGASKHAN: KANGASKHAN, HORSEA: HORSEA,
        SEADRA: HORSEA, GOLDEEN: GOLDEEN, SEAKING: GOLDEEN, STARYU: STARYU,
        STARMIE: STARYU, MR_MIME: MR_MIME, SCYTHER: SCYTHER, JYNX: JYNX,
        ELECTABUZZ: ELECTABUZZ, MAGMAR: MAGMAR, PINSIR: PINSIR, TAUROS: TAUROS,
        MAGIKARP: MAGIKARP, GYARADOS: MAGIKARP, LAPRAS: LAPRAS, DITTO: DITTO,
        EEVEE: EEVEE, VAPOREON: EEVEE, JOLTEON: JOLTEON, FLAREON: FLAREON,
        PORYGON: PORYGON, OMANYTE: OMANYTE, OMASTAR: OMANYTE, KABUTO: KABUTO,
        KABUTOPS: KABUTO, AERODACTYL: AERODACTYL, SNORLAX: SNORLAX,
        ARTICUNO: ARTICUNO, ZAPDOS: ZAPDOS, MOLTRES: MOLTRES, DRATINI: DRATINI,
        DRAGONAIR: DRATINI, DRAGONITE: DRATINI, MEWTWO: MEWTWO, MEW: MEW
    }

    _rarity = {
        Rarity.MYTHIC: [MEW],
        Rarity.LEGENDARY: [
            ZAPDOS, MOLTRES, MEWTWO, ARTICUNO
        ],
        Rarity.EPIC: [
            DITTO, VENUSAUR, TAUROS, DRAGONITE, CLEFABLE,
            CHARIZARD, BLASTOISE
        ],
        Rarity.VERY_RARE: [
            WEEPINBELL, WARTORTLE, VILEPLUME, VICTREEBEL,
            VENOMOTH, VAPOREON, SLOWBRO, RAICHU, POLIWRATH,
            PINSIR, PIDGEOT, OMASTAR, NIDOQUEEN, NIDOKING,
            MUK, MAROWAK, LAPRAS, KANGASKHAN, KABUTOPS, IVYSAUR,
            GYARADOS, GOLEM, GENGAR, EXEGGUTOR, DRAGONAIR, DEWGONG,
            CHARMELEON, BEEDRILL, ALAKAZAM
        ],
        Rarity.RARE: [
            WIGGLYTUFF, WEEZING, TENTACRUEL, TANGELA,
            STARMIE, SNORLAX, SCYTHER, SEAKING, SEADRA,
            RHYDON, RAPIDASH, PRIMEAPE, PORYGON, POLIWHIRL,
            PARASECT, ONIX, OMANYTE, NINETALES, NIDORINO,
            NIDORINA, MR_MIME, MAGMAR, MACHOKE, MACHAMP,
            LICKITUNG, KINGLER, JOLTEON, HYPNO, HITMONCHAN,
            GLOOM, GOLDUCK, FLAREON, FEAROW, FARFETCHD,
            ELECTABUZZ, DUGTRIO, DRATINI, DODRIO, CLOYSTER,
            CHANSEY, BUTTERFREE, ARCANINE, AERODACTYL
        ],
        Rarity.UNCOMMON: [
            VULPIX, TENTACOOL, STARYU, SQUIRTLE, SPEAROW,
            SHELLDER, SEEL, SANDSLASH, RHYHORN, RATICATE,
            PSYDUCK, PONYTA, PIKACHU, PIDGEOTTO, PERSIAN,
            METAPOD, MAGNETON, KOFFING, KADABRA, KABUTO,
            KAKUNA, JYNX, JIGGLYPUFF, HORSEA, HITMONLEE,
            HAUNTER, GROWLITHE, GRIMER, GRAVELER, GOLBAT,
            EXEGGCUTE, ELECTRODE, CUBONE, CLEFAIRY, CHARMANDER,
            BULBASAUR, ARBOK, ABRA
        ],
        Rarity.COMMON: [
            WEEDLE, VOLTORB, VENONAT, SLOWPOKE, SANDSHREW,
            POLIWAG, PARAS, ODDISH, NIDORAN_MALE, NIDORAN_FEMALE,
            MEOWTH, MANKEY, MAGNEMITE, MAGIKARP, MACHOP, KRABBY,
            GOLDEEN, GEODUDE, GASTLY, EEVEE, EKANS, DROWZEE,
            DODUO, DIGLETT, CATERPIE, BELLSPROUT
        ],
        Rarity.CRITTER: [ZUBAT, PIDGEY, RATTATA]
    }


    def __init__(self):
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

    def getRarityById(self, pokemonId):
        for rarity in self.rarity:
            if pokemonId in self._rarity[rarity]:
                return rarity
        return 0

    def getRarityByName(self, name):
        return self.getRarityById(self[name])

    @property
    def rarity(self):
        return self._rarity

    @property
    def families(self):
        return self._families

    @property
    def evolves(self):
        return self._evolves

pokedex = Pokedex()
