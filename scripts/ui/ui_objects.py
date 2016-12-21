__author__ = 'Perkel'

from scripts.user_interface import UIMainMenu

# Main User Interface

MainMenu = UIMainMenu()
Options = object
Save = object
Load = object
CharacterCreation = object
Inventory = object
Gameplay = object

uiList = [
    MainMenu
]


def update_ui():
    for x in uiList:
        x.update()