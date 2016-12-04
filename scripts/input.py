__author__ = 'Perkel'


import pygame as pg


def mouse_input():
    import storage as st
    st.Input.mousePressedButtons = pg.mouse.get_pressed()
    st.Input.mousePos = pg.mouse.get_pos()

    # LMB state
    hits = 0
    for event in st.Events.pygame:
        if event == pg.MOUSEBUTTONDOWN and event.button == 1:
            st.Input.LMBDown = True
            st.Input.LMBUp = False
            hits += 1
        elif event == pg.MOUSEBUTTONUP and event.button == 1:
            st.Input.LNBUp = True
            st.Input.LMBDown = False
            hits += 1

    if hits == 0:
        st.Input.LMBDown = False
        st.Input.LMBUp = False

    #RMB state
    hits = 0
    for event in st.Events.pygame:
        if event == pg.MOUSEBUTTONDOWN and event.button == 2:
            st.Input.RMBDown = True
            st.Input.RMBUp = False
            hits += 1
        elif event == pg.MOUSEBUTTONUP and event.button == 2:
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


def pad_input():
    pass

