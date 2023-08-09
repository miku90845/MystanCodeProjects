"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    n_l = 1
    n = 1
    m = 1
    while n_l <= NUM_LIVES and graphics.sc != graphics.ro*graphics.co:
        graphics.ball.move(n*graphics.set_dx(), m*graphics.set_dy())
        graphics.hit_box()
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width > 0:
            n = -n
        if graphics.ball.y <= 0:
            m = -m
        if graphics.ball.y >= graphics.window.height-graphics.ball.height > 0:
            graphics.reset_ball()
            n_l += 1
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
