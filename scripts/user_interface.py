__author__ = 'Perkel'

import pygame as pg
from scripts.utils.graphics_sound_handling import Button


class UIMainMenu():
    def __init__(self):
        self.visible = True
        self.inputControl = True

        self.background = Button('ui_background_mm.jpg')

    def update(self):
        self.position_ui()

    def position_ui(self):
        from storage import UInterface
        UInterface.background.empty()
        UInterface.background.add(self.background)

    def execute_actions(self):
        pass
