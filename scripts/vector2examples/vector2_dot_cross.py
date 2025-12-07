import pyxel
import math
from pyxel_vector import Vector2
from pyxel_vector import Line


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)

        # 初期値　マウスの座標で遷移
        self.p1 = Vector2(100,0)

        self.line1 = Line(Vector2(80,60),Vector2(50,-50))

        pyxel.run(self.update, self.draw)

    def update(self):
        # マウス位置に追従する点
        self.p1.x = pyxel.mouse_x
        self.p1.y = pyxel.mouse_y

        # 直線上の一点からマウス位置までの線分
        self.line2p = Line(self.p1,Vector2(self.p1.x - self.line1.p.x,self.p1.y - self.line1.p.y))
         # 直線方向のベクトルとマウス位置方向のベクトルの内積 / 外積
        self.dot = self.line1.v.dot(self.line2p.v)
        self.cross = self.line1.v.cross(self.line2p.v)

        # ベクトル間の角度（弧度法）
        self.degrees = (math.degrees(math.atan2(self.cross,self.dot)))

        # 直線方向のベクトルを正規化
        # self.line1norm = self.line1.v.normalized()

        # マウス位置方向のベクトルの射影
        self.proj =  self.line2p.v.proj(self.line1.v)
        self.proj_length = self.proj.magnitude()

        # 射影からマウス位置までの距離（高さ）
        self.perp = self.line2p.v.perp(self.line1.v)
        self.perp_length = self.perp.magnitude()
        

    def draw(self):
        pyxel.cls(6)
        # （擬似的に）直線を描画
        self.line1.draw_line_from_point()
        pyxel.pset(self.p1.x,self.p1.y,0)

        # 直線上の点からマウス位置までの線分
        pyxel.line(self.line1.p.x,self.line1.p.y,self.p1.x,self.p1.y,0)
        # 直線方向のベクトルの大きさを視覚的に描画
        pyxel.line(self.line1.p.x,self.line1.p.y,self.line1.v.x + self.line1.p.x,self.line1.v.y+self.line1.p.y,2)
        
        # 射影ベクトルを視覚的に描画
        pyxel.line(self.line1.p.x,self.line1.p.y,self.line1.p.x+self.proj.x,self.line1.p.y+self.proj.y,8)
        # # 垂線
        pyxel.line(
                    self.line1.p.x+self.proj.x,
                    self.line1.p.y+self.proj.y,
                    self.line1.p.x+self.proj.x + self.perp.x,
                    self.line1.p.y+self.proj.y + self.perp.y,
                    3
                )

        pyxel.text(0,0,f"dot: {self.dot}",0)
        pyxel.text(0,10,f"cross: {self.cross}",0)
        pyxel.text(0,20,f"degrees: {self.degrees}",0)
        pyxel.text(0,30,f"magnitude: {self.line2p.v.magnitude()}",0)
        pyxel.text(0,40,f"proj_length: {self.proj_length}",0)
        pyxel.text(0,50,f"perp_length: {self.perp_length}",0)




App()