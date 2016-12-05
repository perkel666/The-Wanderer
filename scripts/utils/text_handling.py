__author__ = 'Perkel'

import pygame as pg

# colors
red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)
white   = (255, 255, 255)
black   = (0, 0, 0)


def text(string, position, size):
    import storage as st
    font = pg.font.Font(None, size)
    scoretext = font.render(str(string), 1, white)
    st.Display.screen.blit(scoretext, position)