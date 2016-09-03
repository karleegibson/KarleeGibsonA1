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
            required_items = load_required_items(list_of_items)
            count = 0
            for item in required_items:
                print("{}. {:18} ${:6.2f} ({})".format(count, item[0], item[1], item[2]))
                count += 1
            expected_price_of_items = calculate_expected_price(required_items)
            print("Total expected price for {} items: ${}".format(len(required_items), expected_price_of_items))
            menu = choose_menu_option()

        elif menu == "C":
            completed_items = load_completed_items(list_of_items)
            if completed_items == '':
                print("No completed items")
            else:
                print(completed_items)
            menu = choose_menu_option()

        elif menu == "A":
            new_item = add_new_item(list_of_items)
            menu = choose_menu_option()

        elif menu == "M":
            print("Required items: ")
            required_items = load_required_items(list_of_items)
            count = 0
            for item in required_items:
                print("{}. {:18} ${:6.2f} ({})".format(count, item[0], item[1], item[2]))
                count += 1
            expected_price_of_items = calculate_expected_price(required_items)
            print("Total expected price for {} items: ${}".format(len(required_items), expected_price_of_items))
            item_to_be_completed =
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


def load_required_items(list_of_items):
    required_items_list = []
    for item in list_of_items:
        if item[3] == 'r':
            required_items_list.append(item)
    return required_items_list


def load_completed_items(list_of_items):
    completed_items_list = []
    for item in list_of_items:
        if item[3] == 'c':
            completed_items_list.append(item)
        else:
            completed_items_list = ''
    return completed_items_list


def calculate_expected_price(required_items):
    expected_price = 0.00
    for item in required_items:
        expected_price += item[1]
    return expected_price


def add_new_item(list_of_items):
    try:
        item_name = input("Item name: ")
        item_price = float(input("Price: "))
        item_priority = int(input("Priority: "))
        while item_priority not in [1, 2, 3]:
            print("Priority must be 1, 2 or 3")
            item_priority = int(input("Priority: "))
        completion = 'r'
        print("{}, ${} (priority {}) added to shopping list".format(item_name, item_price, item_priority))
        list_of_items.append(item_name, item_price, item_priority, completion)
        print("Invalid input; enter a valid number")
    except TypeError:
        print("Invalid input; enter a valid number")
    except "":
        print("Input can not be blank")
    return list_of_items


def complete_an_item(required_items):
    item_to_complete = (input("Enter the number of an item to mark as completed"))



main()
