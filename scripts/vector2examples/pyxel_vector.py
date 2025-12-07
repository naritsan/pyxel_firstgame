import pyxel
import math

class Vector2:    
    def __init__(self,x,y):
        self.x: float = x
        self.y: float = y

    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)

    @staticmethod
    def normalize(v:Vector2):
        return Vector2(v.x / v.magnitude(),v.y / v.magnitude())

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