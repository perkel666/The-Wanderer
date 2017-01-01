__author__ = 'Perkel'

import pygame as pg

# CREATING EVENTS


def keyboard_system_events():
    """
    This creates events from keyboard input
    """
    import storage as st

    if st.Input.keysPressed[pg.K_LALT] and st.Input.keysPressed[pg.K_F4]:
        st.Events.system.append('QUIT')
    if st.Input.keysPressed[pg.K_LALT] and st.Input.keysPressed[pg.K_RETURN]:
        if st.Display.fullscreen is True:
            st.Events.system.append('DISPLAY:WINDOWED')
        else:
            st.Events.system.append('DISPLAY:FULLSCREEN')
    if st.Input.keysPressed[pg.K_ESCAPE]:
        st.Events.system.append('ESCAPE')


def system_events():
    import storage as st
    for event in st.Events.pygame:
        if event.type == pg.QUIT:
            st.Events.system.append('QUIT')

# EVENTS HANDLING


def handle_system_events():
    """
    This handles system events like Quit game and other.
    :return:
    """
    import storage as st
    for event in st.Events.system:
        if event == 'QUIT':
            st.System.isGameStillRunning = False
        if event == 'DISPLAY:FULLSCREEN':
            st.Display.fullscreen = True
        if event == 'DISPLAY:WINDOWED':
            st.Display.fullscreen = False
        if event == 'PRINT:FILELIST':
            st.Files.files.print_file_list()

    # DISPLAY FULL-SCREEN SWITCH
    if st.Display.fullscreenSwitch != st.Display.fullscreen:
        if st.Display.fullscreen is True:
            pg.display.set_mode(st.Display.resolution, pg.FULLSCREEN)
            st.Display.fullscreenSwitch = st.Display.fullscreen
        else:
            pg.display.set_mode(st.Display.resolution)
            st.Display.fullscreenSwitch = st.Display.fullscreen

    st.Events.system = []