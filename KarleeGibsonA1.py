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
    print(MENU)

main()
