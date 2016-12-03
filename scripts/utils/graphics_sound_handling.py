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
        :param name:
        :return:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(name, True)

        self.true_position_x = self.rect.x
        self.true_position_y = self.rect.y


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
        :return:
        """

        import storage as st

        events = st.Events.pygame
        mouse_hover = False
        mouse_button_down = False
        mouse_button_up = False

        # MOUSE STATE

        #    is mouse over sprite ?
        if self.rect.collidepoint(st.Input.mouse_pos):
            mouse_hover = True
        else:
            mouse_hover = False

        #    is mouse button is down ?
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_button_down = True
            else:
                mouse_button_down = False

        #    is mouse button is up ?
        for event in st.Events.pygame:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_button_up = True
            else:
                mouse_button_up = False

        #    If mouse is on sprite and button is pressed up
        if mouse_button_up is True and mouse_hover is True:
            self.last_pressed = True
        else:
            self.last_pressed = False

        # BUTTON ANIMATION GRAPHICS

        # if there is pressed and hover image
        if self.type == 'hover,press':
            if self.rect.collidepoint(st.Input.mouse_pos):
                if st.Input.mouse_pressed_buttons[0]:
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
            if self.rect.collidepoint(st.Input.mouse_pos):
                for event in events:
                    # pressed
                    if event == 'lmb_down':
                        self.image = self.image_pressed
                    # not pressed
                    else:
                        self.image = self.image_no_hover

        # if there is hover but there isn't pressed
        elif self.type == 'hover':
            if self.rect.collidepoint(st.Input.mouse_pos):
                self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
