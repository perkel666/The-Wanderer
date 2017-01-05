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


def handle_ui_events():
    import storage as st
    import scripts.ui.ui_objects as ui
    for event in st.Events.ui:

        # MAIN MENU

        if event == 'EVENT:BUTTON:NEWGAME':
            ui.MainMenu.visible = False
            ui.MainMenu.inputControl = False
            ui.CharacterCreation.visible = True
            ui.CharacterCreation.inputControl = True
        if event == 'EVENT:BUTTON:OPTIONS':
            ui.MainMenu.visible = False
            ui.MainMenu.inputControl = False
            ui.Options.visible = True
            ui.Options.inputControl = True
        if event == 'EVENT:BUTTON:SAVE':
            pass
        if event == 'EVENT:BUTTON:LOAD':
            pass
        if event == 'EVENT:BUTTON:QUIT':
            st.System.isGameStillRunning = False

        # MAIN MENU - OPTIONS

        if event == 'EVENT:BUTTON:OMBACK':
            ui.MainMenu.visible = True
            ui.MainMenu.inputControl = True
            ui.Options.visible = False
            ui.Options.inputControl = False

        # CHARACTER CREATION

        if event == 'EVENT:BUTTON:CCFINISH':
            pass
        if event == 'EVENT:BUTTON:CCBACK':
            ui.CharacterCreation.visible = False
            ui.CharacterCreation.inputControl = False
            ui.MainMenu.visible = True
            ui.MainMenu.inputControl = True

