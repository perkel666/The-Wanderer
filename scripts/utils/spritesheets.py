from __future__ import division
__author__ = 'Perkel'

from scripts.utils.graphics_sound_handling import load_image
from scripts.utils.graphics_sound_handling import Button
import pygame


def sprite_sheet(name, nr_of_frames):
    """
    :param name: Takes spritesheet name without whole path just spritesheet.jpg
    :param nr_of_frames: how many strips sprite has
    :return: list of sprites from spritesheet
    """
    image = load_image(name)
    strips = []
    count = 0

    while count < nr_of_frames:
        sprite = pygame.Surface((32, 32))
        sprite.blit(image, (0, 0), (count*32, 0, 32, 32))
        sprite.convert_alpha()
        sprite.get_rect()
        strips.append(sprite)
        count += 1
    return strips


def sprite_animation(spritesheet, seconds):
    import storage as st
    time_future = st.System.currentTime + seconds
    nr_frames = seconds / len(spritesheet)
    pass


class SpriteAnim():
    def __init__(self, sprite_list,  seconds):
        self.timeDuration = seconds
        self.timeStartOfAnim = None
        self.timeCurrentTime = None
        self.timeCurrentAnimTime = 0
        self.timeEndOfAnim = None
        self.listOfFrames = []
        self.animationStarted = False
        self.animationLoop = True
        self.sprite_list = sprite_list
        self.image = self.sprite_list[0]
        self.animShowOffset = self.timeDuration / len(sprite_list)
        self.lastFrameTime = None

    def anim_update(self):
        import time
        self.timeCurrentTime = time.time()
        SpriteAnim.anim_start(self)
        if self.animationStarted is True:
            for x in self.listOfFrames:
                if x[1] > self.timeCurrentTime:
                    self.lastFrameTime = x[1]
                    self.image = x[0]
                    break
            if self.timeEndOfAnim < self.timeCurrentTime:
                self.animationStarted = False

    def anim_start(self):
        import time
        if self.animationLoop is True:
            if self.animationStarted is False:
                self.timeCurrentTime = time.time()
                self.timeStartOfAnim = self.timeCurrentTime
                self.timeEndOfAnim = self.timeCurrentTime + self.timeDuration
                self.animationStarted = True
                self.lastFrameTime = self.timeStartOfAnim

                count = 1
                for sprite in self.sprite_list:
                    self.listOfFrames.append(
                        [sprite, self.timeStartOfAnim+count*self.animShowOffset])
                    count += 1

    def anim_reset(self):
        pass


