import pyxel
import math

class Vector2:    
    def __init__(self,x,y):
        self.x: float = x
        self.y: float = y

class Line:
    def __init__(self,p,v):
        self.p:Vector2 = p
        self.v:Vector2 = v

    def draw_line_from_point(self):
        # ベクトルを大きく伸ばして画面外まで届かせる
        L = 300  # 画面より大きければOK(例: Pyxel デフォルト 160x120)
        
        x1 = self.p.x - self.v.x * L
        y1 = self.p.y - self.v.y * L
        x2 = self.p.x + self.v.x * L
        y2 = self.p.y + self.v.y * L

        pyxel.line(int(x1), int(y1), int(x2), int(y2), 7)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)

        # 初期値　マウスの座標で遷移
        self.p1 = Vector2(100,0)

        self.line1 = Line(Vector2(20,50),Vector2(10,10))

        pyxel.run(self.update, self.draw)

    def update(self):
        self.p1.x = pyxel.mouse_x
        self.p1.y = pyxel.mouse_y

        self.line2p = Line(self.p1,Vector2(self.p1.x - self.line1.p.x,self.p1.y - self.line1.p.y))

        self.dot = (self.line1.v.x*self.line2p.v.x) + (self.line1.v.y*self.line2p.v.y)
        self.cross = (self.line1.v.x*self.line2p.v.y) - (self.line1.v.y*self.line2p.v.x)

        self.degrees = (math.degrees(math.atan2(self.cross,self.dot)))
        

    def draw(self):
        pyxel.cls(6)
        self.line1.draw_line_from_point()
        pyxel.pset(self.p1.x,self.p1.y,0)

        pyxel.line(self.line1.p.x,self.line1.p.y,self.p1.x,self.p1.y,0)
        pyxel.line(self.line1.p.x,self.line1.p.y,self.line1.v.x + self.line1.p.x,self.line1.v.y+self.line1.p.y,2)

        
        pyxel.text(0,0,f"dot: {self.dot}",0)
        pyxel.text(0,10,f"cross: {self.cross}",0)
        pyxel.text(0,20,f"degrees: {self.degrees}",0)



App()