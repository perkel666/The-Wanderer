from __future__ import division
__author__ = 'Perkel'

import pygame as pg


class Game(object):
    def __init__(self):
        import storage as st
        pg.init()
        # system
        st.System.debug = True
        st.System.clock = pg.time.Clock()
        st.System.isGameStillRunning = True
        st.System.newGameStarted = False
        # display
        st.Display.resolution = (1280, 720)
        st.Display.fullscreen = False
        st.Display.fullscreen_switch = st.Display.fullscreen
        st.Display.framerate = 50
        st.Display.screen = pg.display.set_mode(st.Display.resolution)
        # events
        st.Events.pygame = pg.event.get()
        st.Events.system = []

    def main_loop(self):
        import storage as st
        while st.System.isGameStillRunning is True:
            pg.display.update()
            self.start_frame()
            self.get_user_input()
            self.update_state()
            self.render_screen()
            self.render_sound()
            self.execute_state()

    def start_frame(self):
        import storage as st
        st.System.dt = st.System.clock.tick(st.Display.framerate)
        st.System.dt_seconds = st.System.dt / 1000
        st.Events.pygame = pg.event.get()
        st.Events.game = []
        st.Events.system = []

    def get_user_input(self):
        pass

    def update_state(self):
        pass

    def render_sound(self):
        pass

    def render_screen(self):
        pass

    def execute_state(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.main_loop()