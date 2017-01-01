__author__ = 'Perkel'


class System:
    debug = bool
    isGameStillRunning = bool
    newGameStarted = bool
    clock = None
    dt = float
    dtSeconds = float
    fps = float
    fpsPosition = tuple
    currentTime = None


class Files:
    import scripts.utils.data_file_handling as f
    files = f.FileList()


class Display:
    resolution = tuple
    framerate = int
    screen = object
    fullscreen = bool
    fullscreenSwitch = bool


class Events:
    game = []
    system = list
    pygame = list


class Input:
    # ALL CURRENT INPUT
    allInput = list
    # MOUSE
    mousePos = tuple
    mousePressedButtons = list
    mouseMovement = tuple

    LMBUp = bool
    LMBDown = bool

    RMBUp = bool
    RMBDown = bool

    MMBUp = bool
    MMBDown = bool

    # KEYBOARD
    keysPressed = list
    # JOYSTICK


class UInterface:
    from scripts.user_interface import UIMainMenu

    # UI STATE GLOBAL

    UIVisible = True
    UIInputControl = True

    # LAYERS

    import pygame.sprite as pgspr

    background = pgspr.Group()
    transparency = pgspr.Group()

    layer1 = pgspr.Group()
    layer2 = pgspr.Group()
    layer3 = pgspr.Group()
    layer4 = pgspr.Group()
    layer5 = pgspr.Group()

    button_layer1 = pgspr.Group()
    button_layer2 = pgspr.Group()
    button_layer3 = pgspr.Group()
    button_layer4 = pgspr.Group()

    other_layer1 = pgspr.Group()
    other_layer2 = pgspr.Group()
    other_layer3 = pgspr.Group()

    # LAYER LISTS

    list_background = (
        background,
        transparency)

    list_layers = (
        layer1,
        layer2,
        layer3,
        layer4,
        layer5)

    list_buttons = (
        button_layer1,
        button_layer2,
        button_layer3,
        button_layer4)

    list_other = (
        other_layer1,
        other_layer2,
        other_layer3)

    listCompleteRendering = []

    for x in list_background:
        listCompleteRendering.append(x)
    for x in list_layers:
        listCompleteRendering.append(x)
    for x in list_buttons:
        listCompleteRendering.append(x)
    for x in list_other:
        listCompleteRendering.append(x)

class UIGameplay():
    pass