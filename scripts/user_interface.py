__author__ = 'Perkel'

import pygame as pg
from scripts.utils.graphics_sound_handling import CreateSprite


class UIMainMenu():
    def __init__(self):
        self.visible = True
        self.inputControl = True

        self.difference = 120

        self.background = CreateSprite('ui_background_mm.jpg', 'mm_background')
        self.uiBackground = CreateSprite('ui_background.jpg', 'mm_ui_background')

        self.buttonNewGame = CreateSprite('mm_button_newgame.jpg', 'NEWGAME')
        self.buttonOptions = CreateSprite('mm_button_options.jpg', 'OPTIONS')
        self.buttonQuit = CreateSprite('mm_button_quit.jpg', 'QUIT')

        self.buttonList =[
            self.buttonNewGame,
            self.buttonOptions,
            self.buttonQuit
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()
        self.execute_actions()

    def position_ui(self):

        self.background.rect.x = 0
        self.background.rect.y = 0
        self.uiBackground.rect.x = 100
        self.uiBackground.rect.y = 50

        count = 0

        for button in self.buttonList:
            button.rect.x = self.uiBackground.rect.x+20
            button.rect.y = 20+self.uiBackground.rect.y+count*self.difference
            count += 1

    def add_spritestorender(self):
        from storage import UInterface
        UInterface.background.add(self.background)
        UInterface.layer1.add(self.uiBackground)

        for button in self.buttonList:
            UInterface.button_layer1.add(button)

    def execute_actions(self):
        if self.inputControl is True:
            for button in self.buttonList:
                button.click()


class UICharacterCreation():
    def __init__(self):
        self.visible = False
        self.inputControl = False

        self.background = CreateSprite('cc_background.jpg', 'cc_background')
        self.uiBackground = CreateSprite('cc_ui_background.jpg', 'cc_ui_background')

        self.faceBackground = CreateSprite('cc_face_background.jpg', 'cc_face_background')
        self.faceForeground = ''

        self.buttonNextFace = CreateSprite('cc_arrow_right.jpg', 'CCNEXTFACE')
        self.buttonPreviousFace = CreateSprite('cc_arrow_left.jpg', 'CCPREVIOUSFACE')
        self.buttonNextBackground = CreateSprite('cc_arrow_right.jpg', 'CCNEXTFACEBACKGROUND')
        self.buttonPreviousBackground = CreateSprite('cc_arrow_left.jpg', 'CCPREVIOUSFACEBACKGROUND')

        self.buttonFinish = CreateSprite('cc_button_finish.jpg', 'CCFINISH')
        self.buttonBack = CreateSprite('cc_button_back.jpg', 'CCBACK')

        self.buttonList = [
            self.buttonFinish,
            self.buttonBack,
            self.buttonNextFace,
            self.buttonPreviousFace,
            self.buttonNextBackground,
            self.buttonPreviousBackground
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()
        self.execute_actions()

    def position_ui(self):
        import storage as st

        self.uiBackground.rect.center = (st.Display.resolution[0]/2, st.Display.resolution[1]/2+30)
        self.faceBackground.rect.center = (st.Display.resolution[0]/2, st.Display.resolution[1]/2-90)

        self.buttonNextFace.rect.center = (st.Display.resolution[0]/2+140, st.Display.resolution[1]/2-160)
        self.buttonPreviousFace.rect.center = (st.Display.resolution[0]/2-140, st.Display.resolution[1]/2-160)
        self.buttonNextBackground.rect.center = (st.Display.resolution[0]/2+140, st.Display.resolution[1]/2-15)
        self.buttonPreviousBackground.rect.center = (st.Display.resolution[0]/2-140, st.Display.resolution[1]/2-15)

        self.buttonFinish.rect.center = (st.Display.resolution[0]*0.825, st.Display.resolution[1]*0.945)
        self.buttonBack.rect.center = (st.Display.resolution[0]*0.175, st.Display.resolution[1]*0.945)

    def add_spritestorender(self):
        from storage import UInterface
        UInterface.background.add(self.background)
        UInterface.layer1.add(self.uiBackground)
        UInterface.layer2.add(self.faceBackground)

        for button in self.buttonList:
            UInterface.button_layer1.add(button)

    def execute_actions(self):
        if self.inputControl is True:
            for button in self.buttonList:
                button.click()


class UIOptions():
    def __init__(self):
        self.visible = False
        self.inputControl = False

        self.difference = 120

        self.background = CreateSprite('om_background.jpg', 'om_background')
        self.uiBackground = CreateSprite('om_ui_background.jpg', 'om_ui_background')

        self.buttonGame = CreateSprite('om_button_game.jpg', 'OMGAME')
        self.buttonDisplay = CreateSprite('om_button_display.jpg', 'OMDISPLAY')
        self.buttonSound = CreateSprite('om_button_sound.jpg', 'OMSOUND')
        self.buttonBack = CreateSprite('om_button_back.jpg', 'OMBACK')

        self.buttonList = [
            self.buttonGame,
            self.buttonDisplay,
            self.buttonSound,
            self.buttonBack
        ]

        self.moButtonList = [
            self.buttonGame,
            self.buttonDisplay,
            self.buttonSound,
            self.buttonBack
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()
        self.execute_actions()

    def position_ui(self):
        import storage as st

        self.uiBackground.rect.center = (st.Display.resolution[0]*0.15, st.Display.resolution[1]*0.50)

        count = 0
        for button in self.moButtonList:
            button.rect.x = self.uiBackground.rect.x+20
            button.rect.y = 20+self.uiBackground.rect.y+count*self.difference
            count += 1

    def add_spritestorender(self):
        from storage import UInterface
        UInterface.background.add(self.background)
        UInterface.layer1.add(self.uiBackground)

        for button in self.buttonList:
            UInterface.button_layer1.add(button)

    def execute_actions(self):
        if self.inputControl is True:
            for button in self.buttonList:
                button.click()


class GameUIOptions():
    def __init__(self):
        self.visible = False
        self.inputControl = False

        self.difference = 120

        # self.background = CreateSprite('om_background.jpg', 'og_background')
        self.uiBackground = CreateSprite('om_ui_background.jpg', 'og_ui_background')

        self.buttonGame = CreateSprite('om_button_game.jpg', 'OGGAME')
        self.buttonDisplay = CreateSprite('om_button_display.jpg', 'OGDISPLAY')
        self.buttonSound = CreateSprite('om_button_sound.jpg', 'OGSOUND')
        self.buttonBack = CreateSprite('om_button_back.jpg', 'OGBACK')

        self.buttonList = [
            self.buttonGame,
            self.buttonDisplay,
            self.buttonSound,
            self.buttonBack
        ]

        self.moButtonList = [
            self.buttonGame,
            self.buttonDisplay,
            self.buttonSound,
            self.buttonBack
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()
        self.execute_actions()

    def position_ui(self):
        import storage as st

        self.uiBackground.rect.center = (st.Display.resolution[0]*0.15, st.Display.resolution[1]*0.50)

        count = 0
        for button in self.moButtonList:
            button.rect.x = self.uiBackground.rect.x+20
            button.rect.y = 20+self.uiBackground.rect.y+count*self.difference
            count += 1

    def add_spritestorender(self):
        from storage import UInterface
        #UInterface.background.add(self.background)
        UInterface.layer1.add(self.uiBackground)

        for button in self.buttonList:
            UInterface.button_layer1.add(button)

    def execute_actions(self):
        if self.inputControl is True:
            for button in self.buttonList:
                button.click()


class UIGameplay():
    def __init__(self):
        self.visible = False
        self.inputControl = False

        self.background = CreateSprite('gm_background.jpg', 'gm_background')
        self.portraitBackground = CreateSprite('gm_portrait_background.jpg', 'gm_portrait_background')
        self.toolboxBackground = CreateSprite('gm_toolbox_background.jpg', 'gm_toolbox_background')
        self.moneyBackground = CreateSprite('gm_money_background.jpg', 'gm_money_background')
        self.dayTime_background = CreateSprite('gm_day_time_background.jpg', 'gm_day_time_background')

        self.uiElBackgroundList = [
            self.portraitBackground,
            self.toolboxBackground,
            self.moneyBackground,
            self.dayTime_background
        ]

    def update(self):
        self.position_ui()
        self.add_spritestorender()
        self.execute_actions()

    def position_ui(self):
        import storage as st
        res = st.Display.resolution
        self.portraitBackground.rect.topleft = (10, 10)
        self.toolboxBackground.rect.bottomright = (st.Display.resolution[0]*0.99, st.Display.resolution[1]*0.99)
        self.moneyBackground.rect.x = self.portraitBackground.rect.right + 10
        self.moneyBackground.rect.y = self.portraitBackground.rect.top
        self.dayTime_background.rect.x = self.portraitBackground.rect.right + 10
        self.dayTime_background.rect.y = self.moneyBackground.rect.bottom + 10

    def add_spritestorender(self):
        from storage import UInterface
        UInterface.background.add(self.background)

        for ui_element in self.uiElBackgroundList:
            UInterface.layer1.add(ui_element)

    def execute_actions(self):
        if self.inputControl is True:
            for button in self.uiElBackgroundList:
                button.click()

