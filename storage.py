__author__ = 'Perkel'


class System:
    debug = bool
    isGameStillRunning = bool
    newGameStarted = bool
    clock = None
    dt = float
    dtSeconds = float
    fps = float


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


class UInteface:
    UIMainMenu = object
    UIGameplay = object
    UICharacterCreation = object
    UIInventory = object