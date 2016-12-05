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

        # TEST ||||||||||||||||||||||||||||||||||||||||||||||||||

        self.surfacebcg = pg.Surface((1280, 720))
        self.surfacebcg.fill((200, 200, 200))
        self.surfacebcg.get_rect()

        import scripts.utils.graphics_sound_handling as gsh
        import scripts.utils.spritesheets as spr

        self.spritesheet = spr.sprite_sheet('spritesheet.jpg', 5)
        self.animatedSprite = spr.SpriteAnim(self.spritesheet, 3)

        self.image = gsh.Button('background.jpg')
        self.image2 = Game.ButtonsQuit('pc_left_arrow.png')

        self.sprites_bcg = pg.sprite.Group()
        self.sprites_for = pg.sprite.Group()
        self.sprites_bcg.add(self.image)
        self.sprites_for.add(self.image2)

        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||

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
        ev.keyboard_system_events()
        ev.system_events()

        self.image2.get_state()
        self.animatedSprite.anim_update()

    def render_sound(self):
        pass

    def render_screen(self):
        import scripts.utils.text_handling as tx
        import storage as st

        # TEST ||||||||||||||||||||||||||||||||||||||||||||||||
        self.sprites_bcg.draw(st.Display.screen)
        self.sprites_for.draw(st.Display.screen)

        #tx.text(st.Input.mousePos)
        tx.text(st.System.fps, st.System.fpsPosition, 50)
        st.Display.screen.blit(self.surfacebcg, (0, 0))
        st.Display.screen.blit(self.spritesheet[0], (200, 200))
        st.Display.screen.blit(self.animatedSprite.image, (300, 300))
        # TEST ||||||||||||||||||||||||||||||||||||||||||||||||
        pg.display.update()

    def execute_state(self):
        import scripts.events as ev
        ev.handle_system_events()
        self.image2.do_action()

    import scripts.utils.graphics_sound_handling as gsh

    class ButtonsQuit(gsh.Button):
        def __init__(self, name):
            super(Game.ButtonsQuit, self).__init__(name, hover=True, pressed=True)
            self.description = "Quit"
            self.order = 6

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

if __name__ == "__main__":
    game = Game()
    game.main_loop()