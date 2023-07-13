import time
import numpy as num
import sys
import random


def delayPrint(string):
    sys.stdout.write("> ")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

class Entity:
    def __init__(self, name, health, moves):
        self.name = name 
        self.moves = moves
        self.health = health

    def fight(self, enemy):
        print(f"{self.name} V.S {enemy.name}")
        print(f"\n{self.name.ljust(23)}Health {formatHealthBar(self.health)}")
        print(f"{enemy.name.ljust(23)}Health {formatHealthBar(enemy.health)}\n")
        time.sleep(1)

        while self.health >= 0 and enemy.health >= 0: 
            delayPrint("Select your move")
            for index, move in enumerate(self.moves, 1):
                print(f"{index}. {moves[move]['name']} | {moves[move]['damage']}")
            yourMove = int(input()) - 1
            delayPrint(f"You hit {enemy.name} with {moves[yourMove]['name']} for {moves[yourMove]['damage']} damage")
            enemy.health  -= moves[yourMove]['damage']
            if enemy.health <=0:
                break
            time.sleep(1)
            print(f"\n{self.name.ljust(23)}Health {formatHealthBar(self.health)}")
            print(f"{enemy.name.ljust(23)}Health {formatHealthBar(enemy.health)}\n")
            theirMove = random.randint(0, len(enemy.moves) - 1)
            time.sleep(1)
            delayPrint(f"{enemy.name} hit you with {moves[theirMove]['name']} for {moves[theirMove]['damage']} damage")
            self.health  -= moves[theirMove]['damage']
            if self.health <=0:
                break
            time.sleep(1)
            print(f"\n{self.name.ljust(23)}Health {formatHealthBar(self.health)}")
            print(f"{enemy.name.ljust(23)}Health {formatHealthBar(enemy.health)}\n")

        if self.health <= 0:
            delayPrint(f"You fainted at the hands of {enemy.name}")
        else:
            delayPrint(f"You knocked out {enemy.name}")
            currentPlanet.enemies -= 1

        if currentPlanet.enemies == 0:
            delayPrint("Planet cleared!")
            currentPlanet.cleared = True


class Planet:
    def __init__(self, name, description, atmosphere, cleared, enemies):
        self.name = name
        self.description = description
        self.atmosphere = atmosphere
        self.cleared = cleared
        self.enemies = enemies

currentPlanet = Planet("earth", "home", "air or sum", False, 1)
player = Entity("placeholder", 0, [])

def selectClass(): 
    print("Choose your class")
    validClass = False
    startingClass = 0
    while not validClass:
        for index, charClass in enumerate(classes, 1):
            print(f"{index}. {charClass['name']}: ")
            print(f"    Health: {charClass['health']}")
            print("    Starting Moves:")
            for move in charClass["attack"]:
                print(f"        {moves[move]['name']} | {moves[move]['damage']}")
            print()
        startingClass = int(input("Choose your starting class: ")) - 1
        if startingClass > -1 and startingClass < len(classes) -1:
            validClass = True
        else:
            print("Invalid class selection, try again")
    return classes[startingClass]

def formatHealthBar(health):
    return "="* int(health / 10)

def print_formatted_string(name, health):
    formatted_string = f"{name.ljust(23)}HLTH    {'=' * health}"
    print(formatted_string)

def generatePlanets():
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
    for planet in planet_names:
            description = generate_description(planet)
            atmo = random.choice(atmosphere_options)
            planets.append(Planet(planet, description, atmo, False, random.randint(1, 3)))


def displayPlayerInfo():
    print(player.name)

def createEnemy(index):
    enemyObj = enemyList[index]
    return Entity(enemyObj["name"], enemyObj["health"], enemyObj["attacks"])

def generate_description(name):
    prefixes = ["A mysterious", "An enigmatic", "A captivating", "A mesmerizing", "A breathtaking"]
    suffixes = ["beauty", "world", "planet", "realm", "celestial body"]
    return f"{random.choice(prefixes)} {name}, a {random.choice(suffixes)} filled with wonders and secrets."

classes = [
    {"name": "Soldier", "health": 300, "attack": [0, 8, 11]},
    {"name": "Crusader", "health": 200, "attack": [1, 15, 6]},
    {"name": "Assassin", "health": 180, "attack": [2, 9, 13]},
    {"name": "Technomancer", "health": 150, "attack": [3, 11, 16]},
    {"name": "Engineer", "health": 210, "attack": [4, 19, 11]},
]


moves = [
    {"id": 1, "name": "Laser Blast", "damage": 20},
    {"id": 2, "name": "Plasma Strike", "damage": 100},
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

planets = []


if __name__ == '__main__':
    playerName = input("Enter your characters name: ")
    classObj = selectClass()
    player.name = playerName
    player.health = classObj['health']
    player.moves = classObj['attack']
    generatePlanets()
    print("Dear player, prepare for an epic odyssey as you, the intrepid space traveler, unleash your cosmic might to defend Earth from intergalactic foes, merging two worlds into an unforgettable battle.")
    time.sleep(1)
    print("Before you can begin your epic journey, an enemy attacks you")
    enemy = createEnemy(0)
    player.fight(enemy)
    while True:
        delayPrint("Select the planet you would like to visit")






