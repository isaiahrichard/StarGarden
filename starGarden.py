import time
import numpy as num
import sys
import random
class Player:
    def __init__(self, name, health, moves):
        self.name = name 
        self.moves = moves
        self.health = health

    def fight(self, enemy):
        print(f"{self.name} V.S {enemy.name}")
        print(f"\n{self.name.ljust(23)}Health {format_health_bar(self.health)}{self.health}")
        print(f"{enemy.name.ljust(23)}Health {format_health_bar(enemy.health)}{enemy.health}\n")
        time.sleep(1)

        while self.health >= 0 and enemy.health >= 0: 
            delay_print("Select your move")
            for index, move in enumerate(self.moves, 1):
                print(f"{index}. {moves[move]['name']} | {moves[move]['damage']}")
            yourMove = int(star_input("")) - 1
            delay_print(f"You hit {enemy.name} with {moves[self.moves[yourMove]]['name']} for {moves[self.moves[yourMove]]['damage']} damage!")
            enemy.health  -= moves[self.moves[yourMove]]['damage']
            if enemy.health <=0:
                break
            time.sleep(1)
            print(f"\n{self.name.ljust(23)}Health {format_health_bar(self.health)}{self.health}")
            print(f"{enemy.name.ljust(23)}Health {format_health_bar(enemy.health)}{enemy.health}\n")
            theirMove = random.randint(0, len(enemy.moves) - 1)
            time.sleep(1)
            delay_print(f"{enemy.name} hit you with {moves[enemy.moves[theirMove]]['name']} for {moves[enemy.moves[theirMove]]['damage']} damage!")
            self.health  -= moves[enemy.moves[theirMove]]['damage']
            if self.health <=0:
                break
            time.sleep(1)
            print(f"\n{self.name.ljust(23)}Health {format_health_bar(self.health)}{self.health}")
            print(f"{enemy.name.ljust(23)}Health {format_health_bar(enemy.health)}{enemy.health}\n")

        if self.health <= 0:
            delay_print(f"You fainted at the hands of {enemy.name}")
        else:
            delay_print(f"You knocked out {enemy.name}! Good job!")
            currentPlanet.enemies -= 1

        if currentPlanet.enemies == 0:
            delay_print(f"Planet {currentPlanet.name} cleared!")
            currentPlanet.cleared = True


class Enemy:
    def __init__(self, name, health, moves):
        self.name = name 
        self.moves = moves
        self.health = health

class Planet:
    def __init__(self, name, description, atmosphere, cleared, enemies):
        self.name = name
        self.description = description
        self.atmosphere = atmosphere
        self.cleared = cleared
        self.enemies = enemies

currentPlanet = Planet("earth", "home", "air or sum", False, 1)
player = Player("placeholder", 0, [])

def delay_print(string):
    sys.stdout.write("> ")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def star_input(query):
    val = input(query)
    
    if val.lower() == 'quit':
        delay_print("Thank you for playing. The stars will be waiting for you.")
        sys.exit()
    else:
        return val

def print_banner():
    print(" ____  _                ____               _            ")
    time.sleep(0.25)
    print("/ ___|| |_ __ _ _ __   / ___| __ _ _ __ __| | ___ _ __  ")
    time.sleep(0.25)
    print("\___ \| __/ _` | '__| | |  _ / _` | '__/ _` |/ _ \ '_ \ ")
    time.sleep(0.25)
    print(" ___) | || (_| | |    | |_| | (_| | | | (_| |  __/ | | |")
    time.sleep(0.25)
    print("|____/ \__\__,_|_|     \____|\__,_|_|  \__,_|\___|_| |_|")
    time.sleep(0.25)
    print()

def print_rocket():
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("       /\\")
    time.sleep(0.25)
    print("      /  \\")
    time.sleep(0.25)
    print("     /    \\")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("     |    |")
    time.sleep(0.25)
    print("    /| |  |\\")
    time.sleep(0.25)
    print("   / | |  | \\")
    time.sleep(0.25)
    print("  |  | |  |  |")
    time.sleep(0.25)
    print("  |  | |  |  |")
    time.sleep(0.25)
    print("  |__|_|__|_ |")
    time.sleep(0.25)
    print("      /_\\    ")
    time.sleep(0.25)
    print("       /\\  ")
    time.sleep(0.25)
    print("      /  \\")
    time.sleep(0.25)
    print("     /    \\")
    time.sleep(0.25)
    print("    /      \\ ")
    time.sleep(0.25)
    print("    \\/\\/\\/\\/")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)

def select_class():
    print("Choose your class")
    validClass = False
    startingClass = 0
    while not validClass:
        for index, charClass in enumerate(classes, 1):
            display_class_info(charClass, index)
        startingClass = int(star_input("Choose your starting class: ")) - 1
        if startingClass > -1 and startingClass < len(classes):
            validClass = True
        else:
            print("Invalid class selection, try again")
    delay_print(f"You selected {classes[startingClass]['name']}")
    return classes[startingClass]

def format_health_bar(health):
    return "="* int(health / 10)

def generate_planets():
    for planet in planet_names:
            description = generate_description(planet)
            atmo = random.choice(atmosphere_options)
            planets.append(Planet(planet, description, atmo, False, random.randint(1, 3)))

def display_planet_info(planet, index):
    time.sleep(0.5)
    delay_print(f"{index}. {planet.name}: ")
    time.sleep(0.25)
    print(f"\tDescription: {planet.description}")
    time.sleep(0.25)
    print(f"\tAtmosphere: {planet.atmosphere}")
    time.sleep(0.25)
    print()

def display_class_info(gameClass, index):
    time.sleep(0.5)
    delay_print(f"{index}. {gameClass['name']}: ")
    time.sleep(0.25)
    print(f"\tHealth: {gameClass['health']}")
    time.sleep(0.25)
    print("\tStarting Moves:")
    time.sleep(0.25)
    for move in gameClass["attack"]:
        print(f"\t\t{moves[move]['name']} | {moves[move]['damage']}")
        time.sleep(0.25)
    print()


def create_enemy(index):
    enemyObj = enemyList[index]
    return Enemy(enemyObj["name"], enemyObj["health"], enemyObj["attacks"])

def generate_description(name):
    prefixes = ["A mysterious", "An enigmatic", "A captivating", "A mesmerizing", "A breathtaking"]
    suffixes = ["beauty", "world", "planet", "realm", "celestial body"]
    return f"{random.choice(prefixes)} {name}, a {random.choice(suffixes)} filled with wonders and secrets."

def intro():
    delay_print("Dear player, prepare for an epic odyssey as you, the intrepid space traveler, unleash your cosmic might to defend Earth from intergalactic foes, merging two worlds into an unforgettable battle.")
    time.sleep(1)
    delay_print("Before you can begin your epic journey, an enemy attacks you")
    enemy = create_enemy(0)
    player.fight(enemy)

def explore_landscape():
    event = random.choices(exploration_events, [event['weight'] for event in exploration_events])[0]
    delay_print(exploration_mapping[event['id']])
    event['action']()

def encounter_enemy():
    enemyIndex = random.randrange(len(enemyList))
    enemy = create_enemy(enemyIndex)
    player.fight(enemy)

def find_ruins():
    print("Found ruins")

def find_shopkeeper():
    print("Found shopkeeper")


# classes = [
#     {"name": "Soldier", "health": 300, "attack": [0, 8, 10]},
#     {"name": "Crusader", "health": 200, "attack": [1, 15, 6]},
#     {"name": "Assassin", "health": 180, "attack": [2, 9, 13]},
#     {"name": "Technomancer", "health": 150, "attack": [3, 11, 16]},
#     {"name": "Engineer", "health": 210, "attack": [4, 19, 11]},
# ]

classes = [
    {"name": "Soldier", "health": 300, "attack": [0, 8, 10]},
]


moves = [
    {"id": 1, "name": "Laser Blast", "damage": 20},
    {"id": 2, "name": "Plasma Strike", "damage": 40},
    {"id": 3, "name": "Ion Cannon", "damage": 50},
    {"id": 4, "name": "Quantum Surge", "damage": 60},
    {"id": 5, "name": "Nanobot Swarm", "damage": 40},
    {"id": 6, "name": "Gravity Well", "damage": 30},
    {"id": 7, "name": "Temporal Rift", "damage": 50},
    {"id": 8, "name": "Dark Matter Beam", "damage": 70},
    {"id": 9, "name": "Disintegration Wave", "damage": 40},
    {"id": 10, "name": "Hypernova Burst", "damage": 60},
    {"id": 11, "name": "Nova Blast", "damage": 70},
    {"id": 12, "name": "Cybernetic Augment", "damage": -60},
    {"id": 13, "name": "Plasma Cannon", "damage": 50},
    {"id": 14, "name": "Quantum Leap", "damage": 70},
    {"id": 15, "name": "Nanotech Repair", "damage": -30},
    {"id": 16, "name": "Gravity Field", "damage": 20},
    {"id": 17, "name": "Time Warp", "damage": 50},
    {"id": 18, "name": "Black Hole", "damage": 80},
    {"id": 19, "name": "Particle Beam", "damage": 40},
    {"id": 20, "name": "Supernova", "damage": 90}
]

enemyList = [
    {"name": "Robo-Sentinel", "health": 150, "attacks": [0, 4]},
    {"name": "Plasma Drone", "health": 120, "attacks": [1, 11, 2]},
    {"name": "Nanobot Assassin", "health": 100, "attacks": [2, 13]},
    {"name": "Cybernetic Behemoth", "health": 200, "attacks": [3, 14]},
    {"name": "Astro-Marauder", "health": 180, "attacks": [4, 19, 15]},
    {"name": "Galactic Enforcer", "health": 160, "attacks": [5, 14, 11]},
    {"name": "Quantum Stalker", "health": 140, "attacks": [6, 4]},
    {"name": "Exo-Warrior", "health": 130, "attacks": [7, 6]},
    {"name": "Ionized Specter", "health": 110, "attacks": [8]},
    {"name": "Neural Disruptor", "health": 190, "attacks": [9, 5]},
    {"name": "Plasma Wraith", "health": 170, "attacks": [10]},
    {"name": "Cosmic Annihilator", "health": 150, "attacks": [11, 3]},
    {"name": "Astro-Swarm", "health": 120, "attacks": [12, 17]},
    {"name": "Nebula Predator", "health": 100, "attacks": [13]},
    {"name": "Particle Destructor", "health": 200, "attacks": [14]},
    {"name": "Xeno-Berserker", "health": 180, "attacks": [15, 3]},
    {"name": "Plasma Titan", "health": 160, "attacks": [16, 12]},
    {"name": "Quantum Harbinger", "health": 140, "attacks": [17]},
    {"name": "Hypernova Sentinel", "health": 130, "attacks": [18, 2]},
    {"name": "Void Reaver", "health": 110, "attacks": [19, 4]}
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
        "Olympia"
    ]

atmosphere_options = [
        "Electro-plasmic",
        "Radiant Ether",
        "Ionized Mists",
        "Cosmic Vapors",
        "Neural Haze"
    ]


exploration_events = [
    {"event": "Encounter Enemy", "weight": 0.5, "action": encounter_enemy, "id": "1"},
    {"event": "Find Ruins", "weight": 0.3, "action": find_ruins, "id": "2"},
    {"event": "Find Shopkeeper", "weight": 0.2, "action": find_shopkeeper,"id": "3"},
]

exploration_mapping = {
    "1": f"While wandering the landscape of {currentPlanet.name} you are ambushed",
    "2": f"You discover ancient ruins while exploring {currentPlanet.name}",
    "3": f"You stumble across a humble shopkeeper on the surface of {currentPlanet.name}"
}

items = [
    {"name": "Energy Shield", "type": "armor", "value": 15},
    {"name": "Jet Boots", "type": "armor", "value": 10},
    {"name": "Nanobot Injector", "type": "heal", "value": 30},
    {"name": "Cloaking Device", "type": "buff", "value": 5},
    {"name": "Ionized Armor", "type": "armor", "value": 20},
    {"name": "Plasma Grenade", "type": "buff", "value": 30},
    {"name": "Holographic Decoy", "type": "buff", "value": 3},
    {"name": "Antigravity Boots", "type": "armor", "value": 8},
    {"name": "Force Field Generator", "type": "armor", "value": 25},
    {"name": "EMP Grenade", "type": "buff", "value": 25},
    {"name": "Medkit", "type": "heal", "value": 40},
    {"name": "Power Armor", "type": "armor", "value": 30},
    {"name": "Energy Pack", "type": "buff", "value": 20},
    {"name": "Repair Drone", "type": "heal", "value": 50}
]

planets = []
if __name__ == '__main__':
    print_banner()
    playerName = star_input("Enter your characters name: ")
    classObj = select_class()
    player.name = playerName
    player.health = classObj['health']
    player.moves = classObj['attack']
    generate_planets()
    # intro()
    while True:
        availablePlanets = [planet for planet in planets if not planet.cleared and planet.name != currentPlanet.name]

        if not availablePlanets:
            delay_print("You've explored all the planets in this solar system. Go explore some grass on Earth")
            sys.exit()

        delay_print("Select the next planet in your journey: ")
        nextPlanets = random.sample(availablePlanets, 4)
        for index, planet in enumerate(nextPlanets, 1):
            display_planet_info(planet, index)
        nextPlanet = int(star_input("")) - 1

        # Issue selecting planet 
        currentPlanet = nextPlanets[nextPlanet]
        delay_print(f"Prepare for launch to {currentPlanet.name}")
        time.sleep(1)
        print_rocket()
        delay_print(f"You have arrived on {currentPlanet.name}")
        delay_print("What would you like to do?")
        delay_print("1. Explore Landscape")
        delay_print("2. Travel to a new planet")
        action = star_input("")
        if action == "1":
            explore_landscape()












