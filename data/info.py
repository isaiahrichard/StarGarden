classes = [
    {"name": "Soldier", "health": 300, "attacks": [4, 8, 10], "mana": 100},
    # {"name": "Crusader", "health": 200, "attacks": [1, 15, 6], "mana": 140},
    # {"name": "Assassin", "health": 180, "attacks": [2, 9, 13], "mana": 180},
    # {"name": "Technomancer", "health": 150, "attacks": [3, 11, 16], "mana": 200},
    # {"name": "Engineer", "health": 210, "attacks": [4, 19, 11], "mana": 130},
]

# classes = [
#     {"name": "Soldier", "health": 300, "attacks": [0, 8, 10], "mana": 100},
# ]

moves = [
    {"id": 0, "name": "Slap", "damage": 10, "mana_cost": 0},
    {"id": 1, "name": "Laser Blast", "damage": 20, "mana_cost": 10},
    {"id": 2, "name": "Plasma Strike", "damage": 40, "mana_cost": 20},
    {"id": 3, "name": "Ion Cannon", "damage": 50, "mana_cost": 20},
    {"id": 4, "name": "Quantum Surge", "damage": 60, "mana_cost": 30},
    {"id": 5, "name": "Nanobot Swarm", "damage": 40, "mana_cost": 20},
    {"id": 6, "name": "Gravity Well", "damage": 30, "mana_cost": 10},
    {"id": 7, "name": "Temporal Rift", "damage": 50, "mana_cost": 20},
    {"id": 8, "name": "Dark Matter Beam", "damage": 70, "mana_cost": 30},
    {"id": 9, "name": "Disintegration Wave", "damage": 40, "mana_cost": 20},
    {"id": 10, "name": "Hypernova Burst", "damage": 60, "mana_cost": 30},
    {"id": 11, "name": "Nova Blast", "damage": 70, "mana_cost": 30},
    {"id": 12, "name": "Cybernetic Augment", "damage": -60, "mana_cost": 30},
    {"id": 13, "name": "Plasma Cannon", "damage": 50, "mana_cost": 20},
    {"id": 14, "name": "Quantum Leap", "damage": 70, "mana_cost": 30},
    {"id": 15, "name": "Nanotech Repair", "damage": -30, "mana_cost": 10},
    {"id": 16, "name": "Gravity Field", "damage": 20, "mana_cost": 10},
    {"id": 17, "name": "Time Warp", "damage": 50, "mana_cost": 20},
    {"id": 18, "name": "Black Hole", "damage": 80, "mana_cost": 40},
    {"id": 19, "name": "Particle Beam", "damage": 40, "mana_cost": 20},
    {"id": 20, "name": "Supernova", "damage": 90, "mana_cost": 40},
]

enemyList = [
    {"name": "Robo-Sentinel", "health": 150, "attacks": [9, 4], "mana": 130},
    {"name": "Plasma Drone", "health": 120, "attacks": [1, 11, 2], "mana": 170},
    {"name": "Nanobot Assassin", "health": 100, "attacks": [2, 13], "mana": 200},
    {"name": "Cybernetic Behemoth", "health": 200, "attacks": [3, 14], "mana": 100},
    {"name": "Astro-Marauder", "health": 180, "attacks": [4, 19, 15], "mana": 110},
    {"name": "Galactic Enforcer", "health": 160, "attacks": [5, 14, 11], "mana": 120},
    {"name": "Quantum Stalker", "health": 140, "attacks": [6, 4], "mana": 140},
    {"name": "Exo-Warrior", "health": 130, "attacks": [7, 6], "mana": 150},
    {"name": "Ionized Specter", "health": 110, "attacks": [8], "mana": 180},
    {"name": "Neural Disruptor", "health": 190, "attacks": [9, 5], "mana": 100},
    {"name": "Plasma Wraith", "health": 170, "attacks": [10], "mana": 110},
    {"name": "Cosmic Annihilator", "health": 150, "attacks": [11, 3], "mana": 130},
    {"name": "Astro-Swarm", "health": 120, "attacks": [12, 17], "mana": 170},
    {"name": "Nebula Predator", "health": 100, "attacks": [13], "mana": 200},
    {"name": "Particle Destructor", "health": 200, "attacks": [14], "mana": 100},
    {"name": "Xeno-Berserker", "health": 180, "attacks": [15, 3], "mana": 110},
    {"name": "Plasma Titan", "health": 160, "attacks": [16, 12], "mana": 120},
    {"name": "Quantum Harbinger", "health": 140, "attacks": [17], "mana": 140},
    {"name": "Hypernova Sentinel", "health": 130, "attacks": [18, 2], "mana": 150},
    {"name": "Void Reaver", "health": 110, "attacks": [19, 4], "mana": 180},
]

planet_names = [
    "Xenoria",
    "Aetheron",
    "Nebulon",
    "Chronos",
    "Zephyria",
    "Stellara",
    "Galactis",
    "Aurion",
    "Exolara",
    "Celestria",
    "Elysium",
    "Phobos",
    "Eridania",
    "Serenia",
    "Andromeda",
    "Quasar",
    "Luminara",
    "Pulsara",
    "Zion",
    "Olympia",
]

atmosphere_options = [
    "Electro-plasmic",
    "Radiant Ether",
    "Ionized Mists",
    "Cosmic Vapors",
    "Neural Haze",
]


class Colours:
    def __init__(self):
        self.red = "\033[91m"
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.cyan = "\033[96m"
        self.white = "\033[97m"
        self.yellow = "\033[93m"
        self.magenta = "\033[95m"
        self.grey = "\033[90m"
        self.black = "\033[90m"
        self.default = "\033[0m"


colour = Colours()
