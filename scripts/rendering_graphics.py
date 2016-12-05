__author__ = 'Perkel'

import pygame as pg


def render_gameplay():
    pass


def render_ui():
    from storage import UInterface

    if UInterface.MainMenu.visible is True:
        UInterface.MainMenu.draw_ui()
