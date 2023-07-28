from time import sleep
import random
from helpers.text import delay_print, display_selectable_list
from helpers.combat import player_turn, enemy_turn
from helpers.general import get_required_exp
from data.info import moves, colour


class Player:
    def __init__(self, name, starting_class):
        self.name = name
        self.moves = [moves[0]] + [moves[i] for i in starting_class["attacks"]]
        self.health = starting_class["health"]
        self.max_health = starting_class["health"]
        self.mana = starting_class["mana"]
        self.max_mana = starting_class["mana"]
        self.items = {
            "health": {"value": 30, "count": 4},
            "mana": {"value": 10, "count": 0},
        }
        self.level = 1
        self.next_level_exp = get_required_exp(1)
        self.gold = 0

    def fight(self, enemy, current_planet):
        delay_print(f"{self.name} V.S {enemy.name}")
        sleep(0.5)
        while self.health >= 0 and enemy.health >= 0:
            status = player_turn(player=self, enemy=enemy)
            if status != "continue":
                break
            sleep(0.5)
            enemy_turn(player=self, enemy=enemy)

        if self.health <= 0:
            delay_print(f"You fainted at the hands of {enemy.name}")
        elif enemy.health <= 0:
            self.gold += random.randint(1, 6) * self.level
            delay_print(f"You knocked out {enemy.name}! Good job!")
            current_planet.enemies -= 1

        if current_planet.enemies == 0:
            delay_print(f"Planet {current_planet.name} cleared!")
            self.gold += random.randint(8, 15) * self.level
            current_planet.cleared = True

    def add_item(self, item):
        self.items[item]["count"] += 1

    def use_item(self, item):
        if self.items[item]["count"]:
            if item == "health":
                self.health = min(
                    self.health + self.items[item]["value"], self.max_health
                )
            elif item == "mana":
                self.mana = min(self.mana + self.items[item]["value"], self.max_mana)
            self.items[item]["count"] -= 1
        else:
            delay_print("Please select an item you have")

    def add_exp(self, exp):
        self.next_level_exp -= exp
        if self.next_level_exp <= 0:
            delay_print(f"{self.name} is now level {self.level + 1}!")
            diff = self.next_level_exp * (-1)
            self.level += 1
            self.next_level_exp = get_required_exp(self.level)
            self.next_level_exp -= diff
            delay_print("Choose an upgrade")
            selection = display_selectable_list(["+10 health", "+5 mana"])
            if selection == "1":
                self.max_health += 10
            elif selection == "2":
                self.max_mana += 5

            self.health = self.max_health
            self.mana = self.max_mana

            if not self.level % 5:
                delay_print("Choose a new attack to learn")
                move_ids = [move["id"] for move in self.moves]
                new_moves = [move for move in moves if move["id"] not in move_ids]
                new_moves = random.choices(new_moves, 4)
                selection = display_selectable_list(
                    [
                        f"{move['name']} ({colour.red}{move['damage']}{colour.default}|{colour.blue}{move['mana_cost']}{colour.default})"
                        for move in new_moves
                    ]
                )


class Enemy:
    def __init__(self, enemy):
        self.name = enemy["name"]
        self.moves = [moves[0]] + [moves[i] for i in enemy["attacks"]]
        self.health = enemy["health"]
        self.max_health = enemy["health"]
        self.mana = enemy["mana"]
        self.max_mana = enemy["mana"]


class Planet:
    def __init__(self, name, description, atmosphere, cleared, enemies):
        self.name = name
        self.description = description
        self.atmosphere = atmosphere
        self.cleared = cleared
        self.enemies = enemies
