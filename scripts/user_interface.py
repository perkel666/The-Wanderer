__author__ = 'Perkel'

import pygame as pg
from scripts.utils.graphics_sound_handling import Button


class UIMainMenu():
    def __init__(self):
        self.visible = True
        self.inputControl = True

        self.difference = 120

        self.background = Button('ui_background_mm.jpg')
        self.uiBackground = Button('ui_background.jpg')

        self.buttonNewGame = Button('mm_button_newgame.jpg', hover=True)
        self.buttonOptions = Button('mm_button_options.jpg', hover=True)
        self.buttonQuit = Button('mm_button_quit.jpg', hover=True)

        self.buttonList =[
            self.buttonNewGame,
            self.buttonOptions,
            self.buttonQuit
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()

    def position_ui(self):

        self.background.rect.x = 0
        self.background.rect.y = 0
        self.uiBackground.rect.x = 100
        self.uiBackground.rect.y = 50

        count = 0

        for button in self.buttonList:
            button.rect.x = self.uiBackground.rect.x+20
            button.rect.y = 20+self.uiBackground.rect.y+count*self.difference
            count += 1

    def add_spritestorender(self):
        from storage import UInterface
        UInterface.background.add(self.background)
        UInterface.layer1.add(self.uiBackground)

        for button in self.buttonList:
            UInterface.button_layer1.add(button)

    def execute_actions(self):
        pass
