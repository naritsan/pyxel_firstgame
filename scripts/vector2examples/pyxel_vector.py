import pyxel
import math

class Vector2:    
    # コンストラクタ
    def __init__(self,x:float,y:float):
        self.x: float = x
        self.y: float = y

### ベクトル演算 ##

    # 加算
    def __add__(self,other:Vector2):
        return Vector2(self.x + other.x, self.y + other.y)

    # 減算
    def __sub__(self,other:Vector2):
        return Vector2(self.x - other.x, self.y - other.y)

    # 乗算（スカラー倍）
    def __mul__(self,scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    # 式の左右が逆の場合にも対応
    __rmul__ = __mul__

## 定数 ##

    # ベクトルの長さ
    def magnitude(self) -> float:
        return math.hypot(self.x,self.y)

    # 内積
    def dot(self,other:Vector2) -> float:
        return (self.x*other.x) + (self.y*other.y)

    # 外積
    def cross(self,other:Vector2) -> float:
        return (self.x*other.y) - (self.y*other.x)

## ベクトル変換 ##

    # 正規化
    def normalized(self) -> Vector2:
        if self.magnitude() == 0:
            return Vector2(0,0)
        return Vector2(self.x / self.magnitude(),self.y / self.magnitude())

    # 射影
    def proj(self,other:Vector2) -> Vector2:
        n = other.normalized()
        len = self.dot(n)
        return Vector2(n.x*len,n.y*len)

    # 垂線
    def perp(self, other):
        return self - self.proj(other)

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