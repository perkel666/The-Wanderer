__author__ = 'perkel666'

import os
import pygame


def load_image(name, rect=None):
    import storage as st
    file_path = st.Files.files.find_path(name)

    if rect is not None:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image, image.get_rect()

    else:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image


def text(string):
    import storage as st
    font = pygame.font.Font(None, 50)
    scoretext = font.render(str(string), 1, (255, 255, 255))
    st.Display.screen.blit(scoretext, (500, 457))


class CreateSprite(pygame.sprite.Sprite):
    def __init__(self, name):
        """
        Creates Sprite from image and gives it size according to image size
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(name, True)


class Button(CreateSprite):
    def __init__(self, name, hover=None, pressed=None):

        """
        Creates Button from sprite (which has already size information and image)
        :param name: name of the file without path eg. nice_picture.png
        :param hover: gives button ability to have mouse hover image.
        Picture needs to be in same folder as param name and name needs to be finished with _hover
        eg. nice_picture_hover.png
        :param pressed: Same as above but with _pressed eg. nice_picture_pressed.png
        """
        super(Button, self).__init__(name)
        self.visible = True
        self.input_control = False
        # images
        self.image_no_hover = self.image
        self.image_hover = None
        self.image_pressed = None
        # button type
        self.type = 'normal'
        self.pressed = None
        # State in response to input
        self.last_pressed = False

        # check for hover and pressed images
        if hover is True:
            import storage as st
            name_path = st.Files.files.find_path(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_hover = load_image(file_name+"_hover"+file_ending)
        if pressed is True:
            import storage as st
            name_path = st.Files.files.find_path(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_pressed = load_image(file_name+"_pressed"+file_ending)

        if hover is True and pressed is True:
            self.type = 'hover,press'
        elif pressed is True and hover is not True:
            self.type = 'press'
        elif hover is True and pressed is not True:
            self.type = 'hover'

    def get_state(self):
        """
        Compare button with mouse position and state of its buttons to generate various
        states. Like hovering over button, pressing button etc.
        Upon those states graphic of button changes
        """

        import storage as st

        events = st.Events.pygame

        # is mouse over button ?
        if self.rect.collidepoint(st.Input.mousePos):
            mouse_hover = True
        else:
            mouse_hover = False

        # did user click button ?
        if st.Input.LMBUp is True and mouse_hover is True:
            self.last_pressed = True
        else:
            self.last_pressed = False

        # if there is pressed and hover image
        if self.type == 'hover,press':
            if mouse_hover is True:
                if st.Input.mousePressedButtons[0]:
                    # pressed
                    self.image = self.image_pressed
                else:
                    # not pressed
                    self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
                else:
                    pass
        # if there is hover but there isn't pressed
        elif self.type == 'press':
            if mouse_hover is True:
                for event in events:
                    # pressed
                    if event == 'lmb_down':
                        self.image = self.image_pressed
                    # not pressed
                    else:
                        self.image = self.image_no_hover

        # if there is hover but there isn't pressed
        elif self.type == 'hover':
            if mouse_hover is True:
                self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
