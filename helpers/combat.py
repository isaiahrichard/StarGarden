from helpers.text import display_selectable_list, delay_print, clear, star_input
from helpers.general import display_selectable_items
from time import sleep
from data.info import colour
import random

# display
bars = 20
remaining_health_symbol = "█"
lost_health_symbol = "_"


def display_resource_bars(entity) -> None:
    health_color = colour.red
    if entity.health > 0.66 * entity.max_health:
        health_color = colour.green
    elif entity.health > 0.33 * entity.max_health:
        health_color = colour.yellow

    remaining_player_health = round(entity.health / entity.max_health * bars)
    lost_player_health = bars - remaining_player_health
    remaining_player_mana = round(entity.mana / entity.max_mana * bars)
    lost_player_mana = bars - remaining_player_mana
    print(f"{entity.name}: ")
    print(
        f"{health_color}|{remaining_player_health * remaining_health_symbol}{lost_player_health * lost_health_symbol}|{entity.health}/{entity.max_health}{colour.default}\t{colour.blue}|{remaining_player_mana * remaining_health_symbol}{lost_player_mana * lost_health_symbol}|{entity.mana}/{entity.max_mana}{colour.default}"
    )


def player_turn(player, enemy) -> str:
    clear()
    print("==============================")
    display_resource_bars(player)
    print()
    display_resource_bars(enemy)
    selection = display_selectable_list(["Attack", "Items", "Flee"])
    if selection == "1":
        selecting_move = True
        selected_move = None
        while selecting_move:
            selected_move_index = int(display_selectable_moves(player)) - 1
            selected_move = player.moves[selected_move_index]
            if selected_move["mana_cost"] > player.mana:
                delay_print(
                    f"You do not have enough mana to cast {selected_move['name']}"
                )
                clear()
                print("==================")
                display_resource_bars(player)
                display_resource_bars(enemy)
            else:
                selecting_move = False
        player.mana -= selected_move["mana_cost"]
        if selected_move["damage"] < 0:
            delay_print(f"You healed {selected_move['damage']} HP")
            player.health = min(
                player.health + selected_move["damage"], player.max_health
            )
        else:
            delay_print(
                f"You hit {enemy.name} with {selected_move['name']} "
                f"for {selected_move['damage']} damage!"
            )
            enemy.health -= selected_move["damage"]
        if enemy.health <= 0:
            return "victory"
    elif selection == "2":
        selected_item = display_selectable_items(player.items)
        selected_item = "health" if selected_item == "1" else "mana"
        delay_print(
            f"You restored {player.items[selected_item]['value']} points of {selected_item}"
        )
        player.use_item(selected_item)
    elif selection == "3":
        delay_print(f"You fled from the {enemy.name}")
        return "defeat"
    return "continue"


def enemy_turn(player, enemy) -> None:
    clear()
    print("==================")
    display_resource_bars(player)
    display_resource_bars(enemy)
    print("==================")
    sleep(1)
    enemy_moves = [move for move in enemy.moves if move["mana_cost"]]
    enemy_move = random.choice(enemy_moves)
    if enemy_move["damage"] < 0:
        delay_print(f"{enemy.name} healed {enemy_move['damage']} HP")
        enemy.health = min(enemy.health + enemy_move["damage"], enemy.max_health)
    else:
        delay_print(
            f"{enemy.name} hit you with {enemy_move['name']} "
            f"for {enemy_move['damage']} damage!"
        )
        player.health -= enemy_move["damage"]


def display_selectable_moves(player) -> str:
    print("==============================")
    for index, move in enumerate(player.moves, 1):
        print_colour = (
            colour.default if move["mana_cost"] <= player.mana else colour.grey
        )
        print(
            f"{print_colour}{index} - {move['name']}{colour.default} ({colour.red}{move['damage']}{colour.default}|{colour.blue}{move['mana_cost']}{colour.default})"
        )
    print("==============================")
    selection = star_input("> ")
    return selection
