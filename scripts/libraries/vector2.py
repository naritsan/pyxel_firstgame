from __future__ import annotations
import math
from scripts.libraries.pyxel_matrix import Matrix

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
    def __mul__(self,scalar:float):
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
    def perp(self, other:Vector2):
        return self - self.proj(other)

    # 並行移動
    @staticmethod
    def translate_2d_by_multiplication(p:Vector2, dx:float, dy:float) -> None:
        tmpmtx1:Matrix = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        # 並行移動に用いる掛け算の3X3行列
        tmpmtx1.index[0][0] = 1
        tmpmtx1.index[1][1] = 1
        tmpmtx1.index[2][2] = 1

        # 移動量
        tmpmtx1.index[0][2] = dx
        tmpmtx1.index[1][2] = dy

        result:Matrix = Matrix.multiplyMatrixNxM(tmpmtx1,Matrix([[p.x],[p.y],[1]]))

        p.x = result.index[0][0]
        p.y = result.index[1][0]

        return 

    @staticmethod
    def vector2matrix(v:Vector2) -> Matrix:
        tmp = Matrix([[v.x],[v.y],[1]])

        return tmp