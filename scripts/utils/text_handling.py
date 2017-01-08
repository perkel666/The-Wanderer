__author__ = 'Perkel'

import pygame as pg
import string

from pygame.locals import *

# colors
red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)
white   = (255, 255, 255)
black   = (0, 0, 0)


def text(text_to_display, position, size):
    import storage as st
    font = pg.font.Font(None, size)
    scoretext = font.render(str(text_to_display), 1, green)
    st.Display.screen.blit(scoretext, position)


text_to_print = "Luis had a good time last year at Olimpics. He was proud of our boys delivering fantastic performance."


def text2(text_to_display, sprite, size):
    import storage as st
    font = pg.font.Font(None, size)

    new_line = ''
    line = []
    lines_to_print = []
    text_list = text_to_display.split()
    text_width, text_height = font.size(new_line)

    for word in text_list:
        temp_width, temp_height = font.size(' '+word)
        if text_width+temp_width <= sprite.rect.width-size/2:
            if word == text_list[0]:
                new_line = word
            elif word == text_list[-1]:
                new_line = new_line+' '+word
                lines_to_print.append(new_line)
            else:
                new_line = new_line+' '+word

        else:
            lines_to_print.append(new_line)
            new_line = word

        text_width, text_height = font.size(new_line)

    #print '============='
    #for x in lines_to_print:
    #    print x
    #print '============='
    print text_list
    count = 0
    for line in lines_to_print:
        final_text = font.render(str(line), 1, green)
        st.Display.screen.blit(final_text, (sprite.rect.left+size/2, sprite.rect.top+size+count*size-size/2))
        count += 1

def things_to_print(list_of_things_to_print):

    for tuple_text in list_of_things_to_print:
        text2(tuple_text[0], tuple_text[1], tuple_text[2])
