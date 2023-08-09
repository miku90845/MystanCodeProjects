"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

w = GWindow(title='draw_line')
n = 1
SIZE = 9
frx = None
fry = None
cir = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(buildline)


def buildline(axis):
    """
    次數等於一就畫圈，畫完後次數加一，次數等於二就畫線，畫完後次數減一
    """
    global n, frx, fry
    if n == 1:
        w.add(cir, axis.x - SIZE / 2, axis.y - SIZE / 2)
        frx = axis.x
        fry = axis.y
        n += 1
    elif n == 2:
        w.remove(cir)
        lin = GLine(frx, fry, axis.x, axis.y)
        w.add(lin)
        n -= 1


if __name__ == "__main__":
    main()
