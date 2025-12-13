import pyxel
import math
from pyxel_vector import Vector2
from pyxel_vector import Line
from pyxel_vector import Segment
from pyxel_vector import Circle


class App:
    def __init__(self):
        pyxel.init(160, 120)
        # pyxel.mouse(True)

        # 初期値　マウスの座標で遷移
        self.p1 = Vector2(100,0)

        self.circle = Circle(Vector2(80,60),10)

        pyxel.run(self.update, self.draw)

    def update(self):
        # マウス位置に追従する点
        self.p1.x = pyxel.mouse_x
        self.p1.y = pyxel.mouse_y

        # 直線上の一点からマウス位置までの線分
        self.line2p = Segment(self.p1,self.circle.p - self.p1 )
        
        self.isHit:bool = self.line2p.v.magnitude() < self.circle.r
        

    def draw(self):
        pyxel.cls(6)
        # （擬似的に）直線を描画
        self.circle.draw()
        pyxel.pset(self.p1.x,self.p1.y,0)

        # # 直線上の点からマウス位置までの線分
        self.line2p.draw()
        
        # 直線方向のベクトルの大きさを視覚的に描画
        # pyxel.line(self.line1.p.x,self.line1.p.y,self.line1.v.x + self.line1.p.x,self.line1.v.y+self.line1.p.y,2)

        if self.isHit:
            pyxel.text(0,40,f"Hit",8)




App()