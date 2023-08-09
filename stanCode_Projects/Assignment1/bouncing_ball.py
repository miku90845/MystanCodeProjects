"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 9
DELAY = 30
GRAVITY = 3
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
vector = VX
n = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(lock)


def lock(axis):
    """
    只有再次數小於3以及小球回到起始位置時，才會讓小球可以落下
    """
    global n, START_X
    if n <= 2 and START_X == 30:
        n += 1
        falling()


def falling():
    """
    小球落下，並在撞牆後重製變動值
    """
    global GRAVITY, vector, START_X, START_Y
    while True:
        vector += GRAVITY
        START_X += VX
        START_Y += vector
        ball.move(VX, vector)
        pause(DELAY)
        if START_Y + SIZE >= 500 and vector >= 0:
            vector *= 0.9
            vector = -vector
        elif START_X + SIZE >= 800:
            vector = VX
            START_X = 30
            START_Y = 40
            main()
            break


if __name__ == "__main__":
    main()
