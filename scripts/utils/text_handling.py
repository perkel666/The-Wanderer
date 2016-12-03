__author__ = 'Perkel'

import pygame as pg


def text(string):
    import storage as st
    font = pg.font.Font(None, 50)
    scoretext = font.render(str(string), 1, (255, 255, 255))
    st.Display.screen.blit(scoretext, (500, 457))