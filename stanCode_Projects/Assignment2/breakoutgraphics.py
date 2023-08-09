"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.sc = 0
        self.ro = brick_rows
        self.co = brick_cols
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.br = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                bri = 'purple'
                if j+1 <= brick_cols/5:
                    bri = 'red'
                elif j+1 <= 2*brick_cols/5:
                    bri = 'orange'
                elif j+1 <= 3*brick_cols/5:
                    bri = 'yellow'
                elif j+1 <= 4*brick_cols/5:
                    bri = 'green'
                elif j+1 <= 5*brick_cols/5:
                    bri = 'blue'
                self.brick.fill_color = bri
                self.window.add(self.brick, x=0+(brick_width+brick_spacing)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)

        # Initialize our mouse listeners
        onmousemoved(self.x_tracker)
        onmouseclicked(self.speed_locker)

    def x_tracker(self, axis):
        self.paddle.x = axis.x-self.paddle.width/2
        if axis.x < self.paddle.width/2:
            self.paddle.x = 0
        if axis.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width

    def speed_locker(self, click_point):
        if self.__dx == self.__dy == 0:
            self.launcher()

    def launcher(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def set_dx(self):
        return self.__dx

    def set_dy(self):
        return self.__dy

    def hit_box(self):
        bup = self.window.get_object_at(self.ball.x + self.br, self.ball.y)
        bdo = self.window.get_object_at(self.ball.x + self.br, self.ball.y + 2 * self.br)
        ble = self.window.get_object_at(self.ball.x, self.ball.y + self.br)
        bri = self.window.get_object_at(self.ball.x + 2 * self.br, self.ball.y + self.br)
        used_obj = [self.paddle, self.ball]
        if bup not in used_obj:
            self.__dy = -self.__dy
            self.window.remove(bup)
            self.sc += 1
        elif bdo not in used_obj:
            self.__dy = -self.__dy
            self.window.remove(bdo)
            self.sc += 1
        elif ble not in used_obj:
            self.__dx = -self.__dx
            self.window.remove(ble)
            self.sc += 1
        elif bri not in used_obj:
            self.__dx = -self.__dx
            self.window.remove(bri)
            self.sc += 1
        if self.ball.y + self.ball.height >= self.paddle.y and self.__dy > 0:
            if self.ball.x + self.ball.width >= self.paddle.x and self.ball.x <= self.paddle.x + self.paddle.width:
                self.__dy = -self.__dy

    def reset_ball(self):
        self.ball.x = self.window.width/2-self.br
        self.ball.y = self.window.height/2-self.br
        self.__dx = 0
        self.__dy = 0
