__author__ = 'Perkel'


import pygame as pg


def mouse_input():
    import storage as st
    st.Input.mousePressedButtons = pg.mouse.get_pressed()
    st.Input.mousePos = pg.mouse.get_pos()

    # LMB state
    hits = 0
    for event in st.Events.pygame:
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            st.Input.LMBDown = True
            st.Input.LMBUp = False
            hits += 1
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            st.Input.LMBUp = True
            st.Input.LMBDown = False
            hits += 1

    if hits == 0:
        st.Input.LMBDown = False
        st.Input.LMBUp = False

    #RMB state
    hits = 0
    for event in st.Events.pygame:
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
            st.Input.RMBDown = True
            st.Input.RMBUp = False
            hits += 1
        elif event.type == pg.MOUSEBUTTONUP and event.button == 2:
            st.Input.RMBUp = True
            st.Input.RMBDown = False
            hits += 1

    if hits == 0:
        st.Input.RMBDown = False
        st.Input.RMBUp = False


def keyboard_input():
    import storage as st
    st.Input.keysPressed = pg.key.get_pressed()
    st.Input.allInput = []


def keyboard_str_input():
    import storage as st
    import string

    if st.Input.keyboard_input is True:
        events = st.Events.pygame
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    st.Input.input_text = st.Input.input_text[:-1]
                    print st.Input.input_text
                elif event.key == pg.K_RETURN:
                    st.Input.keyboard_input = False
                elif event.key == pg.K_SPACE:
                    st.Input.input_text += ' '
                    print st.Input.input_text
                elif event.key == pg.K_DELETE:
                    st.Input.input_text = st.Input.input_text[1:]
                    print st.Input.input_text
                elif event.key <= 127:
                    st.Input.input_text += str(chr(event.key))
                    print st.Input.input_text



def pad_input():
    pass

