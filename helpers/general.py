from time import sleep
import random
from data.info import moves, colour
from helpers.text import delay_print, display_selectable_list


def display_planet_info(planet, index):
    sleep(0.5)
    delay_print(f"{index}. {planet.name}: ")
    sleep(0.25)
    print(f"\tDescription: {planet.description}")
    sleep(0.25)
    print(f"\tAtmosphere: {planet.atmosphere}")
    sleep(0.25)
    print()


def display_class_info(game_class, index):
    sleep(0.5)
    delay_print(f"{index}. {game_class['name']}: ")
    sleep(0.25)
    print(f"\tHealth: {game_class['health']}")
    sleep(0.25)
    print("\tStarting Moves:")
    sleep(0.25)
    for move_index in game_class["attacks"]:
        move = moves[move_index]
        print(
            f"\t\t{move['name']} ({colour.red}{move['damage']}{colour.default}|{colour.blue}{move['mana_cost']}{colour.default})"
        )
        sleep(0.25)
    print()


def display_selectable_items(items):
    item_strings = []
    for item_type, item_info in items.items():
        item_string = ""
        if item_type == "health":
            item_string = f"{item_type.capitalize()} potions: {colour.red}{'()' * item_info['count'] if item_info['count'] else 'None'}{colour.default}"
        if item_type == "mana":
            item_string = f"{item_type.capitalize()} potions: {colour.blue}{'[]' * item_info['count'] if item_info['count'] else 'None'}{colour.default}"
        item_strings.append(item_string)
    return display_selectable_list(item_strings)


def item_description(item):
    if item["type"] == "heal":
        return f"Heals the player {item['value']} health"


def generate_description(name):
    prefixes = [
        "A mysterious",
        "An enigmatic",
        "A captivating",
        "A mesmerizing",
        "A breathtaking",
    ]
    suffixes = ["beauty", "world", "planet", "realm", "celestial body"]
    return f"{random.choice(prefixes)} {name}, a {random.choice(suffixes)} filled with wonders and secrets."


def get_required_exp(level):
    return (2 * level * level) + (11 * level) + 86
