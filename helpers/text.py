import sys
from time import sleep
import os


def delay_print(string, flat=False):
    sys.stdout.write("" if flat else "> ")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    print()
    sleep(0.5)


def star_input(query):
    val = input(query)

    if val.lower() == "quit":
        delay_print("Thank you for playing. The stars will be waiting for you.")
        sys.exit()
    else:
        return val


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display_selectable_list(list, delayed=False):
    print("==============================")
    for index, item in enumerate(list, 1):
        if delayed:
            delay_print(f"{index} - {item}", flat=True)
        else:
            print(f"{index} - {item}")
    print("==============================")
    selection = star_input("> ")
    return selection


def print_ascii_art(ascii_arr):
    for line in ascii_arr:
        sleep(0.25)
        print(line)
