from time import sleep
import sys
import os
import random
from data.info import classes, enemyList, planet_names, atmosphere_options
from data.ascii_art import rocket_ship, banner
from helpers.general import (
    display_class_info,
    display_selectable_items,
    display_planet_info,
    generate_description,
)
from classes import Planet, Enemy, Player
from helpers.text import (
    star_input,
    delay_print,
    display_selectable_list,
    clear,
    print_ascii_art,
)


current_planet = Planet("Earth", "home", "air or sum", False, 1)
player = None


def select_class():
    print("Choose your class")
    valid_class = False
    starting_class = 0
    while not valid_class:
        for index, char_class in enumerate(classes, 1):
            display_class_info(char_class, index)
        starting_class = int(star_input("Choose your starting class: ")) - 1
        if starting_class > -1 and starting_class < len(classes):
            valid_class = True
        else:
            print("Invalid class selection, try again")
    delay_print(f"You selected {classes[starting_class]['name']}")
    return classes[starting_class]


def generate_planets():
    for planet in planet_names:
        description = generate_description(planet)
        atmo = random.choice(atmosphere_options)
        planets.append(Planet(planet, description, atmo, False, random.randint(1, 3)))


def create_enemy(index):
    enemy_obj = enemyList[index]
    return Enemy(enemy=enemy_obj)


def generate_shopkeeper_inventory():
    return {
        "health": {"count": random.randint(0, 5)},
        "mana": {"count": random.randint(0, 5)},
    }


def intro():
    clear()
    # delay_print(
    #     "Dear player, prepare for an epic odyssey as you, the intrepid space traveler, unleash your cosmic might to defend Earth from intergalactic foes, merging two worlds into an unforgettable battle."
    # )
    # sleep(0.5)
    # delay_print("Before you can begin your epic journey, an enemy attacks you")
    enemy = create_enemy(0)
    player.fight(enemy, current_planet)
    clear()


def explore_landscape():
    exploration_mapping = {
        "1": f"While wandering the landscape of {current_planet.name} you are ambushed",
        "2": f"You discover ancient ruins while exploring {current_planet.name}",
        "3": f"You stumble across a humble shopkeeper on the surface of {current_planet.name}",
    }
    event = random.choices(
        exploration_events, [event["weight"] for event in exploration_events]
    )[0]
    delay_print(exploration_mapping[event["id"]])
    event["action"]()


def encounter_enemy():
    enemy_index = random.randrange(len(enemyList))
    enemy = create_enemy(enemy_index)
    player.fight(enemy, current_planet)


def find_ruins():
    ruin_item = random.choice(["health", "mana"])
    ruin_events = [
        {
            "message": f"You find a {ruin_item} potion while scouring the ruin",
            "id": "1",
        },
        {
            "message": "You are caught searching the ruin by another treasure hunter",
            "id": "2",
        },
    ]
    search_event = random.choice(ruin_events)
    delay_print(search_event["message"])
    if search_event["id"] == "1":
        player.add_item(ruin_item)
    elif search_event["id"] == "2":
        encounter_enemy()


def find_shopkeeper():
    selection = display_selectable_list(
        ["See what's for sale", "Continue exploring"], delayed=True
    )
    if selection == "1":
        buying = True
        shop_inventory = generate_shopkeeper_inventory()
        while buying:
            selected_item = (
                "health" if display_selectable_items(shop_inventory) == "1" else "mana"
            )
            delay_print(f"Purchased {selected_item.capitalize()} potion")
            player.add_item(selected_item)
            shop_inventory[selected_item]["count"] -= 1
            delay_print("Continue shopping?")
            continue_val = display_selectable_list(["Yes", "No"], delayed=True)
            if continue_val == "2":
                buying = False


exploration_events = [
    {"event": "Encounter Enemy", "weight": 0.5, "action": encounter_enemy, "id": "1"},
    {"event": "Find Ruins", "weight": 0.3, "action": find_ruins, "id": "2"},
    {"event": "Find Shopkeeper", "weight": 0.2, "action": find_shopkeeper, "id": "3"},
]

planets = []

if __name__ == "__main__":
    os.system("color")
    print_ascii_art(banner)
    sleep(3)
    clear()
    playerName = star_input("Enter your characters name: ")
    clear()
    classObj = select_class()
    player = Player(name=playerName, starting_class=classObj)
    generate_planets()
    intro()
    while True:
        availablePlanets = [
            planet
            for planet in planets
            if not planet.cleared and planet.name != current_planet.name
        ]

        if not availablePlanets:
            delay_print(
                "You've explored all the planets in this solar system. Go explore some grass on Earth"
            )
            sys.exit()
        clear()
        delay_print("Select the next planet in your journey: ")
        nextPlanets = random.sample(availablePlanets, 4)
        for index, planet in enumerate(nextPlanets, 1):
            display_planet_info(planet, index)
        nextPlanet = int(star_input("")) - 1
        current_planet = nextPlanets[nextPlanet]
        clear()
        delay_print(f"Prepare for launch to {current_planet.name}")
        clear()
        print_ascii_art(rocket_ship)
        clear()
        delay_print(f"You have arrived on {current_planet.name}")
        exploring = True
        while exploring:
            action = display_selectable_list(
                ["Explore Landscape", "Travel to a new planet"], delayed=True
            )
            if action == "1":
                explore_landscape()
            if action == "2":
                exploring = False
