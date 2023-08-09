"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE

讓很多東西動起來，但不包括腦袋
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval, GLabel
from catapultbase import BreakoutGraphics

FRAME_RATE = 16         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()


def main():
    """檢測初始頁面的按鈕有沒有被點按"""
    while True:
        if graphics.start_opr == 2:
            ball_can_move()
        pause(FRAME_RATE)


def ball_can_move():
    # Add the animation loop here!
    delay_n = 21
    n_l = 1
    eft_size = 30
    eft_size2 = 20
    re_eft = 1
    hbx = 0
    hby = 0
    hbx2 = 0
    hby2 = 0
    score_counting = 0
    breaking_brick = 0
    eft_use = eft_size + delay_n * re_eft
    eft_use2 = eft_size2 + delay_n * re_eft
    v_ray = 0
    new_v = 0
    while n_l <= NUM_LIVES and graphics.sc != graphics.ro*graphics.co:
        """清理殘留特效、讓球移動、讓球在撞到物件後反彈"""
        graphics.score_num.font = '-18'
        graphics.window.remove(graphics.eft1)
        graphics.window.remove(graphics.eft3)
        graphics.ball.move(graphics.dx*graphics.add_v, graphics.dy)
        graphics.hit_box()
        """檢測清除物件的物件高度來給予相應的分數"""
        if breaking_brick != graphics.sc:
            breaking_brick += 1
            hbx = graphics.ball.x + graphics.ball.width / 2 - eft_use / 2
            hby = graphics.ball.y + graphics.ball.height / 2 - eft_use / 2
            hbx2 = graphics.ball.x + graphics.ball.width / 2 - eft_use2 / 2
            hby2 = graphics.ball.y + graphics.ball.height / 2 - eft_use2 / 2
            delay_n = 0
            if hby <= 105:
                score_counting += 5
                graphics.score_num.text = str(score_counting)
            if hby <= 142:
                score_counting += 4
                graphics.score_num.text = str(score_counting)
            if hby <= 180:
                score_counting += 3
                graphics.score_num.text = str(score_counting)
            if hby <= 218:
                score_counting += 2
                graphics.score_num.text = str(score_counting)
            if hby <= 256:
                score_counting += 1
                graphics.score_num.text = str(score_counting)
        """這邊原本是想說製造一個會隨著while迴圈相隔的pause值慢慢變大的特效，
        每圈迴圈後特效就會變大一點，直到到達設定的次數後重製，非常可能是讓程式卡頓的元凶，
        想法是製造一個特效A，把A存給B後經過一次pause刪除A，並且在製造一個A，以此類推，
        起先是覺得一個迴圈只有十幾毫秒根本看不見，但之後發現......好像看的見也，
        所以迴圈的很沒意義，大可丟進coder端，但我好累，算了"""
        if delay_n <= 1:
            graphics.window.remove(graphics.eft2)
            graphics.eft1 = GOval(eft_use, eft_use, x=hbx, y=hby)
            graphics.eft1.filled = True
            graphics.eft1.fill_color = '#a4d7f5'
            graphics.eft1.color = '#cfeafa'
            graphics.window.add(graphics.eft1)
            graphics.eft2 = graphics.eft1
            delay_n += 1
            graphics.score_num.font = '-22'

            graphics.window.remove(graphics.eft4)
            graphics.eft3 = GOval(eft_use2, eft_use2, x=hbx2, y=hby2)
            graphics.eft3.filled = True
            graphics.eft3.fill_color = '#f2f7fa'
            graphics.eft3.color = '#cfeafa'
            graphics.window.add(graphics.eft3)
            graphics.eft4 = graphics.eft3
            delay_n += 1
            graphics.score_num.font = '-22'
        """這邊是想實現當板子跟著滑鼠移動時，把板子移動的速度乘上某個加權值，在加到原先的球速上，
        但一寫出來就滿滿的bug，好比球會在板子左右兩邊的空中撞到板子，又或是我把板子向右移動，
        而球應該會向右加速，但卻朝著左邊加速的情況"""
        old_v = new_v
        new_v = graphics.paddle.x
        if graphics.get_v != v_ray:
            v_ray += 1
            change_v = 0.11 * (new_v - old_v)
            graphics.add_v += change_v
        """球撞到牆壁反彈，順便檢查是否發射完穿透彈，並讓板子變回藍色，但是coder端不知道是怎樣，又會讓板子變回紅色"""
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width > 0:
            graphics.add_v = -graphics.add_v
            if graphics.fire_tou != 0:
                graphics.fire_tou = 0
                graphics.paddle.fill_color = '#75c2c9'
                graphics.paddle.color = '#0e7f8a'
        if graphics.ball.y <= 30:
            graphics.dy = -graphics.dy
            if graphics.fire_tou != 0:
                graphics.fire_tou = 0
                graphics.paddle.fill_color = '#75c2c9'
                graphics.paddle.color = '#0e7f8a'
        """檢測球出界"""
        if graphics.ball.y >= graphics.window.height-graphics.ball.height > 0:
            graphics.reset_ball()
            n_l += 1
            """檢測遊戲結束，跳出確認介面"""
            if n_l > NUM_LIVES or graphics.sc == 50:
                graphics.get_v = 0
                graphics.add_v = 0
                graphics.end_wr = GLabel(f'Congratulations!!\n\n     score : {score_counting}', x=380, y=430)
                graphics.window.remove(graphics.ball)
                graphics.window.remove(graphics.paddle)
                graphics.game_end()
                graphics.scs = graphics.scs + [score_counting]
                breaking_brick = 0
                graphics.sc = 0
                score_counting = 0
            """還沒掉下去三次，重設球和速度"""
            if n_l <= NUM_LIVES:
                graphics.add_v = 0
                graphics.start_opr = 2
        """撞到紅色技能方塊後讓技能下落的動畫"""
        if graphics.eft_opr == 1:
            graphics.laser_eft.move(0, 7)
        """確認球撞到板子後改值"""
        if graphics.fire == 1:
            graphics.fire_tou = 1

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
