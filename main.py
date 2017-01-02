from __future__ import division
__author__ = 'Perkel'

import pygame as pg
import time


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
        st.Display.fullscreenSwitch = st.Display.fullscreen
        st.Display.framerate = 50
        st.Display.screen = pg.display.set_mode(st.Display.resolution)
        st.System.fpsPosition = (st.Display.resolution[0]*0.92, st.Display.resolution[1]*0.92)
        # events
        st.Events.pygame = pg.event.get()
        st.Events.system = []
        # initialize ui
        st.UInterface()

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
        st.System.dtSeconds = st.System.dt / 1000
        st.Events.pygame = pg.event.get()
        st.Events.game = []
        st.Events.system = []
        st.System.fps = st.System.clock.get_fps()
        st.System.currentTime = time.time()

    def get_user_input(self):
        import scripts.input as u_input
        u_input.mouse_input()
        u_input.keyboard_input()

    def update_state(self):
        import scripts.events as ev
        import scripts.ui.ui_objects as ui_objects
        ev.keyboard_system_events()
        ev.system_events()
        ui_objects.update_ui()

    def render_sound(self):
        pass

    def render_screen(self):
        import scripts.rendering_graphics as rnd

        rnd.update_state()
        rnd.render_ui()
        pg.display.update()
        rnd.render_clear()

    def execute_state(self):
        import scripts.events as ev
        ev.handle_system_events()

    import scripts.utils.graphics_sound_handling as gsh

    class ButtonsQuit(gsh.CreateSprite):
        def __init__(self, name):
            super(Game.ButtonsQuit, self).__init__(name, hover=True, pressed=True)
            self.description = "Quit"
            self.order = 6

        def do_action(self):
            if self.last_press is True:
                print self.description
                self.last_press = False

if __name__ == "__main__":
    game = Game()
    game.main_loop()