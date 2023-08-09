"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon
from campy.graphics.gwindow import GWindow
"""創建視窗"""
w = GWindow(width=1280, height=720, title='SAI')


def main():
    """
    作品名稱:Mint

    要畫畫就必須要有繪圖介面，然後要有可愛的女孩子，加上貓耳，完成!
    ((給我玩明日方舟
    """
    b1 = GRect(1280, 17, x=0, y=0)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GLine(0, 40, 1280, 40)
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(15, 15, x=1, y=21)
    b1.filled = True
    b1.fill_color = 'green'
    b1.color = 'forestgreen'
    w.add(b1)
    b1 = GLabel('PaintTool', x=21, y=30)
    b1.font = '-8'
    b1.color = 'darkviolet'
    w.add(b1)
    b1 = GLine(18, 33, 27, 32)
    b1.color = 'deeppink'
    w.add(b1)
    b1 = GLine(27, 32, 36, 32)
    b1.color = 'purple'
    w.add(b1)
    b1 = GLabel('SAI', x=65, y=33)
    b1.font = '-12'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('SAI', x=64, y=32)
    b1.font = '-12'
    b1.color = 'black'
    w.add(b1)
    b1 = GLine(36, 31, 44, 31)
    b1.color = 'blue'
    w.add(b1)
    b1 = GLine(44, 31, 51, 32)
    b1.color = 'aqua'
    w.add(b1)
    b1 = GLine(51, 32, 63, 33)
    b1.color = 'lightgreen'
    w.add(b1)
    b1 = GLine(63, 33, 72, 34)
    b1.color = 'yellow'
    w.add(b1)
    b1 = GLine(72, 34, 79, 33)
    b1.color = 'orange'
    w.add(b1)
    b1 = GLine(79, 33, 90, 32)
    b1.color = 'red'
    w.add(b1)
    b1 = GOval(15, 15, x=4, y=18)
    b1.filled = True
    b1.fill_color = 'lightgreen'
    b1.color = 'green'
    w.add(b1)
    b1 = GLine(4, 27, 13, 33)
    b1.color = 'brown'
    w.add(b1)
    b1 = GLine(5, 28, 12, 34)
    b1.color = 'brown'
    w.add(b1)
    b1 = GLine(7, 29, 10, 35)
    b1.color = 'brown'
    w.add(b1)
    b1 = GRect(6, 1, x=1195, y=28)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GRect(23, 18, x=1212, y=18)
    b1.filled = True
    b1.fill_color = 'steelblue'
    b1.color = 'steelblue'
    w.add(b1)
    b1 = GRect(6, 6, x=1222, y=22)
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(8, 8, x=1218, y=23)
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(5, 5, x=1219, y=25)
    b1.filled = True
    b1.fill_color = 'steelblue'
    b1.color = 'steelblue'
    w.add(b1)
    b1 = GRect(44, 18, x=1237, y=18)
    b1.filled = True
    b1.fill_color = 'darkred'
    b1.color = 'darkred'
    w.add(b1)
    b1 = GLine(1254, 23, 1261, 31)
    b1.color = 'white'
    w.add(b1)
    b1 = GLine(1254, 30, 1261, 22)
    b1.color = 'white'
    w.add(b1)
    b1 = GLabel('檔案(F)   編輯(E)   影像(C)   圖層(L)   選取(S)   濾鏡(T)   檢視(Y)   視窗(W)   其他(O)', x=10, y=58)
    b1.font = '-10'
    w.add(b1)
    b2 = GLine(0, 63, 1280, 63)
    b2.color = 'grey'
    w.add(b2)
    b1 = GLine(164, 63, 164, 720)
    b1.color = 'grey'
    w.add(b1)
    b1 = GLine(0, 164, 164, 164)
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(154, 50, x=4, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'ghostwhite'
    w.add(b1)
    b1 = GLabel('縮放倍率    50.0%', x=5, y=130)
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('旋轉角度    +000', x=5, y=151)
    b1.color = 'black'
    w.add(b1)
    b1 = GLine(6, 131, 96, 131)
    b1.color = 'darkgrey'
    w.add(b1)
    b1 = GLine(6, 152, 96, 152)
    b1.color = 'darkgrey'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((37, 137))
    b1.add_vertex((41, 133))
    b1.add_vertex((45, 137))
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((47, 158))
    b1.add_vertex((51, 154))
    b1.add_vertex((55, 158))
    w.add(b1)
    b1 = GRect(1280, 20, x=0, y=700)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=104, y=121)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=104, y=142)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=124, y=121)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=124, y=142)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=144, y=121)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=144, y=142)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(13, 3, x=75, y=163)
    b1.filled = True
    b1.fill_color = 'grey'
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(16, 16, x=342, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=596, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=614, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=632, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=724, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=742, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=760, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=828, y=66)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(16, 16, x=360, y=66)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(16, 16, x=390, y=66)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(16, 16, x=408, y=66)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(10, 10, x=436, y=70)
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('選取範圍邊緣', x=450, y=83)
    w.add(b1)
    b1 = GLabel('正常', x=793, y=83)
    w.add(b1)
    b1 = GLabel('抖動修正   10', x=855, y=83)
    w.add(b1)
    b1 = GRect(43, 15, x=905, y=67)
    b1.color = 'silver'
    w.add(b1)
    downbutten(933, 69)
    b1 = GRect(64, 15, x=528, y=67)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(59, 15, x=662, y=67)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(36, 15, x=788, y=67)
    b1.color = 'silver'
    w.add(b1)
    downbutten(708, 69)
    b1 = GLabel('+000', x=667, y=83)
    w.add(b1)
    b1 = GLabel('50%', x=532, y=83)
    w.add(b1)
    b1 = GRect(10, 10, x=3, y=168)
    b1.filled = True
    b1.fill_color = 'grey'
    b1.color = 'black'
    w.add(b1)
    downbutten(322, 70)
    b1 = GLabel('畫材效果', x=17, y=181)
    w.add(b1)
    b1 = GLabel('畫材質感     【無質感】', x=11, y=198)
    w.add(b1)
    b1 = GRect(94, 18, x=63, y=181)
    b1.color = 'silver'
    w.add(b1)
    downbutten(139, 184)
    b1 = GRect(90, 15, x=13, y=203)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(50, 15, x=107, y=203)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('倍率          100%    強度 20 ', x=14, y=218)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('畫材效果     【無效果】', x=11, y=240)
    w.add(b1)
    b1 = GRect(8, 3, x=4, y=171)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(94, 18, x=63, y=223)
    b1.color = 'silver'
    w.add(b1)
    downbutten(139, 226)
    b1 = GRect(90, 15, x=13, y=245)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(50, 15, x=107, y=245)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('程度                   1   強度100 ', x=14, y=260)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('混合模式', x=2, y=282)
    w.add(b1)
    b1 = GLabel('不透明度', x=2, y=302)
    w.add(b1)
    b1 = GLabel('鎖定透明', x=17, y=319)
    w.add(b1)
    b1 = GLabel('剪裁遮色', x=17, y=333)
    w.add(b1)
    b1 = GLabel('指定選項', x=17, y=347)
    w.add(b1)
    b1 = GRect(157, 325, x=3, y=355)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(103, 132, x=57, y=266)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GLine(57, 283, 160, 283)
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GRect(10, 10, x=3, y=306)
    w.add(b1)
    b1 = GRect(10, 10, x=3, y=320)
    w.add(b1)
    b1 = GOval(10, 10, x=3, y=334)
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((15, 360))
    b1.add_vertex((15, 373))
    b1.add_vertex((27, 373))
    b1.add_vertex((27, 364))
    b1.add_vertex((22, 360))
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GLine(22, 360, 22, 364)
    w.add(b1)
    b1 = GLine(22, 364, 27, 364)
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((38, 360))
    b1.add_vertex((38, 373))
    b1.add_vertex((50, 373))
    b1.add_vertex((50, 364))
    b1.add_vertex((45, 360))
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    layers(5, 399)
    b1 = GRect(140, 37, x=5, y=437)
    b1.filled = True
    b1.fill_color = 'lavender'
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GRect(13, 13, x=5 + 4, y=437 + 4)
    w.add(b1)
    b1 = GRect(13, 13, x=5 + 4, y=437 + 20)
    w.add(b1)
    b1 = GRect(29, 29, x=5 + 20, y=437 + 4)
    w.add(b1)
    b1 = GLabel('正常', x=5 + 52, y=437 + 26)
    w.add(b1)
    b1 = GLabel('100%', x=5 + 52, y=437 + 39)
    w.add(b1)
    b1 = GOval(9, 6, x=5 + 6, y=437 + 8)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GOval(9, 5, x=5 + 6, y=437 + 9)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(3, 3, x=5 + 9, y=437 + 10)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    layers(5, 475)
    layers(5, 513)
    layers(5, 551)
    layers(5, 589)
    layers(5, 627)
    b1 = GLine(45, 360, 45, 364)
    w.add(b1)
    b1 = GLine(45, 364, 50, 364)
    w.add(b1)
    b1 = GLabel('正常', x=62, y=282)
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GRect(12, 12, x=145, y=268)
    b1.filled = True
    b1.fill_color = 'lavender'
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((145 + 3, 268 + 5))
    b1.add_vertex((145 + 9, 268 + 5))
    b1.add_vertex((145 + 6, 268 + 8))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(12, 108, x=145, y=286)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(12, 263, x=145, y=401)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    upbotten(145, 401)
    downbutten(145, 651)
    b1 = GRect(12, 12, x=145, y=286)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'grey'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((145 + 3, 286 + 7))
    b1.add_vertex((145 + 9, 286 + 7))
    b1.add_vertex((145 + 6, 286 + 4))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(12, 12, x=145, y=384)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'grey'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((145 + 3, 384 + 5))
    b1.add_vertex((145 + 9, 384 + 5))
    b1.add_vertex((145 + 6, 384 + 8))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(83, 12, x=59, y=285)
    b1.filled = True
    b1.fill_color = 'grey'
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(83, 12, x=59, y=300)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('正常', x=62, y=299)
    w.add(b1)
    b1 = GLabel('色彩增值', x=62, y=313)
    w.add(b1)
    b1 = GLabel('濾色', x=62, y=327)
    w.add(b1)
    b1 = GLabel('覆蓋', x=62, y=341)
    w.add(b1)
    b1 = GLabel('發光', x=62, y=355)
    w.add(b1)
    b1 = GLabel('陰影', x=62, y=369)
    w.add(b1)
    b1 = GLabel('明暗', x=62, y=383)
    w.add(b1)
    b1 = GLabel('黑白', x=62, y=397)
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((112, 310))
    b1.add_vertex((112, 326))
    b1.add_vertex((117, 323))
    b1.add_vertex((118, 328))
    b1.add_vertex((121, 326))
    b1.add_vertex((118, 322))
    b1.add_vertex((123, 321))
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(12, 134, x=145, y=462)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GRect(17, 16, x=169, y=66)
    b1.filled = True
    b1.fill_color = 'lavender'
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GRect(17, 16, x=255, y=66)
    b1.filled = True
    b1.fill_color = 'lavender'
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GRect(17, 14, x=191, y=67)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(17, 14, x=212, y=67)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(17, 14, x=233, y=67)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(17, 14, x=277, y=67)
    b1.color = 'silver'
    w.add(b1)
    downbutten(579, 69)
    """中間"""
    b1 = GRect(938, 574, x=342, y=86)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(164, 88, x=171, y=245)
    b1.color = 'silver'
    w.add(b1)
    nouseyet()
    b1 = GRect(12, 83, x=320, y=247)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    upbotten(320, 247)
    downbutten(320, 319)
    b1 = GRect(12, 26, x=320, y=262)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GRect(164, 88, x=171, y=385)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(12, 83, x=320, y=388)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    upbotten(320, 388)
    downbutten(320, 459)
    b1 = GRect(12, 6, x=320, y=403)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GRect(26, 26, x=309, y=353)
    w.add(b1)
    b1 = GRect(26, 26, x=294, y=337)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(22, 22, x=296, y=339)
    b1.filled = True
    b1.fill_color = 'burlywood'
    b1.color = 'burlywood'
    w.add(b1)
    b1 = GRect(8, 8, x=295, y=369)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(3, 3, x=296, y=373)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'gainsboro'
    w.add(b1)
    b1 = GRect(3, 3, x=299, y=370)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'gainsboro'
    w.add(b1)
    againuse()
    tenspace()
    b1 = GRect(36, 28, x=245, y=443)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(36, 28, x=281, y=443)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GLine(170, 481, 336, 481)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(13, 3, x=245, y=480)
    b1.filled = True
    b1.fill_color = 'grey'
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(94, 16, x=170, y=488)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(66, 16, x=268, y=488)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('正常', x=173, y=504)
    w.add(b1)
    downbutten(250, 490)
    b1 = GRect(16, 13, x=317, y=490)
    b1.filled = True
    b1.fill_color = 'lavender'
    b1.color = 'mediumpurple'
    w.add(b1)
    b1 = GRect(12, 9, x=319, y=492)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((270, 501))
    b1.add_vertex((274, 495))
    b1.add_vertex((276, 494))
    b1.add_vertex((278, 495))
    b1.add_vertex((282, 501))
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((285, 501))
    b1.add_vertex((288, 494))
    b1.add_vertex((291, 493))
    b1.add_vertex((294, 494))
    b1.add_vertex((297, 501))
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((302, 501))
    b1.add_vertex((304, 493))
    b1.add_vertex((313, 493))
    b1.add_vertex((315, 501))
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GRect(94, 13, x=238, y=511)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(9, 9, x=240, y=513)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(77, 13, x=238, y=528)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(94, 13, x=238, y=549)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(90, 9, x=240, y=551)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'silver'
    w.add(b1)
    downbutten(224, 512)
    b1 = GLabel('最大直徑          x 5.0           55.0', x=169, y=526)
    w.add(b1)
    b1 = GLabel('最小直徑                          0%', x=169, y=543)
    w.add(b1)
    b1 = GLabel('筆刷濃度                              100', x=169, y=564)
    w.add(b1)
    b1 = GRect(110, 16, x=170, y=569)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('【通常的圓形】', x=176, y=585)
    w.add(b1)
    b1 = GRect(110, 16, x=170, y=591)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('【無材質】', x=176, y=607)
    w.add(b1)
    downbutten(266, 571)
    downbutten(266, 593)
    b1 = GRect(47, 16, x=285, y=569)
    b1.color = 'gainsboro'
    w.add(b1)
    b1 = GLabel('強度100', x=287, y=585)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(47, 16, x=285, y=591)
    b1.color = 'gainsboro'
    w.add(b1)
    b1 = GLabel('強度100', x=287, y=607)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(96, 14, x=238, y=614)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(96, 14, x=238, y=632)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(96, 14, x=238, y=650)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('混色                                            0', x=168, y=629)
    w.add(b1)
    b1 = GLabel('水份量                                        0', x=168, y=647)
    w.add(b1)
    b1 = GLabel('色延伸                                        0', x=168, y=665)
    w.add(b1)
    b1 = GRect(12, 12, x=238, y=668)
    b1.color = 'silver'
    w.add(b1)
    b1 = GLabel('維持不透明度', x=254, y=682)
    w.add(b1)
    b1 = GRect(16, 556, x=1262, y=86)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    upbotten(1264, 88)
    downbutten(1264, 628)
    b1 = GRect(12, 400, x=1264, y=132)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GRect(918, 16, x=343, y=643)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(16, 16, x=1262, y=643)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(600, 12, x=462, y=645)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GRect(12, 12, x=345, y=645)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((345 + 7, 645 + 3))
    b1.add_vertex((345 + 7, 645 + 9))
    b1.add_vertex((345 + 4, 645 + 6))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(12, 12, x=1247, y=645)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((1247 + 5, 645 + 3))
    b1.add_vertex((1247 + 5, 645 + 9))
    b1.add_vertex((1247 + 8, 645 + 6))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GLabel('鉛筆     噴槍     筆        水彩筆', x=175, y=400)
    b1.font = '-8'
    w.add(b1)
    b1 = GLabel('馬克筆 橡皮擦 選擇筆 選取擦', x=175, y=428)
    b1.font = '-8'
    w.add(b1)
    b1 = GLabel('油漆桶 值筆', x=175, y=456)
    b1.font = '-8'
    w.add(b1)
    colorcircle(175, 85)
    b1 = GOval(151, 151, x=178, y=87)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(150, 150, x=179, y=88)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(149, 149, x=179, y=88)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(148, 148, x=179, y=88)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(147, 147, x=180, y=89)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(145, 145, x=181, y=90)
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(111, 111, x=198, y=107)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(103, 103, x=202, y=111)
    b1.color = 'silver'
    w.add(b1)
    b1 = GOval(153, 153, x=177, y=86)
    b1.color = 'silver'
    w.add(b1)
    colorrect()
    b1 = GOval(9, 9, x=240, y=130)
    b1.filled = True
    b1.fill_color = 'darkgrey'
    w.add(b1)
    b1 = GOval(5, 5, x=242, y=132)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(9, 9, x=216, y=102)
    b1.filled = True
    b1.fill_color = 'darkgrey'
    w.add(b1)
    b1 = GOval(5, 5, x=218, y=104)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(44, 44, x=57, y=69)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(6, 6, x=149, y=126)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(6, 6, x=149, y=147)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(8, 2, x=108, y=128)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(8, 2, x=128, y=128)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(2, 8, x=131, y=125)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(8, 2, x=600, y=73)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(8, 2, x=618, y=73)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(2, 8, x=621, y=70)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(6, 6, x=637, y=71)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(6, 6, x=765, y=71)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('⇆', x=829, y=82)
    b1.font = '-13'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('↺ ↻', x=725, y=83)
    b1.font = '-11'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('↺ ↻', x=343, y=83)
    b1.font = '-11'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('↺ ↻', x=105, y=159)
    b1.font = '-12'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('⌧ ∺', x=392, y=83)
    b1.font = '-11'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GLabel('✔', x=436, y=82)
    b1.font = '-9'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('✔', x=240, y=681)
    b1.font = '-9'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('≡ ≡ ≡', x=191, y=83)
    b1.font = '-13'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('⚪', x=171, y=80)
    b1.font = '-8'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('░', x=258, y=80)
    b1.font = '-8'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('⧉ ⧉', x=12, y=397)
    b1.font = '-13'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('←', x=324, y=347)
    b1.font = '-6'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('↓', x=327, y=350)
    b1.font = '-6'
    b1.color = 'black'
    w.add(b1)
    b1 = GLabel('〾', x=53, y=122)
    b1.font = '-40'
    b1.color = 'red'
    w.add(b1)
    b1 = GRect(30, 30, x=61, y=77)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    drawing()


def colorcircle(x, y):
    """
    TODO:色相環
    """
    b1 = GOval(21, 21, x=x+70, y=y+5)
    b1.filled = True
    b1.fill_color = 'yellow'
    b1.color = 'yellow'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 65, y=y + 5)
    b1.filled = True
    b1.fill_color = 'yellow'
    b1.color = 'yellow'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 60, y=y + 5)
    b1.filled = True
    b1.fill_color = 'gold'
    b1.color = 'gold'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 55, y=y + 5)
    b1.filled = True
    b1.fill_color = 'gold'
    b1.color = 'gold'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 50, y=y + 5)
    b1.filled = True
    b1.fill_color = 'gold'
    b1.color = 'gold'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 45, y=y + 10)
    b1.filled = True
    b1.fill_color = 'orange'
    b1.color = 'orange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 40, y=y + 10)
    b1.filled = True
    b1.fill_color = 'orange'
    b1.color = 'orange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 35, y=y + 15)
    b1.filled = True
    b1.fill_color = 'orange'
    b1.color = 'orange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 30, y=y + 15)
    b1.filled = True
    b1.fill_color = 'darkorange'
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 25, y=y + 20)
    b1.filled = True
    b1.fill_color = 'darkorange'
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 20, y=y + 25)
    b1.filled = True
    b1.fill_color = 'darkorange'
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 15, y=y + 30)
    b1.filled = True
    b1.fill_color = 'orangered'
    b1.color = 'orangered'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 15, y=y + 35)
    b1.filled = True
    b1.fill_color = 'orangered'
    b1.color = 'orangered'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 10, y=y + 40)
    b1.filled = True
    b1.fill_color = 'orangered'
    b1.color = 'orangered'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 10, y=y + 45)
    b1.filled = True
    b1.fill_color = 'red'
    b1.color = 'red'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 50)
    b1.filled = True
    b1.fill_color = 'red'
    b1.color = 'red'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 55)
    b1.filled = True
    b1.fill_color = 'red'
    b1.color = 'red'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 60)
    b1.filled = True
    b1.fill_color = 'deeppink'
    b1.color = 'deeppink'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 65)
    b1.filled = True
    b1.fill_color = 'deeppink'
    b1.color = 'deeppink'
    w.add(b1)
    b1 = GOval(21, 21, x=x+5, y=y+70)
    b1.filled = True
    b1.fill_color = 'deeppink'
    b1.color = 'deeppink'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 75)
    b1.filled = True
    b1.fill_color = 'magenta'
    b1.color = 'magenta'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 80)
    b1.filled = True
    b1.fill_color = 'magenta'
    b1.color = 'magenta'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 5, y=y + 85)
    b1.filled = True
    b1.fill_color = 'magenta'
    b1.color = 'magenta'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 10, y=y + 90)
    b1.filled = True
    b1.fill_color = 'mediumorchid'
    b1.color = 'mediumorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 10, y=y + 95)
    b1.filled = True
    b1.fill_color = 'mediumorchid'
    b1.color = 'mediumorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 15, y=y + 100)
    b1.filled = True
    b1.fill_color = 'mediumorchid'
    b1.color = 'mediumorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 15, y=y + 105)
    b1.filled = True
    b1.fill_color = 'darkorchid'
    b1.color = 'darkorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 20, y=y + 110)
    b1.filled = True
    b1.fill_color = 'darkorchid'
    b1.color = 'darkorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 25, y=y + 115)
    b1.filled = True
    b1.fill_color = 'darkorchid'
    b1.color = 'darkorchid'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 30, y=y + 120)
    b1.filled = True
    b1.fill_color = 'blueviolet'
    b1.color = 'blueviolet'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 35, y=y + 120)
    b1.filled = True
    b1.fill_color = 'blueviolet'
    b1.color = 'blueviolet'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 40, y=y + 125)
    b1.filled = True
    b1.fill_color = 'blueviolet'
    b1.color = 'blueviolet'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 45, y=y + 125)
    b1.filled = True
    b1.fill_color = 'blue'
    b1.color = 'blue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 50, y=y + 130)
    b1.filled = True
    b1.fill_color = 'blue'
    b1.color = 'blue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 55, y=y + 130)
    b1.filled = True
    b1.fill_color = 'blue'
    b1.color = 'blue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 60, y=y + 130)
    b1.filled = True
    b1.fill_color = 'mediumblue'
    b1.color = 'mediumblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 65, y=y + 130)
    b1.filled = True
    b1.fill_color = 'mediumblue'
    b1.color = 'mediumblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 70, y=y + 130)
    b1.filled = True
    b1.fill_color = 'mediumblue'
    b1.color = 'mediumblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 75, y=y + 130)
    b1.filled = True
    b1.fill_color = 'blue'
    b1.color = 'blue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 80, y=y + 130)
    b1.filled = True
    b1.fill_color = 'royalblue'
    b1.color = 'royalblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 85, y=y + 130)
    b1.filled = True
    b1.fill_color = 'royalblue'
    b1.color = 'royalblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 90, y=y + 125)
    b1.filled = True
    b1.fill_color = 'royalblue'
    b1.color = 'royalblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 95, y=y + 125)
    b1.filled = True
    b1.fill_color = 'cornflowerblue'
    b1.color = 'cornflowerblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 100, y=y + 120)
    b1.filled = True
    b1.fill_color = 'cornflowerblue'
    b1.color = 'cornflowerblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 105, y=y + 120)
    b1.filled = True
    b1.fill_color = 'cornflowerblue'
    b1.color = 'cornflowerblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 110, y=y + 115)
    b1.filled = True
    b1.fill_color = 'deepskyblue'
    b1.color = 'deepskyblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 115, y=y + 110)
    b1.filled = True
    b1.fill_color = 'deepskyblue'
    b1.color = 'deepskyblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 120, y=y + 105)
    b1.filled = True
    b1.fill_color = 'deepskyblue'
    b1.color = 'deepskyblue'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 120, y=y + 100)
    b1.filled = True
    b1.fill_color = 'aqua'
    b1.color = 'aqua'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 125, y=y + 95)
    b1.filled = True
    b1.fill_color = 'aqua'
    b1.color = 'aqua'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 125, y=y + 90)
    b1.filled = True
    b1.fill_color = 'aqua'
    b1.color = 'aqua'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 85)
    b1.filled = True
    b1.fill_color = 'aquamarine'
    b1.color = 'aquamarine'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 80)
    b1.filled = True
    b1.fill_color = 'aquamarine'
    b1.color = 'aquamarine'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 75)
    b1.filled = True
    b1.fill_color = 'aquamarine'
    b1.color = 'aquamarine'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 70)
    b1.filled = True
    b1.fill_color = 'springgreen'
    b1.color = 'springgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x+130, y=y+65)
    b1.filled = True
    b1.fill_color = 'springgreen'
    b1.color = 'springgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 60)
    b1.filled = True
    b1.fill_color = 'springgreen'
    b1.color = 'springgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 55)
    b1.filled = True
    b1.fill_color = 'lime'
    b1.color = 'lime'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 130, y=y + 50)
    b1.filled = True
    b1.fill_color = 'lime'
    b1.color = 'lime'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 125, y=y + 45)
    b1.filled = True
    b1.fill_color = 'lime'
    b1.color = 'lime'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 125, y=y + 40)
    b1.filled = True
    b1.fill_color = 'lightgreen'
    b1.color = 'lightgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 120, y=y + 35)
    b1.filled = True
    b1.fill_color = 'lightgreen'
    b1.color = 'lightgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 120, y=y + 30)
    b1.filled = True
    b1.fill_color = 'lightgreen'
    b1.color = 'lightgreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 115, y=y + 25)
    b1.filled = True
    b1.fill_color = 'palegreen'
    b1.color = 'palegreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 105, y=y + 20)
    b1.filled = True
    b1.fill_color = 'palegreen'
    b1.color = 'palegreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 100, y=y + 15)
    b1.filled = True
    b1.fill_color = 'palegreen'
    b1.color = 'palegreen'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 95, y=y + 15)
    b1.filled = True
    b1.fill_color = 'greenyellow'
    b1.color = 'greenyellow'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 90, y=y + 10)
    b1.filled = True
    b1.fill_color = 'greenyellow'
    b1.color = 'greenyellow'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 85, y=y + 10)
    b1.filled = True
    b1.fill_color = 'greenyellow'
    b1.color = 'greenyellow'
    w.add(b1)
    b1 = GOval(21, 21, x=x + 80, y=y + 5)
    b1.filled = True
    b1.fill_color = 'yellow'
    b1.color = 'yellow'
    w.add(b1)


def drawing():
    """
    TODO:繪製人物
    """
    b1 = GRect(917, 555, x=343, y=87)
    b1.filled = True
    b1.fill_color = 'grey'
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(557, 553, x=516, y=88)
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((682, 347))
    b1.add_vertex((674, 312))
    b1.add_vertex((700, 252))
    b1.add_vertex((829, 275))
    b1.add_vertex((835, 341))
    b1.filled = True
    b1.fill_color = '#AA9992'
    b1.color = '#AA9992'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((703, 291))
    b1.add_vertex((775, 265))
    b1.add_vertex((817, 310))
    b1.add_vertex((815, 359))
    b1.add_vertex((770, 400))
    b1.add_vertex((700, 385))
    b1.add_vertex((680, 357))
    b1.filled = True
    b1.fill_color = '#D8C6BC'
    b1.color = '#D8C6BC'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((754, 344))
    b1.add_vertex((763, 339))
    b1.add_vertex((773, 346))
    b1.filled = True
    b1.fill_color = '#E8E3E0'
    b1.color = '#E8E3E0'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((693, 346))
    b1.add_vertex((723, 348))
    b1.add_vertex((735, 354))
    b1.add_vertex((733, 369))
    b1.add_vertex((720, 379))
    b1.add_vertex((701, 375))
    b1.add_vertex((678, 362))
    b1.add_vertex((686, 343))
    b1.filled = True
    b1.fill_color = '#DDBBAF'
    b1.color = '#DDBBAF'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((793, 334))
    b1.add_vertex((807, 326))
    b1.add_vertex((813, 335))
    b1.add_vertex((813, 347))
    b1.add_vertex((801, 352))
    b1.add_vertex((788, 348))
    b1.filled = True
    b1.fill_color = '#DDBBAF'
    b1.color = '#DDBBAF'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((698, 350))
    b1.add_vertex((693, 345))
    b1.add_vertex((693, 350))
    b1.add_vertex((685, 341))
    b1.add_vertex((689, 324))
    b1.add_vertex((712, 312))
    b1.add_vertex((732, 316))
    b1.add_vertex((731, 319))
    b1.add_vertex((727, 320))
    b1.add_vertex((730, 324))
    b1.filled = True
    b1.fill_color = '#505052'
    b1.color = '#505052'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((780, 316))
    b1.add_vertex((779, 308))
    b1.add_vertex((798, 293))
    b1.add_vertex((808, 296))
    b1.add_vertex((819, 304))
    b1.add_vertex((823, 305))
    b1.add_vertex((819, 307))
    b1.add_vertex((814, 351))
    b1.add_vertex((813, 333))
    b1.add_vertex((814, 311))
    b1.add_vertex((810, 321))
    b1.filled = True
    b1.fill_color = '#505052'
    b1.color = '#505052'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((693, 340))
    b1.add_vertex((702, 350))
    b1.add_vertex((723, 345))
    b1.add_vertex((730, 325))
    b1.add_vertex((695, 334))
    b1.filled = True
    b1.fill_color = '#DCDFE6'
    b1.color = '#DCDFE6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((796, 334))
    b1.add_vertex((808, 326))
    b1.add_vertex((810, 312))
    b1.add_vertex((805, 305))
    b1.add_vertex((798, 301))
    b1.filled = True
    b1.fill_color = '#DCDFE6'
    b1.color = '#DCDFE6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((700, 345))
    b1.add_vertex((698, 341))
    b1.add_vertex((696, 332))
    b1.add_vertex((702, 325))
    b1.add_vertex((717, 320))
    b1.add_vertex((723, 327))
    b1.add_vertex((723, 342))
    b1.filled = True
    b1.fill_color = '#57616B'
    b1.color = '#57616B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((786, 335))
    b1.add_vertex((779, 320))
    b1.add_vertex((782, 312))
    b1.add_vertex((790, 304))
    b1.add_vertex((798, 302))
    b1.add_vertex((801, 312))
    b1.add_vertex((800, 320))
    b1.filled = True
    b1.fill_color = '#57616B'
    b1.color = '#57616B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((702, 345))
    b1.add_vertex((700, 341))
    b1.add_vertex((702, 337))
    b1.add_vertex((704, 338))
    b1.add_vertex((711, 337))
    b1.add_vertex((713, 332))
    b1.add_vertex((715, 334))
    b1.add_vertex((723, 334))
    b1.add_vertex((723, 342))
    b1.add_vertex((721, 346))
    b1.add_vertex((720, 349))
    b1.add_vertex((717, 352))
    b1.filled = True
    b1.fill_color = '#858F9B'
    b1.color = '#858F9B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((801, 319))
    b1.add_vertex((800, 325))
    b1.add_vertex((795, 332))
    b1.add_vertex((785, 333))
    b1.add_vertex((781, 326))
    b1.add_vertex((782, 321))
    b1.add_vertex((784, 317))
    b1.add_vertex((787, 322))
    b1.add_vertex((791, 315))
    b1.add_vertex((793, 319))
    b1.add_vertex((796, 314))
    b1.filled = True
    b1.fill_color = '#858F9B'
    b1.color = '#858F9B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((721, 341))
    b1.add_vertex((721, 346))
    b1.add_vertex((716, 352))
    b1.add_vertex((710, 353))
    b1.add_vertex((703, 350))
    b1.add_vertex((702, 348))
    b1.add_vertex((705, 342))
    b1.add_vertex((713, 338))
    b1.filled = True
    b1.fill_color = '#A8AEAE'
    b1.color = '#A8AEAE'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((792, 326))
    b1.add_vertex((793, 329))
    b1.add_vertex((792, 334))
    b1.add_vertex((786, 334))
    b1.add_vertex((784, 329))
    b1.add_vertex((785, 324))
    b1.filled = True
    b1.fill_color = '#A8AEAE'
    b1.color = '#A8AEAE'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((708, 285))
    b1.add_vertex((772, 269))
    b1.add_vertex((782, 277))
    b1.add_vertex((837, 287))
    b1.add_vertex((847, 397))
    b1.add_vertex((954, 459))
    b1.add_vertex((999, 612))
    b1.add_vertex((1045, 641))
    b1.add_vertex((1073, 641))
    b1.add_vertex((1073, 541))
    b1.add_vertex((844, 218))
    b1.add_vertex((793, 163))
    b1.add_vertex((729, 151))
    b1.add_vertex((600, 142))
    b1.add_vertex((517, 516))
    b1.add_vertex((517, 554))
    b1.add_vertex((572, 553))
    b1.add_vertex((731, 430))
    b1.add_vertex((704, 389))
    b1.add_vertex((655, 322))
    b1.add_vertex((697, 285))
    b1.filled = True
    b1.fill_color = '#D1C7BD'
    b1.color = '#D1C7BD'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((621, 408))
    b1.add_vertex((608, 371))
    b1.add_vertex((610, 308))
    b1.add_vertex((617, 242))
    b1.add_vertex((598, 224))
    b1.add_vertex((597, 196))
    b1.add_vertex((621, 188))
    b1.add_vertex((627, 198))
    b1.add_vertex((637, 181))
    b1.add_vertex((689, 155))
    b1.add_vertex((749, 149))
    b1.add_vertex((774, 129))
    b1.add_vertex((791, 141))
    b1.add_vertex((799, 171))
    b1.add_vertex((784, 168))
    b1.add_vertex((773, 165))
    b1.add_vertex((765, 165))
    b1.add_vertex((742, 157))
    b1.add_vertex((726, 169))
    b1.add_vertex((735, 157))
    b1.add_vertex((727, 157))
    b1.add_vertex((725, 159))
    b1.add_vertex((721, 167))
    b1.add_vertex((718, 164))
    b1.add_vertex((719, 161))
    b1.add_vertex((714, 163))
    b1.add_vertex((693, 161))
    b1.add_vertex((676, 165))
    b1.add_vertex((691, 165))
    b1.add_vertex((659, 177))
    b1.add_vertex((644, 198))
    b1.add_vertex((641, 211))
    b1.add_vertex((649, 206))
    b1.add_vertex((643, 217))
    b1.add_vertex((646, 224))
    b1.add_vertex((643, 233))
    b1.add_vertex((648, 241))
    b1.add_vertex((653, 233))
    b1.add_vertex((649, 258))
    b1.add_vertex((654, 249))
    b1.add_vertex((651, 270))
    b1.add_vertex((652, 319))
    b1.add_vertex((659, 286))
    b1.add_vertex((663, 228))
    b1.add_vertex((668, 202))
    b1.add_vertex((690, 177))
    b1.add_vertex((704, 171))
    b1.add_vertex((715, 171))
    b1.add_vertex((691, 181))
    b1.add_vertex((674, 200))
    b1.add_vertex((665, 224))
    b1.add_vertex((665, 246))
    b1.add_vertex((673, 227))
    b1.add_vertex((668, 253))
    b1.add_vertex((674, 249))
    b1.add_vertex((674, 259))
    b1.add_vertex((681, 262))
    b1.add_vertex((680, 271))
    b1.add_vertex((684, 269))
    b1.add_vertex((690, 285))
    b1.add_vertex((700, 273))
    b1.add_vertex((697, 241))
    b1.add_vertex((702, 213))
    b1.add_vertex((714, 194))
    b1.add_vertex((702, 217))
    b1.add_vertex((700, 245))
    b1.add_vertex((711, 274))
    b1.add_vertex((722, 273))
    b1.add_vertex((725, 262))
    b1.add_vertex((739, 275))
    b1.add_vertex((750, 261))
    b1.add_vertex((760, 273))
    b1.add_vertex((759, 255))
    b1.add_vertex((765, 263))
    b1.add_vertex((769, 244))
    b1.add_vertex((761, 217))
    b1.add_vertex((759, 215))
    b1.add_vertex((757, 230))
    b1.add_vertex((757, 210))
    b1.add_vertex((751, 195))
    b1.add_vertex((762, 214))
    b1.add_vertex((769, 237))
    b1.add_vertex((780, 272))
    b1.add_vertex((782, 263))
    b1.add_vertex((784, 256))
    b1.add_vertex((789, 259))
    b1.add_vertex((790, 253))
    b1.add_vertex((798, 243))
    b1.add_vertex((799, 232))
    b1.add_vertex((808, 243))
    b1.add_vertex((806, 230))
    b1.add_vertex((818, 239))
    b1.add_vertex((814, 219))
    b1.add_vertex((822, 231))
    b1.add_vertex((828, 243))
    b1.add_vertex((827, 220))
    b1.add_vertex((841, 243))
    b1.add_vertex((851, 280))
    b1.add_vertex((851, 266))
    b1.add_vertex((861, 296))
    b1.add_vertex((861, 337))
    b1.add_vertex((820, 390))
    b1.add_vertex((821, 339))
    b1.add_vertex((829, 302))
    b1.add_vertex((801, 292))
    b1.add_vertex((790, 294))
    b1.add_vertex((774, 269))
    b1.add_vertex((775, 305))
    b1.add_vertex((772, 314))
    b1.add_vertex((750, 323))
    b1.add_vertex((745, 321))
    b1.add_vertex((732, 309))
    b1.add_vertex((719, 319))
    b1.add_vertex((714, 308))
    b1.add_vertex((702, 277))
    b1.add_vertex((696, 304))
    b1.add_vertex((694, 329))
    b1.add_vertex((691, 320))
    b1.add_vertex((682, 333))
    b1.add_vertex((687, 357))
    b1.add_vertex((696, 367))
    b1.add_vertex((715, 371))
    b1.add_vertex((708, 375))
    b1.add_vertex((717, 377))
    b1.add_vertex((700, 377))
    b1.add_vertex((684, 370))
    b1.add_vertex((701, 396))
    b1.add_vertex((736, 433))
    b1.add_vertex((565, 555))
    b1.add_vertex((526, 506))
    b1.filled = True
    b1.fill_color = '#C5B2AA'
    b1.color = '#C5B2AA'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((883, 416))
    b1.add_vertex((904, 420))
    b1.add_vertex((915, 441))
    b1.add_vertex((892, 432))
    b1.filled = True
    b1.fill_color = '#C5B2AA'
    b1.color = '#C5B2AA'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((746, 149))
    b1.add_vertex((712, 156))
    b1.add_vertex((708, 152))
    b1.add_vertex((694, 161))
    b1.add_vertex((696, 155))
    b1.add_vertex((670, 165))
    b1.add_vertex((653, 179))
    b1.add_vertex((637, 190))
    b1.add_vertex((627, 211))
    b1.add_vertex((623, 241))
    b1.add_vertex((634, 214))
    b1.add_vertex((629, 240))
    b1.add_vertex((622, 259))
    b1.add_vertex((615, 288))
    b1.add_vertex((629, 261))
    b1.add_vertex((626, 293))
    b1.add_vertex((620, 324))
    b1.add_vertex((614, 311))
    b1.add_vertex((610, 364))
    b1.add_vertex((614, 364))
    b1.add_vertex((612, 385))
    b1.add_vertex((615, 399))
    b1.add_vertex((619, 389))
    b1.add_vertex((613, 414))
    b1.add_vertex((598, 435))
    b1.add_vertex((609, 429))
    b1.add_vertex((568, 476))
    b1.add_vertex((570, 481))
    b1.add_vertex((549, 492))
    b1.add_vertex((610, 251))
    b1.add_vertex((593, 221))
    b1.add_vertex((604, 225))
    b1.add_vertex((605, 226))
    b1.add_vertex((611, 224))
    b1.add_vertex((612, 228))
    b1.add_vertex((620, 225))
    b1.add_vertex((620, 216))
    b1.add_vertex((625, 205))
    b1.add_vertex((622, 196))
    b1.add_vertex((637, 168))
    b1.add_vertex((674, 157))
    b1.add_vertex((702, 150))
    b1.add_vertex((738, 147))
    b1.filled = True
    b1.fill_color = '#AA9B96'
    b1.color = '#AA9B96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((632, 294))
    b1.add_vertex((635, 322))
    b1.add_vertex((643, 338))
    b1.add_vertex((642, 319))
    b1.add_vertex((649, 336))
    b1.add_vertex((652, 369))
    b1.add_vertex((641, 377))
    b1.add_vertex((641, 349))
    b1.add_vertex((630, 326))
    b1.add_vertex((628, 313))
    b1.filled = True
    b1.fill_color = '#AA9B96'
    b1.color = '#AA9B96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((680, 345))
    b1.add_vertex((688, 323))
    b1.add_vertex((691, 323))
    b1.add_vertex((690, 310))
    b1.add_vertex((688, 316))
    b1.add_vertex((687, 310))
    b1.add_vertex((680, 330))
    b1.add_vertex((676, 306))
    b1.add_vertex((696, 289))
    b1.add_vertex((694, 310))
    b1.add_vertex((703, 288))
    b1.add_vertex((713, 310))
    b1.add_vertex((719, 322))
    b1.add_vertex((718, 325))
    b1.add_vertex((730, 310))
    b1.add_vertex((746, 324))
    b1.add_vertex((745, 328))
    b1.add_vertex((756, 319))
    b1.add_vertex((767, 326))
    b1.add_vertex((764, 316))
    b1.add_vertex((775, 320))
    b1.add_vertex((773, 315))
    b1.add_vertex((774, 297))
    b1.add_vertex((772, 306))
    b1.add_vertex((775, 298))
    b1.add_vertex((772, 312))
    b1.add_vertex((759, 313))
    b1.add_vertex((750, 323))
    b1.add_vertex((752, 316))
    b1.add_vertex((739, 302))
    b1.add_vertex((743, 313))
    b1.add_vertex((730, 300))
    b1.add_vertex((725, 311))
    b1.add_vertex((719, 298))
    b1.add_vertex((717, 308))
    b1.add_vertex((706, 285))
    b1.add_vertex((699, 252))
    b1.add_vertex((696, 285))
    b1.add_vertex((687, 293))
    b1.add_vertex((672, 307))
    b1.add_vertex((667, 290))
    b1.add_vertex((668, 275))
    b1.add_vertex((663, 286))
    b1.add_vertex((661, 283))
    b1.add_vertex((674, 334))
    b1.filled = True
    b1.fill_color = '#AA9B96'
    b1.color = '#AA9B96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((804, 400))
    b1.add_vertex((848, 394))
    b1.add_vertex((880, 432))
    b1.add_vertex((866, 461))
    b1.add_vertex((668, 514))
    b1.add_vertex((659, 471))
    b1.add_vertex((678, 443))
    b1.filled = True
    b1.fill_color = '#DBC9BF'
    b1.color = '#DBC9BF'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((892, 426))
    b1.add_vertex((878, 400))
    b1.add_vertex((866, 400))
    b1.add_vertex((853, 396))
    b1.add_vertex((855, 391))
    b1.add_vertex((854, 384))
    b1.add_vertex((877, 390))
    b1.add_vertex((864, 380))
    b1.add_vertex((849, 370))
    b1.add_vertex((849, 383))
    b1.add_vertex((839, 359))
    b1.add_vertex((842, 335))
    b1.add_vertex((848, 322))
    b1.add_vertex((854, 317))
    b1.add_vertex((843, 288))
    b1.add_vertex((841, 292))
    b1.add_vertex((837, 280))
    b1.add_vertex((837, 308))
    b1.add_vertex((832, 322))
    b1.add_vertex((829, 304))
    b1.add_vertex((818, 262))
    b1.add_vertex((820, 279))
    b1.add_vertex((818, 300))
    b1.add_vertex((814, 296))
    b1.add_vertex((811, 288))
    b1.add_vertex((808, 292))
    b1.add_vertex((795, 286))
    b1.add_vertex((787, 279))
    b1.add_vertex((795, 290))
    b1.add_vertex((787, 299))
    b1.add_vertex((798, 293))
    b1.add_vertex((810, 295))
    b1.add_vertex((818, 302))
    b1.add_vertex((825, 303))
    b1.add_vertex((819, 308))
    b1.add_vertex((814, 328))
    b1.add_vertex((815, 347))
    b1.add_vertex((810, 359))
    b1.add_vertex((808, 372))
    b1.add_vertex((794, 392))
    b1.add_vertex((790, 394))
    b1.add_vertex((790, 398))
    b1.add_vertex((797, 407))
    b1.add_vertex((810, 440))
    b1.add_vertex((823, 436))
    b1.add_vertex((817, 429))
    b1.add_vertex((820, 426))
    b1.add_vertex((814, 425))
    b1.add_vertex((811, 416))
    b1.add_vertex((827, 412))
    b1.add_vertex((812, 408))
    b1.add_vertex((814, 412))
    b1.add_vertex((808, 416))
    b1.add_vertex((809, 400))
    b1.add_vertex((845, 400))
    b1.add_vertex((863, 428))
    b1.add_vertex((880, 449))
    b1.add_vertex((898, 457))
    b1.add_vertex((914, 475))
    b1.add_vertex((952, 469))
    b1.filled = True
    b1.fill_color = '#AA9B96'
    b1.color = '#AA9B96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((809, 405))
    b1.add_vertex((789, 392))
    b1.add_vertex((781, 403))
    b1.add_vertex((804, 417))
    b1.filled = True
    b1.fill_color = '#AC9B94'
    b1.color = '#AC9B94'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((780, 94))
    b1.add_vertex((768, 106))
    b1.add_vertex((767, 137))
    b1.add_vertex((776, 135))
    b1.add_vertex((776, 138))
    b1.add_vertex((785, 142))
    b1.add_vertex((787, 151))
    b1.add_vertex((793, 155))
    b1.add_vertex((795, 164))
    b1.add_vertex((801, 149))
    b1.add_vertex((791, 116))
    b1.filled = True
    b1.fill_color = '#87766F'
    b1.color = '#87766F'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((708, 384))
    b1.add_vertex((732, 392))
    b1.add_vertex((755, 397))
    b1.add_vertex((769, 398))
    b1.add_vertex((780, 390))
    b1.add_vertex((796, 388))
    b1.add_vertex((788, 397))
    b1.add_vertex((790, 413))
    b1.add_vertex((805, 409))
    b1.add_vertex((804, 416))
    b1.add_vertex((808, 423))
    b1.add_vertex((809, 426))
    b1.add_vertex((812, 429))
    b1.add_vertex((811, 447))
    b1.add_vertex((792, 443))
    b1.add_vertex((727, 457))
    b1.add_vertex((718, 461))
    b1.add_vertex((718, 454))
    b1.add_vertex((705, 460))
    b1.add_vertex((706, 457))
    b1.add_vertex((670, 445))
    b1.add_vertex((668, 436))
    b1.add_vertex((686, 424))
    b1.add_vertex((697, 430))
    b1.add_vertex((699, 434))
    b1.add_vertex((702, 430))
    b1.add_vertex((717, 432))
    b1.add_vertex((727, 430))
    b1.add_vertex((712, 418))
    b1.add_vertex((701, 408))
    b1.add_vertex((700, 398))
    b1.add_vertex((694, 392))
    b1.add_vertex((690, 383))
    b1.add_vertex((687, 387))
    b1.add_vertex((674, 381))
    b1.add_vertex((672, 385))
    b1.add_vertex((662, 379))
    b1.add_vertex((674, 400))
    b1.add_vertex((658, 387))
    b1.add_vertex((645, 437))
    b1.add_vertex((629, 465))
    b1.add_vertex((638, 437))
    b1.add_vertex((638, 421))
    b1.add_vertex((629, 436))
    b1.add_vertex((632, 422))
    b1.add_vertex((622, 416))
    b1.add_vertex((620, 435))
    b1.add_vertex((610, 456))
    b1.add_vertex((617, 433))
    b1.add_vertex((617, 418))
    b1.add_vertex((611, 426))
    b1.add_vertex((623, 389))
    b1.add_vertex((623, 406))
    b1.add_vertex((633, 393))
    b1.add_vertex((628, 395))
    b1.add_vertex((635, 385))
    b1.add_vertex((622, 373))
    b1.add_vertex((623, 359))
    b1.add_vertex((616, 345))
    b1.add_vertex((615, 333))
    b1.add_vertex((621, 347))
    b1.add_vertex((623, 330))
    b1.add_vertex((627, 312))
    b1.add_vertex((634, 339))
    b1.add_vertex((639, 351))
    b1.add_vertex((639, 378))
    b1.add_vertex((650, 371))
    b1.add_vertex((657, 375))
    b1.add_vertex((658, 367))
    b1.add_vertex((666, 367))
    b1.add_vertex((661, 348))
    b1.add_vertex((674, 365))
    b1.add_vertex((687, 372))
    b1.filled = True
    b1.fill_color = '#9D8B87'
    b1.color = '#9D8B87'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((787, 264))
    b1.add_vertex((799, 264))
    b1.add_vertex((817, 270))
    b1.add_vertex((801, 266))
    b1.filled = True
    b1.fill_color = '#AC9B94'
    b1.color = '#AC9B94'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((772, 156))
    b1.add_vertex((753, 150))
    b1.add_vertex((740, 148))
    b1.add_vertex((724, 149))
    b1.add_vertex((740, 125))
    b1.add_vertex((762, 96))
    b1.add_vertex((776, 88))
    b1.add_vertex((775, 113))
    b1.add_vertex((771, 137))
    b1.add_vertex((768, 149))
    b1.add_vertex((768, 153))
    b1.filled = True
    b1.fill_color = '#4C4A4D'
    b1.color = '#4C4A4D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((646, 178))
    b1.add_vertex((587, 160))
    b1.add_vertex((586, 166))
    b1.add_vertex((613, 179))
    b1.add_vertex((624, 193))
    b1.add_vertex((634, 193))
    b1.filled = True
    b1.fill_color = '#514F52'
    b1.color = '#514F52'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((775, 105))
    b1.add_vertex((777, 88))
    b1.add_vertex((783, 88))
    b1.add_vertex((793, 107))
    b1.add_vertex((798, 129))
    b1.add_vertex((789, 122))
    b1.add_vertex((783, 101))
    b1.filled = True
    b1.fill_color = '#675B5B'
    b1.color = '#675B5B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((774, 88))
    b1.add_vertex((771, 115))
    b1.add_vertex((770, 103))
    b1.add_vertex((768, 97))
    b1.add_vertex((759, 99))
    b1.add_vertex((770, 88))
    b1.filled = True
    b1.fill_color = '#675B5B'
    b1.color = '#675B5B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((806, 182))
    b1.add_vertex((805, 178))
    b1.add_vertex((807, 168))
    b1.add_vertex((803, 163))
    b1.add_vertex((807, 152))
    b1.add_vertex((803, 137))
    b1.add_vertex((801, 128))
    b1.add_vertex((797, 128))
    b1.add_vertex((797, 119))
    b1.add_vertex((793, 129))
    b1.add_vertex((798, 151))
    b1.add_vertex((794, 161))
    b1.add_vertex((797, 164))
    b1.add_vertex((793, 166))
    b1.add_vertex((797, 172))
    b1.add_vertex((791, 170))
    b1.filled = True
    b1.fill_color = '#5E5351'
    b1.color = '#5E5351'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((615, 266))
    b1.add_vertex((616, 242))
    b1.add_vertex((612, 235))
    b1.add_vertex((608, 231))
    b1.add_vertex((606, 236))
    b1.add_vertex((601, 229))
    b1.add_vertex((601, 225))
    b1.add_vertex((597, 223))
    b1.add_vertex((601, 218))
    b1.add_vertex((599, 217))
    b1.add_vertex((603, 209))
    b1.add_vertex((599, 207))
    b1.add_vertex((605, 203))
    b1.add_vertex((600, 201))
    b1.add_vertex((613, 198))
    b1.add_vertex((619, 188))
    b1.add_vertex((568, 162))
    b1.add_vertex((586, 233))
    b1.add_vertex((598, 262))
    b1.filled = True
    b1.fill_color = '#7E7570'
    b1.color = '#7E7570'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((625, 195))
    b1.add_vertex((618, 195))
    b1.add_vertex((609, 193))
    b1.add_vertex((616, 190))
    b1.add_vertex((594, 192))
    b1.add_vertex((603, 182))
    b1.add_vertex((579, 175))
    b1.add_vertex((573, 188))
    b1.add_vertex((565, 157))
    b1.add_vertex((628, 182))
    b1.filled = True
    b1.fill_color = '#695F5D'
    b1.color = '#695F5D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((650, 178))
    b1.add_vertex((639, 187))
    b1.add_vertex((629, 202))
    b1.add_vertex((624, 193))
    b1.add_vertex((618, 184))
    b1.add_vertex((602, 171))
    b1.add_vertex((585, 166))
    b1.add_vertex((573, 166))
    b1.add_vertex((571, 174))
    b1.add_vertex((588, 226))
    b1.add_vertex((599, 239))
    b1.add_vertex((599, 244))
    b1.add_vertex((601, 255))
    b1.add_vertex((601, 263))
    b1.add_vertex((610, 259))
    b1.add_vertex((610, 252))
    b1.add_vertex((605, 251))
    b1.add_vertex((609, 245))
    b1.add_vertex((614, 252))
    b1.add_vertex((612, 263))
    b1.add_vertex((613, 264))
    b1.add_vertex((613, 309))
    b1.add_vertex((609, 307))
    b1.add_vertex((605, 309))
    b1.add_vertex((604, 328))
    b1.add_vertex((593, 354))
    b1.add_vertex((586, 358))
    b1.add_vertex((598, 333))
    b1.add_vertex((601, 314))
    b1.add_vertex((588, 337))
    b1.add_vertex((586, 335))
    b1.add_vertex((594, 316))
    b1.add_vertex((591, 315))
    b1.add_vertex((587, 309))
    b1.add_vertex((583, 312))
    b1.add_vertex((579, 313))
    b1.add_vertex((583, 297))
    b1.add_vertex((590, 292))
    b1.add_vertex((591, 284))
    b1.add_vertex((599, 282))
    b1.add_vertex((608, 272))
    b1.add_vertex((598, 267))
    b1.add_vertex((589, 255))
    b1.add_vertex((591, 250))
    b1.add_vertex((581, 237))
    b1.add_vertex((568, 213))
    b1.add_vertex((560, 196))
    b1.add_vertex((558, 182))
    b1.add_vertex((555, 158))
    b1.add_vertex((562, 152))
    b1.add_vertex((575, 158))
    b1.add_vertex((578, 156))
    b1.add_vertex((595, 163))
    b1.add_vertex((590, 166))
    b1.add_vertex((619, 180))
    b1.add_vertex((624, 191))
    b1.add_vertex((632, 188))
    b1.add_vertex((636, 180))
    b1.add_vertex((642, 181))
    b1.add_vertex((638, 174))
    b1.filled = True
    b1.fill_color = '#343436'
    b1.color = '#343436'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((660, 246))
    b1.add_vertex((653, 280))
    b1.add_vertex((657, 274))
    b1.add_vertex((659, 292))
    b1.add_vertex((668, 318))
    b1.add_vertex((662, 295))
    b1.add_vertex((660, 269))
    b1.filled = True
    b1.fill_color = '#958A86'
    b1.color = '#958A86'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((627, 311))
    b1.add_vertex((630, 328))
    b1.add_vertex((640, 338))
    b1.add_vertex((641, 370))
    b1.add_vertex((637, 354))
    b1.add_vertex((631, 341))
    b1.add_vertex((625, 319))
    b1.filled = True
    b1.fill_color = '#756B69'
    b1.color = '#756B69'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((666, 370))
    b1.add_vertex((660, 366))
    b1.add_vertex((658, 374))
    b1.add_vertex((654, 363))
    b1.add_vertex((654, 352))
    b1.add_vertex((660, 363))
    b1.filled = True
    b1.fill_color = '#756B69'
    b1.color = '#756B69'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((685, 355))
    b1.add_vertex((685, 345))
    b1.add_vertex((679, 333))
    b1.add_vertex((679, 341))
    b1.add_vertex((672, 333))
    b1.add_vertex((679, 346))
    b1.filled = True
    b1.fill_color = '#958A86'
    b1.color = '#958A86'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((830, 323))
    b1.add_vertex((824, 294))
    b1.add_vertex((823, 306))
    b1.add_vertex((819, 306))
    b1.add_vertex((815, 324))
    b1.add_vertex((813, 338))
    b1.add_vertex((813, 354))
    b1.add_vertex((809, 362))
    b1.add_vertex((798, 376))
    b1.add_vertex((809, 389))
    b1.add_vertex((808, 376))
    b1.add_vertex((817, 356))
    b1.add_vertex((820, 362))
    b1.add_vertex((821, 342))
    b1.add_vertex((824, 317))
    b1.filled = True
    b1.fill_color = '#8D8183'
    b1.color = '#8D8183'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((813, 399))
    b1.add_vertex((807, 388))
    b1.add_vertex((803, 377))
    b1.add_vertex((801, 380))
    b1.add_vertex((799, 375))
    b1.add_vertex((775, 394))
    b1.add_vertex((790, 392))
    b1.add_vertex((808, 399))
    b1.filled = True
    b1.fill_color = '#5B595C'
    b1.color = '#5B595C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((687, 373))
    b1.add_vertex((696, 375))
    b1.add_vertex((704, 383))
    b1.add_vertex((715, 408))
    b1.add_vertex((705, 406))
    b1.add_vertex((699, 392))
    b1.add_vertex((694, 381))
    b1.filled = True
    b1.fill_color = '#5B595C'
    b1.color = '#5B595C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((679, 419))
    b1.add_vertex((672, 412))
    b1.add_vertex((666, 398))
    b1.add_vertex((662, 410))
    b1.add_vertex((666, 418))
    b1.add_vertex((660, 417))
    b1.add_vertex((662, 422))
    b1.add_vertex((671, 422))
    b1.filled = True
    b1.fill_color = '#5B595C'
    b1.color = '#5B595C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((656, 420))
    b1.add_vertex((654, 410))
    b1.add_vertex((653, 393))
    b1.add_vertex((650, 377))
    b1.add_vertex((646, 366))
    b1.add_vertex((643, 377))
    b1.add_vertex((646, 374))
    b1.add_vertex((649, 384))
    b1.add_vertex((648, 394))
    b1.add_vertex((644, 394))
    b1.add_vertex((639, 404))
    b1.add_vertex((642, 413))
    b1.add_vertex((643, 409))
    b1.add_vertex((649, 417))
    b1.filled = True
    b1.fill_color = '#5B595C'
    b1.color = '#5B595C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((747, 419))
    b1.add_vertex((741, 421))
    b1.add_vertex((738, 413))
    b1.add_vertex((737, 421))
    b1.add_vertex((727, 420))
    b1.add_vertex((716, 416))
    b1.add_vertex((709, 407))
    b1.add_vertex((724, 407))
    b1.add_vertex((746, 403))
    b1.filled = True
    b1.fill_color = '#4E503E'
    b1.color = '#4E503E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((775, 403))
    b1.add_vertex((770, 407))
    b1.add_vertex((764, 406))
    b1.add_vertex((763, 415))
    b1.add_vertex((758, 411))
    b1.add_vertex((756, 415))
    b1.add_vertex((746, 419))
    b1.add_vertex((744, 415))
    b1.add_vertex((738, 413))
    b1.add_vertex((742, 405))
    b1.add_vertex((734, 410))
    b1.add_vertex((727, 407))
    b1.add_vertex((724, 410))
    b1.add_vertex((719, 407))
    b1.add_vertex((718, 414))
    b1.add_vertex((713, 410))
    b1.add_vertex((715, 416))
    b1.add_vertex((707, 412))
    b1.add_vertex((706, 407))
    b1.add_vertex((709, 407))
    b1.add_vertex((705, 392))
    b1.add_vertex((707, 388))
    b1.add_vertex((704, 383))
    b1.add_vertex((709, 386))
    b1.add_vertex((711, 398))
    b1.add_vertex((720, 401))
    b1.add_vertex((724, 405))
    b1.add_vertex((730, 401))
    b1.add_vertex((736, 401))
    b1.add_vertex((741, 404))
    b1.add_vertex((746, 402))
    b1.add_vertex((753, 400))
    b1.add_vertex((750, 397))
    b1.add_vertex((761, 398))
    b1.add_vertex((768, 398))
    b1.add_vertex((773, 396))
    b1.filled = True
    b1.fill_color = '#333238'
    b1.color = '#333238'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((804, 408))
    b1.add_vertex((793, 417))
    b1.add_vertex((781, 439))
    b1.add_vertex((791, 442))
    b1.add_vertex((796, 448))
    b1.add_vertex((781, 446))
    b1.add_vertex((773, 457))
    b1.add_vertex((767, 458))
    b1.add_vertex((749, 470))
    b1.add_vertex((742, 462))
    b1.add_vertex((753, 439))
    b1.add_vertex((771, 439))
    b1.add_vertex((787, 409))
    b1.add_vertex((784, 401))
    b1.add_vertex((773, 398))
    b1.add_vertex((773, 395))
    b1.add_vertex((786, 399))
    b1.add_vertex((789, 404))
    b1.add_vertex((795, 407))
    b1.filled = True
    b1.fill_color = '#413B3B'
    b1.color = '#413B3B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((770, 444))
    b1.add_vertex((760, 459))
    b1.add_vertex((753, 465))
    b1.add_vertex((747, 460))
    b1.add_vertex((734, 435))
    b1.add_vertex((749, 438))
    b1.add_vertex((755, 441))
    b1.filled = True
    b1.fill_color = '#5B5C5E'
    b1.color = '#5B5C5E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((769, 448))
    b1.add_vertex((760, 458))
    b1.add_vertex((746, 458))
    b1.add_vertex((736, 463))
    b1.add_vertex((726, 462))
    b1.add_vertex((732, 468))
    b1.add_vertex((742, 464))
    b1.add_vertex((740, 457))
    b1.add_vertex((734, 456))
    b1.add_vertex((744, 448))
    b1.add_vertex((738, 448))
    b1.add_vertex((738, 439))
    b1.add_vertex((746, 438))
    b1.add_vertex((754, 444))
    b1.add_vertex((762, 445))
    b1.add_vertex((763, 448))
    b1.filled = True
    b1.fill_color = '#B1AEA7'
    b1.color = '#B1AEA7'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((699, 429))
    b1.add_vertex((678, 424))
    b1.add_vertex((687, 431))
    b1.filled = True
    b1.fill_color = '#736562'
    b1.color = '#736562'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((719, 459))
    b1.add_vertex((734, 462))
    b1.add_vertex((738, 462))
    b1.add_vertex((742, 456))
    b1.add_vertex((738, 455))
    b1.add_vertex((740, 459))
    b1.add_vertex((733, 457))
    b1.add_vertex((726, 457))
    b1.add_vertex((722, 455))
    b1.filled = True
    b1.fill_color = '#4F4543'
    b1.color = '#4F4543'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((716, 455))
    b1.add_vertex((715, 452))
    b1.add_vertex((706, 455))
    b1.filled = True
    b1.fill_color = '#4F4543'
    b1.color = '#4F4543'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((682, 447))
    b1.add_vertex((670, 460))
    b1.add_vertex((664, 483))
    b1.add_vertex((666, 494))
    b1.add_vertex((671, 508))
    b1.add_vertex((654, 514))
    b1.add_vertex((655, 447))
    b1.filled = True
    b1.fill_color = '#BBA49C'
    b1.color = '#BBA49C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((871, 641))
    b1.add_vertex((860, 614))
    b1.add_vertex((830, 614))
    b1.add_vertex((830, 641))
    b1.filled = True
    b1.fill_color = '#2F333C'
    b1.color = '#2F333C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((697, 452))
    b1.add_vertex((711, 451))
    b1.add_vertex((700, 447))
    b1.add_vertex((709, 444))
    b1.add_vertex((698, 438))
    b1.add_vertex((685, 447))
    b1.add_vertex((685, 443))
    b1.add_vertex((673, 445))
    b1.add_vertex((679, 438))
    b1.add_vertex((671, 440))
    b1.add_vertex((650, 448))
    b1.add_vertex((659, 479))
    b1.add_vertex((661, 471))
    b1.add_vertex((673, 473))
    b1.add_vertex((719, 475))
    b1.add_vertex((731, 476))
    b1.add_vertex((728, 484))
    b1.add_vertex((751, 472))
    b1.add_vertex((742, 463))
    b1.add_vertex((735, 466))
    b1.add_vertex((730, 464))
    b1.add_vertex((731, 470))
    b1.add_vertex((684, 468))
    b1.add_vertex((664, 465))
    b1.add_vertex((665, 457))
    b1.add_vertex((669, 451))
    b1.add_vertex((675, 450))
    b1.add_vertex((684, 450))
    b1.filled = True
    b1.fill_color = '#4F4543'
    b1.color = '#4F4543'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((657, 493))
    b1.add_vertex((663, 508))
    b1.add_vertex((743, 493))
    b1.add_vertex((803, 459))
    b1.add_vertex((793, 442))
    b1.add_vertex((811, 439))
    b1.add_vertex((820, 436))
    b1.add_vertex((828, 451))
    b1.add_vertex((842, 477))
    b1.add_vertex((851, 471))
    b1.add_vertex((882, 449))
    b1.add_vertex((919, 457))
    b1.add_vertex((998, 552))
    b1.add_vertex((955, 616))
    b1.add_vertex((765, 641))
    b1.add_vertex((516, 641))
    b1.add_vertex((516, 463))
    b1.add_vertex((551, 463))
    b1.add_vertex((547, 489))
    b1.add_vertex((528, 579))
    b1.add_vertex((540, 641))
    b1.add_vertex((621, 641))
    b1.add_vertex((647, 500))
    b1.filled = True
    b1.fill_color = '#22252C'
    b1.color = '#22252C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((730, 510))
    b1.add_vertex((729, 516))
    b1.add_vertex((713, 551))
    b1.add_vertex((704, 570))
    b1.add_vertex((674, 542))
    b1.add_vertex((667, 532))
    b1.add_vertex((665, 525))
    b1.add_vertex((700, 499))
    b1.filled = True
    b1.fill_color = '#99958C'
    b1.color = '#99958C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((736, 487))
    b1.add_vertex((735, 499))
    b1.add_vertex((730, 510))
    b1.add_vertex((724, 506))
    b1.add_vertex((722, 516))
    b1.add_vertex((715, 512))
    b1.add_vertex((717, 552))
    b1.add_vertex((720, 519))
    b1.add_vertex((729, 517))
    b1.add_vertex((724, 531))
    b1.add_vertex((716, 532))
    b1.add_vertex((710, 531))
    b1.add_vertex((709, 524))
    b1.add_vertex((705, 526))
    b1.add_vertex((697, 538))
    b1.add_vertex((696, 544))
    b1.add_vertex((690, 543))
    b1.add_vertex((692, 538))
    b1.add_vertex((687, 542))
    b1.add_vertex((677, 535))
    b1.add_vertex((680, 529))
    b1.add_vertex((671, 528))
    b1.add_vertex((673, 513))
    b1.add_vertex((736, 483))
    b1.filled = True
    b1.fill_color = '#D0C7C0'
    b1.color = '#D0C7C0'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((726, 525))
    b1.add_vertex((714, 534))
    b1.add_vertex((710, 533))
    b1.add_vertex((711, 539))
    b1.add_vertex((705, 535))
    b1.add_vertex((698, 540))
    b1.add_vertex((701, 540))
    b1.add_vertex((702, 545))
    b1.add_vertex((713, 553))
    b1.add_vertex((720, 540))
    b1.filled = True
    b1.fill_color = '#A59E96'
    b1.color = '#A59E96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((736, 486))
    b1.add_vertex((712, 503))
    b1.add_vertex((685, 515))
    b1.add_vertex((666, 522))
    b1.add_vertex((663, 518))
    b1.add_vertex((667, 514))
    b1.add_vertex((661, 512))
    b1.add_vertex((653, 508))
    b1.add_vertex((660, 510))
    b1.add_vertex((687, 499))
    b1.add_vertex((713, 491))
    b1.add_vertex((730, 481))
    b1.filled = True
    b1.fill_color = '#675D5B'
    b1.color = '#675D5B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((802, 547))
    b1.add_vertex((815, 532))
    b1.add_vertex((824, 529))
    b1.add_vertex((829, 508))
    b1.add_vertex((818, 494))
    b1.add_vertex((746, 530))
    b1.add_vertex((734, 531))
    b1.add_vertex((748, 549))
    b1.add_vertex((738, 552))
    b1.add_vertex((757, 559))
    b1.add_vertex((771, 541))
    b1.add_vertex((773, 557))
    b1.add_vertex((802, 530))
    b1.filled = True
    b1.fill_color = '#3C404B'
    b1.color = '#3C404B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((761, 550))
    b1.add_vertex((789, 514))
    b1.add_vertex((794, 519))
    b1.add_vertex((801, 504))
    b1.add_vertex((795, 476))
    b1.add_vertex((799, 470))
    b1.add_vertex((791, 471))
    b1.add_vertex((795, 467))
    b1.add_vertex((778, 463))
    b1.add_vertex((756, 473))
    b1.add_vertex((737, 489))
    b1.add_vertex((736, 494))
    b1.add_vertex((751, 497))
    b1.add_vertex((737, 512))
    b1.add_vertex((738, 518))
    b1.add_vertex((731, 524))
    b1.add_vertex((760, 538))
    b1.filled = True
    b1.fill_color = '#454348'
    b1.color = '#454348'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((778, 520))
    b1.add_vertex((786, 499))
    b1.add_vertex((793, 498))
    b1.add_vertex((786, 489))
    b1.add_vertex((787, 480))
    b1.add_vertex((775, 479))
    b1.add_vertex((768, 477))
    b1.add_vertex((768, 472))
    b1.add_vertex((759, 473))
    b1.add_vertex((749, 479))
    b1.add_vertex((742, 491))
    b1.add_vertex((746, 504))
    b1.add_vertex((751, 511))
    b1.add_vertex((749, 516))
    b1.add_vertex((760, 518))
    b1.filled = True
    b1.fill_color = '#63585E'
    b1.color = '#63585E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((717, 499))
    b1.add_vertex((739, 483))
    b1.add_vertex((765, 469))
    b1.add_vertex((779, 462))
    b1.add_vertex((776, 457))
    b1.add_vertex((767, 457))
    b1.add_vertex((749, 469))
    b1.add_vertex((747, 464))
    b1.add_vertex((735, 471))
    b1.add_vertex((743, 474))
    b1.add_vertex((728, 483))
    b1.add_vertex((729, 488))
    b1.add_vertex((726, 492))
    b1.add_vertex((724, 487))
    b1.add_vertex((716, 495))
    b1.add_vertex((718, 499))
    b1.filled = True
    b1.fill_color = '#AE968C'
    b1.color = '#AE968C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((705, 496))
    b1.add_vertex((691, 499))
    b1.add_vertex((677, 506))
    b1.add_vertex((682, 514))
    b1.add_vertex((688, 505))
    b1.add_vertex((705, 506))
    b1.filled = True
    b1.fill_color = '#AE968C'
    b1.color = '#AE968C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((747, 498))
    b1.add_vertex((742, 491))
    b1.add_vertex((765, 475))
    b1.add_vertex((773, 479))
    b1.filled = True
    b1.fill_color = '#AE968C'
    b1.color = '#AE968C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((767, 373))
    b1.add_vertex((763, 373))
    b1.add_vertex((762, 374))
    b1.filled = True
    b1.fill_color = '#AD9C95'
    b1.color = '#AD9C95'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((771, 506))
    b1.add_vertex((777, 495))
    b1.add_vertex((769, 487))
    b1.add_vertex((764, 489))
    b1.add_vertex((761, 495))
    b1.add_vertex((763, 502))
    b1.add_vertex((767, 505))
    b1.add_vertex((769, 503))
    b1.filled = True
    b1.fill_color = '#887A79'
    b1.color = '#887A79'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((803, 518))
    b1.add_vertex((814, 508))
    b1.add_vertex((815, 491))
    b1.add_vertex((804, 478))
    b1.add_vertex((791, 476))
    b1.add_vertex((800, 493))
    b1.filled = True
    b1.fill_color = '#525156'
    b1.color = '#525156'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((843, 482))
    b1.add_vertex((847, 455))
    b1.add_vertex((839, 450))
    b1.add_vertex((836, 444))
    b1.add_vertex((835, 436))
    b1.add_vertex((827, 434))
    b1.add_vertex((833, 437))
    b1.add_vertex((835, 444))
    b1.add_vertex((821, 441))
    b1.add_vertex((832, 455))
    b1.filled = True
    b1.fill_color = '#6A6561'
    b1.color = '#6A6561'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((853, 494))
    b1.add_vertex((853, 485))
    b1.add_vertex((850, 478))
    b1.add_vertex((852, 469))
    b1.add_vertex((847, 456))
    b1.add_vertex((844, 455))
    b1.add_vertex((844, 496))
    b1.add_vertex((847, 502))
    b1.add_vertex((848, 497))
    b1.add_vertex((846, 480))
    b1.add_vertex((851, 495))
    b1.filled = True
    b1.fill_color = '#AB979A'
    b1.color = '#AB979A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((953, 489))
    b1.add_vertex((939, 465))
    b1.add_vertex((957, 481))
    b1.add_vertex((957, 470))
    b1.add_vertex((947, 455))
    b1.add_vertex((952, 453))
    b1.add_vertex((938, 435))
    b1.add_vertex((920, 421))
    b1.add_vertex((920, 425))
    b1.add_vertex((894, 413))
    b1.add_vertex((912, 438))
    b1.add_vertex((934, 464))
    b1.filled = True
    b1.fill_color = '#AB979A'
    b1.color = '#AB979A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((647, 527))
    b1.add_vertex((644, 577))
    b1.add_vertex((636, 611))
    b1.add_vertex((620, 629))
    b1.add_vertex((590, 641))
    b1.add_vertex((578, 613))
    b1.add_vertex((574, 551))
    b1.add_vertex((598, 514))
    b1.add_vertex((611, 496))
    b1.filled = True
    b1.fill_color = '#34373E'
    b1.color = '#34373E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((659, 446))
    b1.add_vertex((653, 471))
    b1.add_vertex((658, 479))
    b1.add_vertex((658, 491))
    b1.add_vertex((652, 500))
    b1.add_vertex((653, 511))
    b1.add_vertex((647, 524))
    b1.add_vertex((647, 531))
    b1.add_vertex((627, 557))
    b1.add_vertex((618, 573))
    b1.add_vertex((602, 548))
    b1.add_vertex((625, 479))
    b1.add_vertex((650, 434))
    b1.filled = True
    b1.fill_color = '#899392'
    b1.color = '#899392'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((658, 477))
    b1.add_vertex((655, 473))
    b1.add_vertex((661, 467))
    b1.add_vertex((660, 458))
    b1.add_vertex((668, 442))
    b1.add_vertex((667, 430))
    b1.add_vertex((649, 432))
    b1.add_vertex((609, 499))
    b1.add_vertex((596, 586))
    b1.add_vertex((608, 641))
    b1.add_vertex((622, 622))
    b1.add_vertex((617, 616))
    b1.add_vertex((619, 606))
    b1.add_vertex((614, 590))
    b1.add_vertex((610, 598))
    b1.add_vertex((614, 584))
    b1.add_vertex((618, 572))
    b1.add_vertex((615, 571))
    b1.add_vertex((614, 557))
    b1.add_vertex((612, 554))
    b1.add_vertex((616, 532))
    b1.add_vertex((612, 528))
    b1.add_vertex((630, 473))
    b1.add_vertex((648, 450))
    b1.add_vertex((641, 477))
    b1.add_vertex((642, 508))
    b1.add_vertex((636, 517))
    b1.add_vertex((628, 532))
    b1.add_vertex((642, 519))
    b1.add_vertex((650, 470))
    b1.add_vertex((651, 455))
    b1.add_vertex((659, 446))
    b1.add_vertex((653, 473))
    b1.filled = True
    b1.fill_color = '#656E73'
    b1.color = '#656E73'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((685, 430))
    b1.add_vertex((670, 430))
    b1.add_vertex((671, 426))
    b1.add_vertex((661, 425))
    b1.add_vertex((649, 419))
    b1.add_vertex((644, 441))
    b1.add_vertex((632, 467))
    b1.add_vertex((624, 478))
    b1.add_vertex((618, 505))
    b1.add_vertex((633, 469))
    b1.add_vertex((650, 440))
    b1.add_vertex((650, 453))
    b1.add_vertex((655, 438))
    b1.add_vertex((662, 442))
    b1.add_vertex((666, 437))
    b1.filled = True
    b1.fill_color = '#535C63'
    b1.color = '#535C63'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((647, 537))
    b1.add_vertex((639, 548))
    b1.add_vertex((621, 599))
    b1.add_vertex((637, 582))
    b1.add_vertex((636, 576))
    b1.add_vertex((644, 566))
    b1.add_vertex((642, 551))
    b1.add_vertex((647, 539))
    b1.filled = True
    b1.fill_color = '#535C63'
    b1.color = '#535C63'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((608, 641))
    b1.add_vertex((601, 612))
    b1.add_vertex((604, 584))
    b1.add_vertex((597, 597))
    b1.add_vertex((600, 575))
    b1.add_vertex((603, 528))
    b1.add_vertex((587, 541))
    b1.add_vertex((581, 563))
    b1.add_vertex((584, 579))
    b1.add_vertex((588, 597))
    b1.add_vertex((599, 552))
    b1.add_vertex((595, 593))
    b1.add_vertex((583, 608))
    b1.add_vertex((585, 611))
    b1.add_vertex((592, 602))
    b1.add_vertex((588, 626))
    b1.add_vertex((592, 641))
    b1.filled = True
    b1.fill_color = '#585B62'
    b1.color = '#585B62'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((584, 538))
    b1.add_vertex((579, 563))
    b1.add_vertex((581, 583))
    b1.add_vertex((582, 581))
    b1.add_vertex((585, 595))
    b1.add_vertex((579, 606))
    b1.add_vertex((579, 600))
    b1.add_vertex((575, 606))
    b1.add_vertex((569, 596))
    b1.add_vertex((565, 569))
    b1.add_vertex((560, 572))
    b1.add_vertex((571, 554))
    b1.filled = True
    b1.fill_color = '#696E60'
    b1.color = '#696E60'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((571, 641))
    b1.add_vertex((575, 601))
    b1.add_vertex((571, 602))
    b1.add_vertex((568, 585))
    b1.add_vertex((565, 568))
    b1.add_vertex((557, 577))
    b1.add_vertex((528, 590))
    b1.add_vertex((516, 603))
    b1.add_vertex((516, 620))
    b1.add_vertex((531, 606))
    b1.add_vertex((541, 627))
    b1.add_vertex((554, 641))
    b1.filled = True
    b1.fill_color = '#787272'
    b1.color = '#787272'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((597, 513))
    b1.add_vertex((590, 528))
    b1.add_vertex((569, 556))
    b1.add_vertex((554, 588))
    b1.add_vertex((551, 592))
    b1.add_vertex((530, 590))
    b1.add_vertex((527, 574))
    b1.add_vertex((529, 556))
    b1.add_vertex((516, 572))
    b1.add_vertex((516, 554))
    b1.add_vertex((535, 536))
    b1.add_vertex((539, 515))
    b1.add_vertex((527, 529))
    b1.add_vertex((531, 520))
    b1.add_vertex((542, 501))
    b1.add_vertex((562, 490))
    b1.add_vertex((547, 505))
    b1.add_vertex((571, 489))
    b1.add_vertex((550, 521))
    b1.add_vertex((550, 527))
    b1.add_vertex((562, 514))
    b1.add_vertex((552, 533))
    b1.add_vertex((564, 549))
    b1.filled = True
    b1.fill_color = '#A6A19D'
    b1.color = '#A6A19D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((561, 611))
    b1.add_vertex((551, 606))
    b1.add_vertex((555, 570))
    b1.add_vertex((547, 588))
    b1.add_vertex((541, 574))
    b1.add_vertex((540, 551))
    b1.add_vertex((537, 569))
    b1.add_vertex((537, 590))
    b1.add_vertex((527, 573))
    b1.add_vertex((536, 548))
    b1.add_vertex((528, 557))
    b1.add_vertex((526, 577))
    b1.add_vertex((539, 604))
    b1.add_vertex((547, 613))
    b1.add_vertex((549, 610))
    b1.filled = True
    b1.fill_color = '#8F8A86'
    b1.color = '#8F8A86'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((869, 437))
    b1.add_vertex((888, 459))
    b1.add_vertex((901, 495))
    b1.add_vertex((885, 513))
    b1.add_vertex((862, 492))
    b1.add_vertex((853, 466))
    b1.add_vertex((849, 455))
    b1.add_vertex((860, 448))
    b1.add_vertex((866, 457))
    b1.add_vertex((870, 453))
    b1.add_vertex((867, 445))
    b1.filled = True
    b1.fill_color = '#CEB8AD'
    b1.color = '#CEB8AD'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((806, 468))
    b1.add_vertex((816, 462))
    b1.add_vertex((821, 454))
    b1.add_vertex((817, 449))
    b1.add_vertex((809, 448))
    b1.add_vertex((805, 450))
    b1.filled = True
    b1.fill_color = '#584D4B'
    b1.color = '#584D4B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((821, 480))
    b1.add_vertex((826, 472))
    b1.add_vertex((819, 468))
    b1.add_vertex((816, 473))
    b1.add_vertex((819, 479))
    b1.filled = True
    b1.fill_color = '#584D4B'
    b1.color = '#584D4B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((888, 460))
    b1.add_vertex((899, 471))
    b1.add_vertex((912, 507))
    b1.add_vertex((905, 532))
    b1.add_vertex((881, 509))
    b1.add_vertex((897, 490))
    b1.add_vertex((894, 476))
    b1.filled = True
    b1.fill_color = '#BCA59F'
    b1.color = '#BCA59F'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((702, 570))
    b1.add_vertex((663, 641))
    b1.add_vertex((642, 639))
    b1.add_vertex((652, 615))
    b1.add_vertex((662, 605))
    b1.add_vertex((664, 611))
    b1.add_vertex((667, 608))
    b1.add_vertex((662, 586))
    b1.add_vertex((663, 578))
    b1.add_vertex((669, 580))
    b1.add_vertex((662, 558))
    b1.add_vertex((645, 576))
    b1.add_vertex((649, 568))
    b1.add_vertex((644, 562))
    b1.add_vertex((646, 554))
    b1.add_vertex((650, 548))
    b1.add_vertex((648, 564))
    b1.add_vertex((660, 554))
    b1.add_vertex((654, 548))
    b1.add_vertex((657, 543))
    b1.add_vertex((689, 548))
    b1.add_vertex((696, 556))
    b1.add_vertex((700, 548))
    b1.add_vertex((704, 557))
    b1.add_vertex((699, 560))
    b1.filled = True
    b1.fill_color = '#82756D'
    b1.color = '#82756D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((703, 574))
    b1.add_vertex((695, 587))
    b1.add_vertex((688, 570))
    b1.add_vertex((695, 562))
    b1.filled = True
    b1.fill_color = '#A48C74'
    b1.color = '#A48C74'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((690, 561))
    b1.add_vertex((684, 568))
    b1.add_vertex((678, 562))
    b1.add_vertex((671, 562))
    b1.add_vertex((647, 583))
    b1.add_vertex((639, 582))
    b1.add_vertex((641, 578))
    b1.add_vertex((651, 575))
    b1.add_vertex((658, 561))
    b1.add_vertex((648, 566))
    b1.add_vertex((668, 552))
    b1.add_vertex((676, 548))
    b1.add_vertex((678, 545))
    b1.add_vertex((684, 545))
    b1.add_vertex((683, 552))
    b1.filled = True
    b1.fill_color = '#A48C74'
    b1.color = '#A48C74'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((880, 511))
    b1.add_vertex((857, 490))
    b1.add_vertex((853, 479))
    b1.add_vertex((854, 473))
    b1.add_vertex((854, 478))
    b1.add_vertex((857, 494))
    b1.add_vertex((872, 512))
    b1.filled = True
    b1.fill_color = '#504F55'
    b1.color = '#504F55'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((860, 504))
    b1.add_vertex((873, 519))
    b1.add_vertex((914, 555))
    b1.add_vertex((957, 554))
    b1.add_vertex((963, 560))
    b1.add_vertex((962, 641))
    b1.add_vertex((933, 641))
    b1.add_vertex((900, 612))
    b1.add_vertex((887, 592))
    b1.add_vertex((890, 585))
    b1.add_vertex((870, 571))
    b1.add_vertex((861, 558))
    b1.add_vertex((856, 543))
    b1.add_vertex((856, 531))
    b1.filled = True
    b1.fill_color = '#504F55'
    b1.color = '#504F55'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((679, 571))
    b1.add_vertex((676, 562))
    b1.add_vertex((668, 567))
    b1.add_vertex((664, 579))
    b1.add_vertex((660, 587))
    b1.add_vertex((668, 605))
    b1.add_vertex((674, 603))
    b1.add_vertex((674, 589))
    b1.add_vertex((666, 577))
    b1.add_vertex((672, 570))
    b1.filled = True
    b1.fill_color = '#555450'
    b1.color = '#555450'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((649, 641))
    b1.add_vertex((650, 622))
    b1.add_vertex((661, 621))
    b1.add_vertex((666, 614))
    b1.add_vertex((652, 618))
    b1.add_vertex((648, 624))
    b1.add_vertex((642, 641))
    b1.filled = True
    b1.fill_color = '#555450'
    b1.color = '#555450'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((943, 530))
    b1.add_vertex((948, 577))
    b1.add_vertex((933, 608))
    b1.add_vertex((924, 614))
    b1.add_vertex((886, 592))
    b1.add_vertex((894, 608))
    b1.add_vertex((877, 594))
    b1.add_vertex((873, 579))
    b1.add_vertex((886, 585))
    b1.add_vertex((880, 579))
    b1.add_vertex((912, 598))
    b1.add_vertex((921, 594))
    b1.add_vertex((929, 567))
    b1.add_vertex((935, 550))
    b1.filled = True
    b1.fill_color = '#34353A'
    b1.color = '#34353A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((925, 500))
    b1.add_vertex((939, 520))
    b1.add_vertex((943, 529))
    b1.add_vertex((941, 541))
    b1.add_vertex((929, 569))
    b1.add_vertex((929, 577))
    b1.add_vertex((926, 585))
    b1.add_vertex((920, 579))
    b1.add_vertex((916, 585))
    b1.add_vertex((882, 569))
    b1.add_vertex((865, 562))
    b1.add_vertex((866, 553))
    b1.add_vertex((874, 559))
    b1.add_vertex((883, 560))
    b1.add_vertex((882, 546))
    b1.add_vertex((870, 526))
    b1.add_vertex((881, 537))
    b1.add_vertex((890, 540))
    b1.add_vertex((890, 534))
    b1.add_vertex((905, 549))
    b1.add_vertex((917, 563))
    b1.add_vertex((918, 554))
    b1.add_vertex((923, 553))
    b1.add_vertex((926, 532))
    b1.add_vertex((926, 514))
    b1.filled = True
    b1.fill_color = '#424146'
    b1.color = '#424146'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((870, 527))
    b1.add_vertex((862, 513))
    b1.add_vertex((857, 502))
    b1.add_vertex((854, 532))
    b1.add_vertex((856, 544))
    b1.add_vertex((857, 528))
    b1.add_vertex((862, 542))
    b1.add_vertex((861, 527))
    b1.add_vertex((864, 521))
    b1.filled = True
    b1.fill_color = '#34353A'
    b1.color = '#34353A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((922, 555))
    b1.add_vertex((911, 540))
    b1.add_vertex((904, 530))
    b1.add_vertex((903, 535))
    b1.add_vertex((893, 527))
    b1.add_vertex((892, 522))
    b1.add_vertex((878, 509))
    b1.add_vertex((878, 516))
    b1.add_vertex((859, 496))
    b1.add_vertex((859, 500))
    b1.add_vertex((871, 516))
    b1.add_vertex((890, 534))
    b1.add_vertex((910, 553))
    b1.add_vertex((921, 565))
    b1.add_vertex((916, 556))
    b1.filled = True
    b1.fill_color = '#34353A'
    b1.color = '#34353A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((888, 449))
    b1.add_vertex((912, 473))
    b1.add_vertex((946, 553))
    b1.add_vertex((1002, 504))
    b1.add_vertex((917, 454))
    b1.filled = True
    b1.fill_color = '#9D8B87'
    b1.color = '#9D8B87'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((973, 535))
    b1.add_vertex((983, 565))
    b1.add_vertex((1008, 618))
    b1.add_vertex((1008, 641))
    b1.add_vertex((894, 641))
    b1.add_vertex((892, 602))
    b1.add_vertex((910, 618))
    b1.add_vertex((935, 641))
    b1.add_vertex((960, 641))
    b1.add_vertex((964, 597))
    b1.add_vertex((962, 557))
    b1.add_vertex((951, 541))
    b1.filled = True
    b1.fill_color = '#2B2C31'
    b1.color = '#2B2C31'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((829, 557))
    b1.add_vertex((823, 555))
    b1.add_vertex((818, 533))
    b1.add_vertex((818, 526))
    b1.add_vertex((825, 529))
    b1.add_vertex((837, 529))
    b1.add_vertex((843, 565))
    b1.filled = True
    b1.fill_color = '#8B786D'
    b1.color = '#8B786D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((739, 565))
    b1.add_vertex((735, 582))
    b1.add_vertex((727, 578))
    b1.add_vertex((726, 594))
    b1.add_vertex((749, 605))
    b1.add_vertex((778, 612))
    b1.add_vertex((767, 596))
    b1.add_vertex((764, 595))
    b1.add_vertex((761, 591))
    b1.add_vertex((748, 587))
    b1.add_vertex((749, 577))
    b1.add_vertex((751, 570))
    b1.filled = True
    b1.fill_color = '#8B786D'
    b1.color = '#8B786D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((861, 641))
    b1.add_vertex((859, 631))
    b1.add_vertex((855, 629))
    b1.add_vertex((846, 608))
    b1.add_vertex((834, 581))
    b1.add_vertex((828, 581))
    b1.add_vertex((824, 575))
    b1.add_vertex((825, 565))
    b1.add_vertex((827, 557))
    b1.add_vertex((835, 556))
    b1.add_vertex((853, 559))
    b1.add_vertex((863, 584))
    b1.add_vertex((882, 641))
    b1.filled = True
    b1.fill_color = '#948B86'
    b1.color = '#948B86'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((741, 641))
    b1.add_vertex((741, 624))
    b1.add_vertex((729, 599))
    b1.add_vertex((721, 594))
    b1.add_vertex((704, 591))
    b1.add_vertex((682, 641))
    b1.filled = True
    b1.fill_color = '#5D5B5E'
    b1.color = '#5D5B5E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((707, 641))
    b1.add_vertex((710, 625))
    b1.add_vertex((703, 610))
    b1.add_vertex((696, 624))
    b1.add_vertex((692, 623))
    b1.add_vertex((699, 605))
    b1.add_vertex((691, 587))
    b1.add_vertex((676, 597))
    b1.add_vertex((679, 602))
    b1.add_vertex((670, 627))
    b1.add_vertex((685, 620))
    b1.add_vertex((674, 641))
    b1.filled = True
    b1.fill_color = '#4C4B50'
    b1.color = '#4C4B50'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((724, 616))
    b1.add_vertex((723, 606))
    b1.add_vertex((726, 604))
    b1.add_vertex((719, 596))
    b1.add_vertex((727, 593))
    b1.add_vertex((714, 564))
    b1.add_vertex((715, 554))
    b1.add_vertex((704, 571))
    b1.add_vertex((704, 575))
    b1.add_vertex((699, 580))
    b1.add_vertex((696, 587))
    b1.add_vertex((691, 583))
    b1.add_vertex((675, 595))
    b1.add_vertex((675, 599))
    b1.add_vertex((690, 590))
    b1.add_vertex((692, 594))
    b1.add_vertex((678, 604))
    b1.add_vertex((676, 610))
    b1.add_vertex((683, 604))
    b1.add_vertex((690, 603))
    b1.add_vertex((685, 615))
    b1.add_vertex((696, 602))
    b1.add_vertex((692, 620))
    b1.add_vertex((701, 601))
    b1.add_vertex((703, 593))
    b1.add_vertex((708, 592))
    b1.add_vertex((712, 603))
    b1.add_vertex((717, 604))
    b1.filled = True
    b1.fill_color = '#343338'
    b1.color = '#343338'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((779, 641))
    b1.add_vertex((770, 616))
    b1.add_vertex((763, 616))
    b1.add_vertex((765, 641))
    b1.add_vertex((762, 641))
    b1.add_vertex((760, 623))
    b1.add_vertex((756, 618))
    b1.add_vertex((753, 619))
    b1.add_vertex((751, 625))
    b1.add_vertex((760, 641))
    b1.filled = True
    b1.fill_color = '#3E4653'
    b1.color = '#3E4653'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((624, 641))
    b1.add_vertex((636, 618))
    b1.add_vertex((640, 600))
    b1.add_vertex((624, 622))
    b1.add_vertex((607, 641))
    b1.filled = True
    b1.fill_color = '#3E4653'
    b1.color = '#3E4653'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((811, 582))
    b1.add_vertex((823, 641))
    b1.add_vertex((779, 641))
    b1.add_vertex((771, 612))
    b1.add_vertex((777, 610))
    b1.add_vertex((770, 602))
    b1.add_vertex((774, 591))
    b1.filled = True
    b1.fill_color = '#C8BFB8'
    b1.color = '#C8BFB8'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((813, 612))
    b1.add_vertex((814, 571))
    b1.add_vertex((798, 577))
    b1.add_vertex((769, 590))
    b1.add_vertex((767, 597))
    b1.add_vertex((774, 606))
    b1.add_vertex((777, 592))
    b1.add_vertex((791, 591))
    b1.add_vertex((775, 607))
    b1.add_vertex((778, 608))
    b1.add_vertex((772, 610))
    b1.add_vertex((773, 620))
    b1.add_vertex((782, 608))
    b1.add_vertex((795, 590))
    b1.add_vertex((800, 588))
    b1.add_vertex((803, 582))
    b1.add_vertex((803, 593))
    b1.add_vertex((810, 584))
    b1.add_vertex((811, 604))
    b1.filled = True
    b1.fill_color = '#95908C'
    b1.color = '#95908C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((817, 641))
    b1.add_vertex((818, 620))
    b1.add_vertex((814, 602))
    b1.add_vertex((812, 622))
    b1.add_vertex((809, 611))
    b1.add_vertex((800, 627))
    b1.add_vertex((794, 641))
    b1.add_vertex((784, 641))
    b1.add_vertex((791, 628))
    b1.add_vertex((792, 616))
    b1.add_vertex((782, 623))
    b1.add_vertex((776, 631))
    b1.add_vertex((778, 641))
    b1.filled = True
    b1.fill_color = '#B8AEAC'
    b1.color = '#B8AEAC'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((824, 641))
    b1.add_vertex((818, 622))
    b1.add_vertex((818, 603))
    b1.add_vertex((813, 597))
    b1.add_vertex((817, 589))
    b1.add_vertex((820, 594))
    b1.add_vertex((819, 571))
    b1.add_vertex((823, 567))
    b1.add_vertex((822, 578))
    b1.add_vertex((826, 599))
    b1.add_vertex((838, 641))
    b1.filled = True
    b1.fill_color = '#54575C'
    b1.color = '#54575C'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((838, 641))
    b1.add_vertex((837, 627))
    b1.add_vertex((842, 634))
    b1.add_vertex((839, 617))
    b1.add_vertex((834, 603))
    b1.add_vertex((826, 599))
    b1.add_vertex((832, 620))
    b1.add_vertex((827, 621))
    b1.add_vertex((829, 641))
    b1.filled = True
    b1.fill_color = '#414852'
    b1.color = '#414852'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((878, 641))
    b1.add_vertex((867, 618))
    b1.add_vertex((871, 611))
    b1.add_vertex((869, 601))
    b1.add_vertex((865, 607))
    b1.add_vertex((861, 600))
    b1.add_vertex((862, 594))
    b1.add_vertex((860, 590))
    b1.add_vertex((861, 588))
    b1.add_vertex((857, 582))
    b1.add_vertex((852, 576))
    b1.add_vertex((843, 573))
    b1.add_vertex((850, 559))
    b1.add_vertex((855, 559))
    b1.add_vertex((855, 565))
    b1.add_vertex((861, 570))
    b1.add_vertex((863, 583))
    b1.add_vertex((876, 597))
    b1.add_vertex((879, 610))
    b1.add_vertex((903, 641))
    b1.filled = True
    b1.fill_color = '#74706F'
    b1.color = '#74706F'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((910, 641))
    b1.add_vertex((902, 620))
    b1.add_vertex((886, 606))
    b1.add_vertex((888, 614))
    b1.add_vertex((884, 610))
    b1.add_vertex((879, 608))
    b1.add_vertex((879, 620))
    b1.add_vertex((880, 612))
    b1.add_vertex((890, 622))
    b1.add_vertex((885, 625))
    b1.add_vertex((894, 628))
    b1.add_vertex((897, 641))
    b1.filled = True
    b1.fill_color = '#615851'
    b1.color = '#615851'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((849, 641))
    b1.add_vertex((851, 633))
    b1.add_vertex((859, 637))
    b1.add_vertex((860, 641))
    b1.filled = True
    b1.fill_color = '#586E7B'
    b1.color = '#586E7B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((845, 618))
    b1.add_vertex((845, 614))
    b1.add_vertex((840, 613))
    b1.add_vertex((838, 608))
    b1.add_vertex((836, 609))
    b1.add_vertex((840, 616))
    b1.filled = True
    b1.fill_color = '#586E7B'
    b1.color = '#586E7B'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((849, 568))
    b1.add_vertex((849, 558))
    b1.add_vertex((852, 557))
    b1.add_vertex((848, 549))
    b1.add_vertex((849, 537))
    b1.add_vertex((843, 533))
    b1.add_vertex((843, 527))
    b1.add_vertex((844, 517))
    b1.add_vertex((837, 527))
    b1.add_vertex((831, 527))
    b1.add_vertex((831, 533))
    b1.add_vertex((840, 528))
    b1.add_vertex((836, 534))
    b1.add_vertex((831, 539))
    b1.add_vertex((822, 535))
    b1.add_vertex((824, 539))
    b1.add_vertex((825, 537))
    b1.add_vertex((831, 539))
    b1.add_vertex((825, 544))
    b1.add_vertex((829, 552))
    b1.add_vertex((833, 552))
    b1.add_vertex((829, 557))
    b1.add_vertex((835, 559))
    b1.add_vertex((840, 552))
    b1.add_vertex((836, 560))
    b1.add_vertex((839, 563))
    b1.add_vertex((839, 553))
    b1.add_vertex((841, 555))
    b1.add_vertex((843, 565))
    b1.filled = True
    b1.fill_color = '#50473E'
    b1.color = '#50473E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((814, 574))
    b1.add_vertex((804, 553))
    b1.add_vertex((792, 553))
    b1.add_vertex((773, 564))
    b1.add_vertex((756, 563))
    b1.add_vertex((746, 561))
    b1.add_vertex((739, 562))
    b1.add_vertex((745, 567))
    b1.add_vertex((753, 570))
    b1.add_vertex((764, 571))
    b1.add_vertex((784, 569))
    b1.add_vertex((782, 575))
    b1.add_vertex((787, 575))
    b1.add_vertex((789, 568))
    b1.add_vertex((793, 573))
    b1.add_vertex((803, 572))
    b1.add_vertex((809, 567))
    b1.add_vertex((812, 559))
    b1.add_vertex((808, 556))
    b1.add_vertex((815, 549))
    b1.filled = True
    b1.fill_color = '#56514E'
    b1.color = '#56514E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((782, 566))
    b1.add_vertex((773, 562))
    b1.add_vertex((766, 563))
    b1.add_vertex((763, 571))
    b1.add_vertex((755, 568))
    b1.add_vertex((750, 576))
    b1.add_vertex((771, 582))
    b1.add_vertex((769, 574))
    b1.add_vertex((765, 571))
    b1.filled = True
    b1.fill_color = '#7E8889'
    b1.color = '#7E8889'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((730, 583))
    b1.add_vertex((724, 591))
    b1.add_vertex((721, 584))
    b1.add_vertex((723, 580))
    b1.add_vertex((718, 574))
    b1.add_vertex((724, 565))
    b1.add_vertex((723, 563))
    b1.add_vertex((717, 573))
    b1.add_vertex((714, 564))
    b1.add_vertex((716, 553))
    b1.add_vertex((720, 547))
    b1.add_vertex((726, 566))
    b1.add_vertex((724, 575))
    b1.filled = True
    b1.fill_color = '#606568'
    b1.color = '#606568'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((539, 516))
    b1.add_vertex((516, 528))
    b1.add_vertex((516, 556))
    b1.add_vertex((537, 535))
    b1.filled = True
    b1.fill_color = '#8F8A86'
    b1.color = '#8F8A86'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((769, 584))
    b1.add_vertex((758, 584))
    b1.add_vertex((747, 582))
    b1.add_vertex((748, 577))
    b1.add_vertex((757, 572))
    b1.add_vertex((765, 577))
    b1.filled = True
    b1.fill_color = '#606568'
    b1.color = '#606568'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((719, 595))
    b1.add_vertex((722, 582))
    b1.add_vertex((714, 572))
    b1.add_vertex((712, 576))
    b1.add_vertex((708, 580))
    b1.add_vertex((705, 590))
    b1.filled = True
    b1.fill_color = '#7E8889'
    b1.color = '#7E8889'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((851, 584))
    b1.add_vertex((849, 572))
    b1.add_vertex((843, 575))
    b1.add_vertex((844, 580))
    b1.filled = True
    b1.fill_color = '#4A4240'
    b1.color = '#4A4240'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((839, 571))
    b1.add_vertex((837, 574))
    b1.add_vertex((833, 574))
    b1.add_vertex((831, 570))
    b1.add_vertex((833, 565))
    b1.filled = True
    b1.fill_color = '#4A4240'
    b1.color = '#4A4240'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((869, 629))
    b1.add_vertex((868, 618))
    b1.add_vertex((865, 621))
    b1.add_vertex((858, 614))
    b1.add_vertex((849, 606))
    b1.add_vertex((851, 621))
    b1.add_vertex((855, 622))
    b1.add_vertex((853, 626))
    b1.add_vertex((861, 627))
    b1.add_vertex((863, 625))
    b1.filled = True
    b1.fill_color = '#C7BEB7'
    b1.color = '#C7BEB7'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((590, 641))
    b1.add_vertex((575, 602))
    b1.add_vertex((574, 614))
    b1.add_vertex((571, 617))
    b1.add_vertex((572, 641))
    b1.filled = True
    b1.fill_color = '#A29791'
    b1.color = '#A29791'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((788, 294))
    b1.add_vertex((781, 277))
    b1.add_vertex((775, 267))
    b1.add_vertex((771, 254))
    b1.add_vertex((774, 275))
    b1.add_vertex((776, 273))
    b1.add_vertex((782, 282))
    b1.filled = True
    b1.fill_color = '#AC9D96'
    b1.color = '#AC9D96'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((956, 566))
    b1.add_vertex((955, 550))
    b1.add_vertex((945, 535))
    b1.add_vertex((947, 550))
    b1.filled = True
    b1.fill_color = '#615B5D'
    b1.color = '#615B5D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((922, 556))
    b1.add_vertex((927, 527))
    b1.add_vertex((925, 500))
    b1.add_vertex((917, 502))
    b1.add_vertex((918, 525))
    b1.filled = True
    b1.fill_color = '#615B5D'
    b1.color = '#615B5D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((920, 517))
    b1.add_vertex((924, 499))
    b1.add_vertex((937, 519))
    b1.add_vertex((924, 491))
    b1.add_vertex((921, 480))
    b1.add_vertex((912, 468))
    b1.add_vertex((901, 458))
    b1.add_vertex((888, 451))
    b1.add_vertex((896, 459))
    b1.add_vertex((916, 487))
    b1.filled = True
    b1.fill_color = '#8D7A73'
    b1.color = '#8D7A73'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((1039, 586))
    b1.add_vertex((1032, 596))
    b1.add_vertex((996, 621))
    b1.add_vertex((1001, 564))
    b1.add_vertex((1011, 561))
    b1.add_vertex((1005, 570))
    b1.add_vertex((1004, 601))
    b1.add_vertex((1016, 596))
    b1.add_vertex((1032, 585))
    b1.filled = True
    b1.fill_color = '#A39997'
    b1.color = '#A39997'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((1045, 641))
    b1.add_vertex((1049, 631))
    b1.add_vertex((1049, 618))
    b1.add_vertex((1058, 626))
    b1.add_vertex((1059, 635))
    b1.add_vertex((1063, 625))
    b1.add_vertex((1067, 618))
    b1.add_vertex((1068, 608))
    b1.add_vertex((1073, 614))
    b1.add_vertex((1071, 602))
    b1.add_vertex((1073, 602))
    b1.add_vertex((1069, 586))
    b1.add_vertex((1073, 584))
    b1.add_vertex((1073, 641))
    b1.filled = True
    b1.fill_color = '#BAB1AA'
    b1.color = '#BAB1AA'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((1050, 616))
    b1.add_vertex((1048, 599))
    b1.add_vertex((1051, 592))
    b1.add_vertex((1046, 584))
    b1.add_vertex((1040, 585))
    b1.add_vertex((1029, 597))
    b1.add_vertex((1021, 604))
    b1.add_vertex((1008, 604))
    b1.add_vertex((998, 622))
    b1.add_vertex((999, 602))
    b1.add_vertex((1001, 584))
    b1.add_vertex((1001, 565))
    b1.add_vertex((975, 581))
    b1.add_vertex((988, 601))
    b1.add_vertex((996, 623))
    b1.add_vertex((1006, 618))
    b1.add_vertex((1018, 609))
    b1.add_vertex((1017, 606))
    b1.add_vertex((1032, 597))
    b1.add_vertex((1040, 600))
    b1.add_vertex((1044, 604))
    b1.filled = True
    b1.fill_color = '#8C837E'
    b1.color = '#8C837E'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((614, 276))
    b1.add_vertex((604, 276))
    b1.add_vertex((589, 281))
    b1.add_vertex((590, 275))
    b1.add_vertex((592, 271))
    b1.add_vertex((580, 274))
    b1.add_vertex((583, 267))
    b1.add_vertex((586, 265))
    b1.add_vertex((582, 259))
    b1.add_vertex((586, 253))
    b1.add_vertex((594, 251))
    b1.add_vertex((601, 253))
    b1.add_vertex((601, 260))
    b1.add_vertex((614, 267))
    b1.filled = True
    b1.fill_color = '#3B414D'
    b1.color = '#3B414D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((609, 272))
    b1.add_vertex((595, 276))
    b1.add_vertex((593, 275))
    b1.add_vertex((591, 264))
    b1.add_vertex((595, 259))
    b1.add_vertex((589, 254))
    b1.add_vertex((597, 252))
    b1.add_vertex((601, 254))
    b1.add_vertex((598, 258))
    b1.add_vertex((597, 266))
    b1.add_vertex((600, 267))
    b1.add_vertex((602, 268))
    b1.filled = True
    b1.fill_color = '#8E989A'
    b1.color = '#8E989A'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((712, 149))
    b1.add_vertex((698, 153))
    b1.add_vertex((673, 156))
    b1.add_vertex((655, 166))
    b1.add_vertex((643, 174))
    b1.add_vertex((633, 171))
    b1.add_vertex((633, 174))
    b1.add_vertex((625, 171))
    b1.add_vertex((613, 166))
    b1.add_vertex((612, 168))
    b1.add_vertex((590, 160))
    b1.add_vertex((591, 100))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((855, 283))
    b1.add_vertex((857, 262))
    b1.add_vertex((877, 267))
    b1.add_vertex((891, 330))
    b1.add_vertex((855, 343))
    b1.filled = True
    b1.fill_color = '#BFB2AA'
    b1.color = '#BFB2AA'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((601, 343))
    b1.add_vertex((600, 375))
    b1.add_vertex((596, 402))
    b1.add_vertex((575, 456))
    b1.add_vertex((566, 466))
    b1.add_vertex((562, 475))
    b1.add_vertex((553, 483))
    b1.add_vertex((528, 524))
    b1.add_vertex((516, 498))
    b1.add_vertex((516, 450))
    b1.add_vertex((594, 355))
    b1.filled = True
    b1.fill_color = '#786B67'
    b1.color = '#786B67'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((575, 437))
    b1.add_vertex((555, 450))
    b1.add_vertex((538, 464))
    b1.add_vertex((531, 475))
    b1.add_vertex((550, 485))
    b1.add_vertex((561, 477))
    b1.add_vertex((562, 470))
    b1.add_vertex((567, 467))
    b1.add_vertex((562, 459))
    b1.add_vertex((592, 448))
    b1.add_vertex((568, 460))
    b1.add_vertex((572, 451))
    b1.add_vertex((570, 446))
    b1.filled = True
    b1.fill_color = '#585453'
    b1.color = '#585453'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((599, 374))
    b1.add_vertex((591, 393))
    b1.add_vertex((592, 396))
    b1.add_vertex((583, 410))
    b1.add_vertex((581, 406))
    b1.add_vertex((571, 412))
    b1.add_vertex((575, 416))
    b1.add_vertex((552, 432))
    b1.add_vertex((524, 451))
    b1.add_vertex((596, 369))
    b1.filled = True
    b1.fill_color = '#8A7F7D'
    b1.color = '#8A7F7D'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((516, 204))
    b1.add_vertex((563, 201))
    b1.add_vertex((572, 215))
    b1.add_vertex((577, 229))
    b1.add_vertex((581, 234))
    b1.add_vertex((584, 239))
    b1.add_vertex((586, 243))
    b1.add_vertex((588, 246))
    b1.add_vertex((591, 249))
    b1.add_vertex((587, 254))
    b1.add_vertex((587, 257))
    b1.add_vertex((583, 256))
    b1.add_vertex((584, 264))
    b1.add_vertex((582, 268))
    b1.add_vertex((581, 274))
    b1.add_vertex((584, 273))
    b1.add_vertex((588, 273))
    b1.add_vertex((589, 277))
    b1.add_vertex((588, 282))
    b1.add_vertex((598, 278))
    b1.add_vertex((607, 274))
    b1.add_vertex((604, 282))
    b1.add_vertex((604, 278))
    b1.add_vertex((595, 285))
    b1.add_vertex((592, 284))
    b1.add_vertex((592, 291))
    b1.add_vertex((584, 298))
    b1.add_vertex((580, 306))
    b1.add_vertex((584, 311))
    b1.add_vertex((588, 307))
    b1.add_vertex((590, 313))
    b1.add_vertex((595, 315))
    b1.add_vertex((588, 335))
    b1.add_vertex((591, 338))
    b1.add_vertex((601, 315))
    b1.add_vertex((600, 323))
    b1.add_vertex((600, 330))
    b1.add_vertex((593, 349))
    b1.add_vertex((588, 357))
    b1.add_vertex((594, 353))
    b1.add_vertex((601, 341))
    b1.add_vertex((599, 372))
    b1.add_vertex((586, 394))
    b1.add_vertex((568, 414))
    b1.add_vertex((544, 435))
    b1.add_vertex((524, 455))
    b1.add_vertex((520, 465))
    b1.add_vertex((516, 476))
    b1.add_vertex((519, 498))
    b1.add_vertex((521, 494))
    b1.add_vertex((528, 511))
    b1.add_vertex((525, 514))
    b1.add_vertex((529, 521))
    b1.add_vertex((523, 529))
    b1.add_vertex((519, 540))
    b1.add_vertex((516, 556))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((554, 641))
    b1.add_vertex((516, 641))
    b1.add_vertex((516, 621))
    b1.add_vertex((525, 615))
    b1.add_vertex((532, 606))
    b1.add_vertex((541, 625))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((516, 606))
    b1.add_vertex((529, 590))
    b1.add_vertex((528, 578))
    b1.add_vertex((529, 557))
    b1.add_vertex((522, 566))
    b1.add_vertex((516, 572))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((525, 544))
    b1.add_vertex((535, 533))
    b1.add_vertex((537, 524))
    b1.add_vertex((541, 514))
    b1.add_vertex((531, 522))
    b1.add_vertex((526, 533))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((545, 519))
    b1.add_vertex((551, 514))
    b1.add_vertex((562, 500))
    b1.add_vertex((549, 508))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((533, 502))
    b1.add_vertex((548, 485))
    b1.add_vertex((546, 469))
    b1.add_vertex((543, 465))
    b1.add_vertex((536, 469))
    b1.add_vertex((532, 477))
    b1.add_vertex((529, 494))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((596, 306))
    b1.add_vertex((603, 298))
    b1.add_vertex((597, 295))
    b1.add_vertex((595, 301))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((585, 306))
    b1.add_vertex((588, 300))
    b1.add_vertex((586, 302))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((810, 169))
    b1.add_vertex((807, 177))
    b1.add_vertex((824, 195))
    b1.add_vertex((837, 212))
    b1.add_vertex((849, 232))
    b1.add_vertex((857, 253))
    b1.add_vertex((863, 277))
    b1.add_vertex((871, 301))
    b1.add_vertex((871, 310))
    b1.add_vertex((867, 300))
    b1.add_vertex((865, 308))
    b1.add_vertex((864, 327))
    b1.add_vertex((868, 327))
    b1.add_vertex((863, 332))
    b1.add_vertex((861, 336))
    b1.add_vertex((858, 328))
    b1.add_vertex((851, 343))
    b1.add_vertex((861, 363))
    b1.add_vertex((873, 375))
    b1.add_vertex((883, 376))
    b1.add_vertex((869, 379))
    b1.add_vertex((858, 375))
    b1.add_vertex((867, 383))
    b1.add_vertex((880, 390))
    b1.add_vertex((892, 388))
    b1.add_vertex((898, 380))
    b1.add_vertex((898, 384))
    b1.add_vertex((902, 383))
    b1.add_vertex((895, 393))
    b1.add_vertex((879, 398))
    b1.add_vertex((891, 407))
    b1.add_vertex((918, 411))
    b1.add_vertex((943, 411))
    b1.add_vertex((933, 415))
    b1.add_vertex((952, 424))
    b1.add_vertex((965, 444))
    b1.add_vertex((970, 469))
    b1.add_vertex((957, 455))
    b1.add_vertex((943, 440))
    b1.add_vertex((953, 455))
    b1.add_vertex((945, 451))
    b1.add_vertex((959, 473))
    b1.add_vertex((955, 473))
    b1.add_vertex((957, 482))
    b1.add_vertex((944, 465))
    b1.add_vertex((954, 487))
    b1.add_vertex((957, 508))
    b1.add_vertex((944, 499))
    b1.add_vertex((943, 507))
    b1.add_vertex((941, 522))
    b1.add_vertex((946, 535))
    b1.add_vertex((961, 552))
    b1.add_vertex((973, 577))
    b1.add_vertex((979, 585))
    b1.add_vertex((994, 571))
    b1.add_vertex((1004, 564))
    b1.add_vertex((1018, 557))
    b1.add_vertex((1043, 557))
    b1.add_vertex((1057, 562))
    b1.add_vertex((1067, 572))
    b1.add_vertex((1073, 577))
    b1.add_vertex((1071, 579))
    b1.add_vertex((1073, 581))
    b1.add_vertex((1073, 400))
    b1.add_vertex((846, 132))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((824, 391))
    b1.add_vertex((829, 378))
    b1.add_vertex((835, 366))
    b1.add_vertex((835, 349))
    b1.add_vertex((831, 351))
    b1.add_vertex((830, 362))
    b1.add_vertex((827, 353))
    b1.add_vertex((824, 357))
    b1.add_vertex((825, 369))
    b1.add_vertex((821, 370))
    b1.add_vertex((824, 378))
    b1.add_vertex((821, 386))
    b1.filled = True
    b1.fill_color = '#BFB2AA'
    b1.color = '#BFB2AA'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((1044, 641))
    b1.add_vertex((1051, 626))
    b1.add_vertex((1047, 612))
    b1.add_vertex((1041, 599))
    b1.add_vertex((1032, 597))
    b1.add_vertex((1019, 604))
    b1.add_vertex((1016, 610))
    b1.add_vertex((1010, 614))
    b1.add_vertex((1017, 641))
    b1.filled = True
    b1.fill_color = '#FFEAF6'
    b1.color = '#FFEAF6'
    w.add(b1)


def useforcopy():
    """
    TODO:複製貼上用
    """
    b1 = GPolygon()
    b1.add_vertex(())
    b1.filled = True
    b1.fill_color = ''
    b1.color = ''
    w.add(b1)


def downbutten(xx, yy):
    """
    TODO:向下按鈕
    """
    b1 = GRect(12, 12, x=xx, y=yy)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((xx+3, yy+5))
    b1.add_vertex((xx+9, yy+5))
    b1.add_vertex((xx+6, yy+8))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)


def upbotten(xx, yy):
    """
    向下按鈕
    """
    b1 = GRect(12, 12, x=xx, y=yy)
    b1.filled = True
    b1.fill_color = 'silver'
    w.add(b1)
    b1 = GPolygon()
    b1.add_vertex((xx + 3, yy + 7))
    b1.add_vertex((xx + 9, yy + 7))
    b1.add_vertex((xx + 6, yy + 4))
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)


def layers(xx, yy):
    """
    TODO:創建多個圖層圖案
    """
    b1 = GRect(140, 37, x=xx, y=yy)
    b1.color = 'grey'
    w.add(b1)
    b1 = GRect(13, 13, x=xx+4, y=yy+4)
    w.add(b1)
    b1 = GRect(13, 13, x=xx+4, y=yy+20)
    w.add(b1)
    b1 = GRect(29, 29, x=xx+20, y=yy+4)
    w.add(b1)
    b1 = GLabel('正常', x=xx+52, y=yy+26)
    w.add(b1)
    b1 = GLabel('100%', x=xx+52, y=yy+39)
    w.add(b1)
    b1 = GOval(9, 6, x=xx+6, y=yy+8)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)
    b1 = GOval(9, 5, x=xx + 6, y=yy + 9)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    w.add(b1)
    b1 = GOval(3, 3, x=xx + 9, y=yy + 10)
    b1.filled = True
    b1.fill_color = 'black'
    w.add(b1)


def nouseyet():
    """
    TODO:創建色庫圖案
    """
    n = 0
    for wor1 in ['aliceblue', 'beige', 'blueviolet', 'chocolate', 'cyan', 'darkorange', 'darkseagreen', 'darkviolet',
                 'dodgerblue', 'gainsboro', 'green', 'indianred']:
        a1 = GRect(10, 10, x=174+n, y=248)
        a1.filled = True
        a1.fill_color = wor1
        a1.color = wor1
        w.add(a1)
        n += 12
    n = 0
    for wor2 in ['antiquewhite', 'bisque', 'brown', 'coral', 'darkblue', 'darkorchid', 'darkslateblue', 'whitesmoke',
                 'whitesmoke', 'whitesmoke', 'whitesmoke', 'whitesmoke']:
        a1 = GRect(10, 10, x=174+n, y=260)
        a1.filled = True
        a1.fill_color = wor2
        a1.color = wor2
        w.add(a1)
        n += 12
    k = -12
    for i in range(5):
        k += 12
        n = 0
        for j in range(12):
            a1 = GRect(10, 10, x=174 + n, y=272+k)
            a1.filled = True
            a1.fill_color = 'whitesmoke'
            a1.color = 'whitesmoke'
            w.add(a1)
            n += 12
    k = -12
    for i in range(5):
        k += 12
        n = 0
        for j in range(12):
            a1 = GRect(5, 5, x=174 + n, y=277 + k)
            a1.filled = True
            a1.fill_color = 'gainsboro'
            a1.color = 'gainsboro'
            w.add(a1)
            n += 12
    k = -12
    for i in range(5):
        k += 12
        n = 0
        for j in range(12):
            a1 = GRect(5, 5, x=179 + n, y=272 + k)
            a1.filled = True
            a1.fill_color = 'gainsboro'
            a1.color = 'gainsboro'
            w.add(a1)
            n += 12
    k = 0
    n = 0
    for j in range(5):
        a1 = GRect(5, 5, x=258 + n, y=265 + k)
        a1.filled = True
        a1.fill_color = 'gainsboro'
        a1.color = 'gainsboro'
        w.add(a1)
        n += 12
    k = 0
    n = 0
    for j in range(5):
        a1 = GRect(5, 5, x=262 + n, y=260 + k)
        a1.filled = True
        a1.fill_color = 'gainsboro'
        a1.color = 'gainsboro'
        w.add(a1)
        n += 12


def againuse():
    """
    TODO:筆刷圖案
    """
    k = -28
    for i in range(3):
        k += 28
        n = 0
        for j in range(4):
            a1 = GRect(36, 28, x=173 + n, y=387 + k)
            a1.filled = True
            a1.fill_color = 'whitesmoke'
            a1.color = 'gainsboro'
            w.add(a1)
            n += 36


def tenspace():
    """
    TODO:小功能方格
    """
    k = -21
    for i in range(2):
        k += 21
        n = 0
        for j in range(5):
            b1 = GRect(18, 18, x=172 + n, y=338 + k)
            b1.color = 'gainsboro'
            w.add(b1)
            n += 21


def colorrect():
    """
    TODO:調色盤
    """
    b1 = GRect(72, 72, x=217, y=126)
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(66, 66, x=220, y=129)
    b1.filled = True
    b1.fill_color = 'black'
    b1.color = 'black'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=129)
    b1.filled = True
    b1.fill_color = 'white'
    b1.color = 'white'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=138)
    b1.filled = True
    b1.fill_color = 'whitesmoke'
    b1.color = 'whitesmoke'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=147)
    b1.filled = True
    b1.fill_color = 'gainsboro'
    b1.color = 'gainsboro'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=156)
    b1.filled = True
    b1.fill_color = 'silver'
    b1.color = 'silver'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=165)
    b1.filled = True
    b1.fill_color = 'dimgrey'
    b1.color = 'dimgrey'
    w.add(b1)
    b1 = GRect(18, 10, x=220, y=174)
    b1.filled = True
    b1.fill_color = 'darkgrey'
    b1.color = 'darkgrey'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=129)
    b1.filled = True
    b1.fill_color = 'orange'
    b1.color = 'orange'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=138)
    b1.filled = True
    b1.fill_color = 'darkorange'
    b1.color = 'darkorange'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=147)
    b1.filled = True
    b1.fill_color = 'chocolate'
    b1.color = 'chocolate'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=156)
    b1.filled = True
    b1.fill_color = 'sienna'
    b1.color = 'sienna'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=165)
    b1.filled = True
    b1.fill_color = 'saddlebrown'
    b1.color = 'saddlebrown'
    w.add(b1)
    b1 = GRect(18, 10, x=268, y=174)
    b1.filled = True
    b1.fill_color = 'maroon'
    b1.color = 'maroon'
    w.add(b1)

    b1 = GRect(18, 10, x=236, y=129)
    b1.filled = True
    b1.fill_color = 'navajowhite'
    b1.color = 'navajowhite'
    w.add(b1)
    b1 = GRect(18, 10, x=236, y=138)
    b1.filled = True
    b1.fill_color = 'peachpuff'
    b1.color = 'peachpuff'
    w.add(b1)
    b1 = GRect(18, 10, x=236, y=147)
    b1.filled = True
    b1.fill_color = 'darksalmon'
    b1.color = 'darksalmon'
    w.add(b1)
    b1 = GRect(18, 10, x=236, y=156)
    b1.filled = True
    b1.fill_color = 'chocolate'
    b1.color = 'chocolate'
    w.add(b1)
    b1 = GRect(18, 10, x=236, y=165)
    b1.filled = True
    b1.fill_color = 'sienna'
    b1.color = 'sienna'
    w.add(b1)
    b1 = GRect(18, 10, x=236, y=174)
    b1.filled = True
    b1.fill_color = 'saddlebrown'
    b1.color = 'saddlebrown'
    w.add(b1)

    b1 = GRect(16, 10, x=252, y=129)
    b1.filled = True
    b1.fill_color = 'gold'
    b1.color = 'gold'
    w.add(b1)
    b1 = GRect(16, 10, x=252, y=138)
    b1.filled = True
    b1.fill_color = 'goldenrod'
    b1.color = 'goldenrod'
    w.add(b1)
    b1 = GRect(16, 10, x=252, y=147)
    b1.filled = True
    b1.fill_color = 'darkgoldenrod'
    b1.color = 'darkgoldenrod'
    w.add(b1)
    b1 = GRect(16, 10, x=252, y=156)
    b1.filled = True
    b1.fill_color = 'sienna'
    b1.color = 'sienna'
    w.add(b1)
    b1 = GRect(16, 10, x=252, y=165)
    b1.filled = True
    b1.fill_color = 'saddlebrown'
    b1.color = 'saddlebrown'
    w.add(b1)
    b1 = GRect(16, 10, x=252, y=174)
    b1.filled = True
    b1.fill_color = 'darkred'
    b1.color = 'darkred'
    w.add(b1)


if __name__ == '__main__':
    main()
