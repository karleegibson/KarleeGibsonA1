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

MENU = "Menu: \nR - List required items \nC - List completed items \nA - Add new item \nM - Mark an item as " \
       "completed \nQ - Quit"
COFFEE_BEANS = 40.00
FISH_FINGERS = 12.95
METAL_DETECTOR = 42.50


def main():
    print("Shopping List 1.0 - by Karlee Gibson")
    list_of_items = load_items()
    print("{} items loaded from items.csv".format(len(list_of_items)))
    menu = choose_menu_option()
    while menu != "Q":
        if menu == "R":
            print("Required items: ")
            required_items = load_items()
            count = 0
            for item in required_items:
                print("{}. {}".format(count, item))
                count += 1
        menu = choose_menu_option()
        if menu == "C":
            completed_items = load_completed_items(list_of_items)
            if completed_items == "0":
                print("No completed items")
            else:
                print(completed_items)
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


def load_items():
    items_file = open('items.csv', 'r')
    items_in_text = items_file.readlines()
    items = []
    for item in items_in_text:
        item = item.strip().split(',')
        item[1] = float(item[1])
        item[2] = int(item[2])
        items.append(item)
    return items


def load_completed_items(list_of_items):
    completed_items_list = []
    for item in list_of_items:
        if "c" in item:
            completed_items_list.append(item)
        else:
            completed_items_list = ["0"]
    return completed_items_list


# def calculate_expected_price():

def add_new_item():
    try:
        item_name = input("Item name: ")
        item_price = float(input("Price: "))
        item_priority = int(input("Priority: "))
        required_items.append(item_name, item_price, item_priority)
    except NameError:
        print("Input can not be blank")



# def complete_an_item():


main()
