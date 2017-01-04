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


class CreateSprite(pygame.sprite.Sprite):
    def __init__(self, name, button=None, event=None):

        """
        Creates CreateSprite from name of image in program folder.
        :param name: name of the file without path eg. nice_picture.png
        :param hover: gives button ability to have mouse hover image.
        Picture needs to be in same folder as param name and name needs to be finished with _hover
        eg. nice_picture_hover.png
        :param pressed: Same as above but with _pressed eg. nice_picture_pressed.png
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(name, True)
        self.visible = True
        self.input_control = False

        self.name = name
        self.buttonEvent = 'EVENT:BUTTON:'+name

        # images
        self.image_no_hover = self.image
        self.image_hover = None
        self.image_press = None

        # button type
        self.type = 'normal sprite'
        self.hover = False
        self.press = False

        # State in response to input
        self.last_press = False

        if button is True:
            import storage as st
            name_path = st.Files.files.find_path(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)

            for image_name in st.Files.files.file_list:
                if image_name[0] == file_name+"_hover"+file_ending:
                    self.image_hover = load_image(file_name+"_hover"+file_ending)
                    self.hover = True

                elif image_name[0] == file_name+"_press"+file_ending:
                    self.image_pressed = load_image(file_name+"_press"+file_ending)
                    self.press = True

        # check for hover and pressed images
        if self.hover is True and self.press is True:
            self.type = 'hover,press'
        elif self.press is True and self.hover is not True:
            self.type = 'press'
        elif self.hover is True and self.press is not True:
            self.type = 'hover'

    def update(self):

        if self.type != 'normal sprite':
            self.get_state()
        if self.press is True:
            self.click()

    def get_state(self):
        """
        Compare button with mouse position and state of its buttons to generate various
        states. Like hovering over button, pressing button etc.
        Upon those states graphic of button changes
        """

        import storage as st

        events = st.Events.pygame

        ### print st.Input.LMBUp

        # is mouse over button ?
        if self.rect.collidepoint(st.Input.mousePos):
            mouse_hover = True
        else:
            mouse_hover = False

        # did user click button ?
        if st.Input.LMBUp is True and mouse_hover is True:
            self.press = True
        else:
            self.press = False

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
        # if there is hover but it isn't pressed
        elif self.type == 'press':
            if mouse_hover is True:
                for event in events:
                    # pressed
                    if event == 'lmb_down':
                        self.image = self.image_pressed
                    # not pressed
                    else:
                        self.image = self.image_no_hover

        # if there is hover but it isn't pressed
        elif self.type == 'hover':
            if mouse_hover is True:
                self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover

    def click(self):
        import storage as st
        st.Events.ui.append('EVENT:BUTTON:'+self.name)
        print self.type




