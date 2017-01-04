__author__ = 'Perkel'

import storage as st


def render_gameplay():
    pass


def render_ui():
    from storage import UInterface
    for spritegroup in UInterface.listCompleteRendering:
        spritegroup.draw(st.Display.screen)


def render_clear():
    from storage import UInterface
    for spritegroup in UInterface.listCompleteRendering:
        spritegroup.empty()


def update_state():
    from storage import UInterface
    for spritegroup in UInterface.listCompleteRendering:
        for sprite in spritegroup:
            sprite.update()