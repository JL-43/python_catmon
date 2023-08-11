TYPE_EFFECTIVENESS = {
    "Fire": {
        "super_effective": ["Grass"],
        "not_effective": ["Water", "Fire"],
    },
    "Water": {
        "super_effective": ["Fire"],
        "not_effective": ["Water", "Grass"],
    },
    "Grass": {
        "super_effective": ["Water"],
        "not_effective": ["Fire", "Grass"],
    },
    "Normal": {},
}

CATMON_TEMPLATES = {
    "mugi": {
        "name": "mugi",
        "type": "Fire",
        "health": 100,
        "max_health": 100,
        "moves": [],
        "atk": 15,
        "def_": 10,
        "sp_atk": 20,
        "sp_def": 10,
        "speed": 12,
        "level": 1,
    },
    "buwie": {
        "name": "buwie",
        "type": "Water",
        "health": 100,
        "max_health": 100,
        "moves": [],
        "atk": 12,
        "def_": 12,
        "sp_atk": 18,
        "sp_def": 12,
        "speed": 11,
        "level": 1,
    },
    "raffy": {
        "name": "raffy",
        "type": "Grass",
        "health": 100,
        "max_health": 100,
        "moves": [],
        "atk": 13,
        "def_": 15,
        "sp_atk": 17,
        "sp_def": 15,
        "speed": 10,
        "level": 1,
    },
}
