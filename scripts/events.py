__author__ = 'Perkel'

import pygame as pg
from pygame.locals import *

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
        if event == 'EVENT:BUTTON:OMGAME':
            pass
        if event == 'EVENT:BUTTON:OMDISPLAY':
            pass
        if event == 'EVENT:BUTTON:OMSOUND':
            pass
        if event == 'EVENT:BUTTON:OMBACK':
            ui.MainMenu.visible = True
            ui.MainMenu.inputControl = True
            ui.Options.visible = False
            ui.Options.inputControl = False

        # CHARACTER CREATION

        if event == 'EVENT:BUTTON:CCFINISH':
            ui.CharacterCreation.visible = False
            ui.CharacterCreation.inputControl = False
            ui.Gameplay.visible = True
            ui.Gameplay.inputControl = True
        if event == 'EVENT:BUTTON:CCBACK':
            ui.CharacterCreation.visible = False
            ui.CharacterCreation.inputControl = False
            ui.MainMenu.visible = True
            ui.MainMenu.inputControl = True

        if event == 'EVENT:BUTTON:CCNEXTFACE':
            import scripts.ui.ui_objects as ui
            import scripts.utils.graphics_sound_handling as gsh

            if ui.CharacterCreation.currentFaceCount < ui.CharacterCreation.numberOfFaces-1:
                ui.CharacterCreation.currentFace = gsh.CreateSprite(ui.CharacterCreation.list_faces[
                    ui.CharacterCreation.currentFaceCount+1])
                ui.CharacterCreation.currentFaceCount += 1
            else:
                ui.CharacterCreation.currentFace = gsh.CreateSprite(ui.CharacterCreation.list_faces[0])
                ui.CharacterCreation.currentFaceCount = 0
            print 'next face'
        if event == 'EVENT:BUTTON:CCPREVIOUSFACE':
            import scripts.ui.ui_objects as ui
            import scripts.utils.graphics_sound_handling as gsh

            if ui.CharacterCreation.currentFaceCount > 0:
                ui.CharacterCreation.currentFace = gsh.CreateSprite(ui.CharacterCreation.list_faces[
                    ui.CharacterCreation.currentFaceCount-1])
                ui.CharacterCreation.currentFaceCount -= 1
            else:
                ui.CharacterCreation.currentFace = gsh.CreateSprite(ui.CharacterCreation.list_faces[
                    ui.CharacterCreation.numberOfFaces-1])
                ui.CharacterCreation.currentFaceCount = ui.CharacterCreation.numberOfFaces-1
            print 'previous face'
        if event == 'EVENT:BUTTON:CCNEXTFACEBACKGROUND':
            import scripts.ui.ui_objects as ui
            import scripts.utils.graphics_sound_handling as gsh

            if ui.CharacterCreation.currentFaceBackgroundCount < ui.CharacterCreation.numberOfFaceBackground-1:
                ui.CharacterCreation.currentFaceBackground = gsh.CreateSprite(ui.CharacterCreation.list_background[
                    ui.CharacterCreation.currentFaceBackgroundCount+1])
                ui.CharacterCreation.currentFaceBackgroundCount += 1
            else:
                ui.CharacterCreation.currentFaceBackground = gsh.CreateSprite(ui.CharacterCreation.list_background[0])
                ui.CharacterCreation.currentFaceBackgroundCount = 0
            print 'next face background'

        if event == 'EVENT:BUTTON:CCPREVIOUSFACEBACKGROUND':
            import scripts.ui.ui_objects as ui
            import scripts.utils.graphics_sound_handling as gsh

            if ui.CharacterCreation.currentFaceBackgroundCount > 0:
                ui.CharacterCreation.currentFaceBackground = gsh.CreateSprite(ui.CharacterCreation.list_background[
                    ui.CharacterCreation.currentFaceBackgroundCount-1])
                ui.CharacterCreation.currentFaceBackgroundCount -= 1
            else:
                ui.CharacterCreation.currentFaceBackground = gsh.CreateSprite(ui.CharacterCreation.list_background[
                    ui.CharacterCreation.numberOfFaceBackground-1])
                ui.CharacterCreation.currentFaceBackgroundCount = ui.CharacterCreation.numberOfFaceBackground-1
            print 'previous face background'
        # GAMEPLAY OPTIONS

        if event == 'EVENT:BUTTON:OGGAME':
            pass
        if event == 'EVENT:BUTTON:OGDISPLAY':
            pass
        if event == 'EVENT:BUTTON:OGSOUND':
            pass
        if event == 'EVENT:BUTTON:OGBACK':
            ui.Gameplay.visible = True
            ui.Gameplay.inputControl = True
            ui.GameplayOptions.visible = False
            ui.GameplayOptions.inputControl = False

        # GAMEPLAY UI

        if event == 'EVENT:BUTTON:GPTQUIT':
            ui.MainMenu.visible = True
            ui.MainMenu.inputControl = True
            ui.Gameplay.visible = False
            ui.Gameplay.inputControl = False
        if event == 'EVENT:BUTTON:GMTOPTIONS':
            ui.Gameplay.visible = False
            ui.Gameplay.inputControl = False
            ui.GameplayOptions.visible = True
            ui.GameplayOptions.inputControl = True

