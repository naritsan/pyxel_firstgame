from __future__ import annotations
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

    def draw(self):
        # ベクトルを大きく伸ばして画面外まで届かせる
        L = 300  # 画面より大きければOK(例: Pyxel デフォルト 160x120)
        
        x1 = self.p.x - self.v.x * L
        y1 = self.p.y - self.v.y * L
        x2 = self.p.x + self.v.x * L
        y2 = self.p.y + self.v.y * L

        pyxel.line(int(x1), int(y1), int(x2), int(y2), 7)

class Ray:
    def __init__(self,p,v):
        self.p:Vector2 = p
        self.v:Vector2 = v

    def draw(self):
        # ベクトルを大きく伸ばして画面外まで届かせる
        L = 300  # 画面より大きければOK(例: Pyxel デフォルト 160x120)
        
        x2 = self.p.x + self.v.x * L
        y2 = self.p.y + self.v.y * L

        pyxel.line(int(self.p.x), int(self.p.y), int(x2), int(y2), 7)

class Segment:
    def __init__(self,p,v):
        self.p:Vector2 = p
        self.v:Vector2 = v

    def draw(self):
        # 始点からベクトルの長さ分だけ線分を描画する
        
        endp:Vector2 = self.p + self.v
        pyxel.line(int(self.p.x), int(self.p.y), int(endp.x), int(endp.y), 7)

class Circle:
    def __init__(self,p,r):
        self.p:Vector2 = p
        self.r:float = r

    def draw(self):
        # 始点からベクトルの長さ分だけ線分を描画する
        pyxel.circb(self.p.x,self.p.y,self.r,0)
        