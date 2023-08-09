"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE

絕對很難用的圖形介面生成器
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 4      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 90       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 70      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 120      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 10    # Initial vertical speed for the ball
MAX_X_SPEED = 1        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - 5*brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.sc = 0
        self.ofs = brick_offset
        self.bs = brick_spacing
        self.ro = brick_rows
        self.co = brick_cols
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = '#75c2c9'
        self.paddle.color = '#0e7f8a'
        # Center a filled ball in the graphical window
        self.br = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = '#0bd3e6'
        self.brick = GRect(brick_width, brick_height)
        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        # start page
        self.start_opr = 1
        self.start_bt = GRect(2*brick_width, 4*brick_height,
                              x=(window_width-2*brick_width)/2, y=window_height-8*brick_height)
        self.start_bt.fill_color = '#f2f7fa'
        self.start_bt.color = '#79b5ba'
        self.start_wr = GLabel('START')
        self.window.add(self.start_bt)
        self.window.add(self.start_wr, x=(window_width-self.start_wr.width)/2, y=window_height-7*self.start_wr.height)
        self.record_wr = GLabel('hi')
        """唯一一個檢測點按，當初多加一個就出問題了，可能是我還不太會設置開關"""
        onmouseclicked(self.click_start_bt)
        """特效"""
        self.eft1 = GOval(0, 0)
        self.eft2 = GOval(0, 0)
        self.eft3 = GOval(0, 0)
        self.eft4 = GOval(0, 0)
        """記分板"""
        self.count_board = GRect(self.window.width, 30)
        self.score = GLabel('score:', x=10, y=25)
        self.score.font = '-20'
        self.score_num = GLabel('0', x=90, y=28)
        self.score_num.font = '-18'
        """儲存分數"""
        self.scs = []
        """確認分數的圖示"""
        self.end_bar = GRect(2 * self.start_bt.width, 4 * self.start_bt.height,
                             x=(window_width - 2 * self.start_bt.width) / 2,
                             y=window_height - 4.5 * self.start_bt.height)
        self.end_bar.fill_color = '#f2f7fa'
        self.end_bar.color = '#79b5ba'
        self.end_wr = GLabel('hi')
        """儲存板子移動給的速度"""
        self.get_v = 0
        self.add_v = random.randint(1, 2)
        """技能會用到的"""
        self.laser_brick = GRect(self.brick.width, self.brick.height)
        self.laser_brick.filled = True
        self.laser_brick.fill_color = '#f59b98'
        self.laser_brick.color = '#db6763'
        self.laser_eft = GRect(10, 10)
        self.laser_eft.fill_color = '#f59b98'
        self.laser_eft.color = '#db6763'
        self.eft_opr = 0
        self.fire = 0
        self.fire_tou = 0

    def game_starter(self):
        """遊戲的圖像介面"""
        # Initialize our mouse listeners
        onmousemoved(self.x_tracker)
        # Draw bricks
        self.window.add(self.paddle)
        self.window.add(self.ball)
        self.window.add(self.count_board)
        self.window.add(self.score)
        self.window.add(self.score_num)
        for i in range(self.ro):
            for j in range(self.co):
                self.brick = GRect(self.brick.width, self.brick.height)
                self.brick.filled = True
                self.brick.color = '#79b5ba'
                bri = '#ebfdff'
                if j + 1 <= self.co / 5:
                    bri = '#75c2c9'
                elif j + 1 <= 2 * self.co / 5:
                    bri = '#8bd2d9'
                elif j + 1 <= 3 * self.co / 5:
                    bri = '#ade8ed'
                elif j + 1 <= 4 * self.co / 5:
                    bri = '#d0f2f5'
                elif j + 1 <= 5 * self.co / 5:
                    bri = '#ebfdff'
                self.brick.fill_color = bri
                self.window.add(self.brick, x=0 + (self.brick.width + self.bs) * i,
                                y=self.ofs + (self.brick.height + self.bs) * j)
        ran = random.randint(0, 9)
        this = self.window.get_object_at(x=(self.brick.width + self.bs)*ran,
                                         y=self.ofs + (self.brick.height + self.bs) * 7)
        self.window.remove(this)
        self.window.add(self.laser_brick, x=(self.brick.width + self.bs)*ran,
                        y=self.ofs + (self.brick.height + self.bs) * 7)

    def click_start_bt(self, here):
        """燒腦檢測器，檢測opr為某某數值時，提供相應的功能介面，要一直跳來跳去看opr到底變成多少了，頭很痛"""
        if self.start_opr == 2:
            if self.dy == 0:
                self.start_opr = 3
                self.launcher()
        if self.start_opr == 1:
            if here.x >= self.start_bt.x and here.y >= self.start_bt.y:
                if here.x <= self.start_bt.x+self.start_bt.width and here.y <= self.start_bt.y+self.start_bt.height:
                    self.window.remove(self.start_bt)
                    self.window.remove(self.start_wr)
                    self.start_opr = 2
                    self.score_num = GLabel('0', x=90, y=28)
                    self.game_starter()
        if self.start_opr == 5:
            if here.x >= self.start_bt.x and here.y >= self.start_bt.y:
                if here.x <= self.start_bt.x+self.start_bt.width and here.y <= self.start_bt.y+self.start_bt.height:
                    self.window.remove(self.record_wr)
                    self.window.remove(self.start_bt)
                    self.window.remove(self.start_wr)
                    self.start_bt = GRect(2 * self.brick.width, 4 * self.brick.height,
                                          x=(self.window.width - 2 * self.brick.width) / 2,
                                          y=self.window.height-8*self.brick.height)
                    self.start_bt.fill_color = '#f2f7fa'
                    self.start_bt.color = '#79b5ba'
                    self.start_wr = GLabel('START')
                    self.window.add(self.start_bt)
                    self.window.add(self.start_wr, x=(self.window.width - self.start_wr.width) / 2,
                                    y=self.window.height-7*self.start_wr.height)
                    self.start_opr = 1
        if self.start_opr == 4:
            if here.x >= self.start_bt.x and here.y >= self.start_bt.y:
                if here.x <= self.start_bt.x+self.start_bt.width and here.y <= self.start_bt.y+self.start_bt.height:
                    self.window.remove(self.start_bt)
                    self.window.remove(self.start_wr)
                    self.reset_window()

    def x_tracker(self, axis):
        """板子跟著滑鼠動"""
        self.paddle.x = axis.x-self.paddle.width/2
        if axis.x < self.paddle.width/2:
            self.paddle.x = 0
        if axis.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width

    def launcher(self):
        """讓球動起來"""
        self.dx = MAX_X_SPEED
        self.dy = INITIAL_Y_SPEED

    def hit_box(self):
        """碰撞檢測器，不設在方形的四個角是因為我不知道要怎樣檢測其中一個點撞到磚塊時，
        要怎麼判斷撞到的是上面還是側便並做出相應方向的反彈"""
        bup = self.window.get_object_at(self.ball.x+self.br, self.ball.y)
        bdo = self.window.get_object_at(self.ball.x + self.br, self.ball.y+2*self.br)
        ble = self.window.get_object_at(self.ball.x, self.ball.y+self.br)
        bri = self.window.get_object_at(self.ball.x+2*self.br, self.ball.y+self.br)
        used_obj = [self.paddle, self.ball, self.eft1, self.eft2, self.eft3, self.eft4, self.count_board,
                    self.score, self.score_num, self.laser_eft]
        """檢測四個點撞到物件後反彈"""
        if bup not in used_obj:
            if self.fire_tou == 0:
                self.dy = -self.dy
            self.window.remove(bup)
            self.sc += 1
        elif bdo not in used_obj:
            if self.fire_tou == 0:
                self.dy = -self.dy
            self.window.remove(bdo)
            self.sc += 1
        elif ble not in used_obj:
            if self.fire_tou == 0:
                self.dy = -self.dy
            self.window.remove(ble)
            self.sc += 1
        elif bri not in used_obj:
            if self.fire_tou == 0:
                self.dy = -self.dy
            self.window.remove(bri)
            self.sc += 1
        """檢測球撞板子"""
        if self.ball.x + self.ball.width >= self.paddle.x and self.ball.x <= self.paddle.x + self.paddle.width:
            if self.ball.y + self.ball.height >= self.paddle.y and self.dy > 0:
                self.dy = -self.dy
                self.get_v += 1
        """四個都在檢測有沒有撞到紅色技能磚塊"""
        if bup is self.laser_brick:
            self.window.add(self.laser_eft, x=self.laser_brick.x+(self.laser_brick.width+self.laser_eft.width)/2,
                            y=self.laser_brick.y+(self.laser_brick.height+self.laser_eft.height)/2)
            self.eft_opr = 1
        if bdo is self.laser_brick:
            self.window.add(self.laser_eft, x=self.laser_brick.x+(self.laser_brick.width+self.laser_eft.width)/2,
                            y=self.laser_brick.y+(self.laser_brick.height+self.laser_eft.height)/2)
            self.eft_opr = 1
        if ble is self.laser_brick:
            self.window.add(self.laser_eft, x=self.laser_brick.x+(self.laser_brick.width+self.laser_eft.width)/2,
                            y=self.laser_brick.y+(self.laser_brick.height+self.laser_eft.height)/2)
            self.eft_opr = 1
        if bri is self.laser_brick:
            self.window.add(self.laser_eft, x=self.laser_brick.x+(self.laser_brick.width+self.laser_eft.width)/2,
                            y=self.laser_brick.y+(self.laser_brick.height+self.laser_eft.height)/2)
            self.eft_opr = 1
        """檢測到紅色技能特小方塊撞到板子，板子變紅"""
        if self.laser_eft.y + self.laser_eft.height >= self.paddle.y and self.dy > 0:
            if self.ball.x + self.ball.width >= self.paddle.x and self.ball.x <= self.paddle.x + self.paddle.width:
                self.paddle.fill_color = '#f59b98'
                self.paddle.color = '#db6763'
                self.window.remove(self.laser_eft)
                self.window.remove(self.laser_brick)
                self.fire += 1

    def reset_ball(self):
        """重設球速和位置，但不知道為何在球掉下去一次過後水平速度都會變成0"""
        self.ball.x = self.window.width/2-self.br
        self.ball.y = self.window.height/2-self.br
        self.dx = 1
        self.dy = 0
        self.add_v = random.randint(1, 2)
        if random.random() < 0.5:
            self.dx = -self.dx

    def game_end(self):
        """遊戲結束後的確認頁面"""
        self.start_wr = GLabel('ok!')
        self.window.add(self.start_bt)
        self.window.add(self.start_wr, x=(self.window.width - self.start_wr.width) / 2,
                        y=self.window.height-7*self.start_wr.height)
        self.end_wr.font = '-20'
        self.window.add(self.end_bar)
        self.window.add(self.end_wr)
        self.start_opr = 4

    def reset_window(self):
        """清除版面"""
        self.start_opr = 3
        sort_num = sorted(self.scs, reverse=True)
        sort_num = sort_num + [None, None, None, None]
        for i in range(62):
            for j in range(40):
                this = self.window.get_object_at(i*15, j*15)
                self.window.remove(this)
        self.record_wr = GLabel(f'record\n==============================================\n\n1.{sort_num[0]}\n\n'
                                f'2.{sort_num[1]}\n\n'f'3.{sort_num[2]}\n\n4.{sort_num[3]}\n\n5.{sort_num[4]}', 85, 420)
        self.record_wr.font = '-25'
        self.total_page()

    def total_page(self):
        """結算介面"""
        self.window.add(self.record_wr)
        self.window.add(self.start_bt)
        self.window.add(self.start_wr, x=(self.window.width - self.start_wr.width) / 2,
                        y=self.window.height-7*self.start_wr.height)
        self.start_opr = 5
