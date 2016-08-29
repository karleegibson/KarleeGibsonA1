""" Name: Karlee Gibson
    Date: 28/08/16
    Brief program details: Shopping List 1.0
    Link to GitHub:

Pseudocode:
function load_items()
    display required_items_list
    display menu choice
    get menu choice


function complete_an_item()
    display required_items_list
    get number of item to mark
    display item marked as completed message




"""
import csv

items_file = open('items.csv', 'r')

MENU = "Menu: \nR - List required items \nC - List completed items \nA - Add new item \nM - Mark an item as " \
       "completed \nQ - Quit"


def main():
    print("Shopping List 1.0 - by Karlee Gibson")
    lines = items_file.readlines()
    print("{} items loaded from items.csv".format(len(lines)))
    menu = choose_menu_option()
    while menu != "Q":
        if menu == "R":
            items_reader = csv.reader(items_file)
            for row in items_reader:
                print(row)
        menu = choose_menu_option()


def choose_menu_option():
    print(MENU)
    try:
        menu_choice = input(">>>").upper()
        while menu_choice not in ['R', 'C', 'A', 'M', 'Q']:
            print("Invalid menu choice")
            print(MENU)
            menu_choice = input(">>>").upper()
        return menu_choice
    except ValueError:
        print("Invalid menu choice")
        print(MENU)


# def list_required_items():



main()
