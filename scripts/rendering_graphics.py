__author__ = 'Perkel'

import storage as st


def render_gameplay():
    pass


def render_ui():
    from storage import UInterface
    for spritegroup in UInterface.listCompleteRendering:
        spritegroup.draw(st.Display.screen)