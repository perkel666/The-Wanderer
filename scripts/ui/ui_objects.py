__author__ = 'Perkel'

import scripts.user_interface as ui

# Main User Interface

MainMenu = ui.UIMainMenu()
Options = object
Save = object
Load = object
CharacterCreation = ui.UICharacterCreation()
Inventory = object
Gameplay = object

uiList = [
    MainMenu,
    CharacterCreation
]


def update_ui():
    for x in uiList:
        if x.visible is True:
            x.update()