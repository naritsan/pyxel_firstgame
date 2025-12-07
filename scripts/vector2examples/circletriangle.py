import pyxel
import math

class Vector2:    
    def __init__(self,x,y):
        self.x: float = x
        self.y: float = y

class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3,col):
        self.x1: float = x1
        self.y1: float = y1
        self.x2: float = x2
        self.y2: float = y2
        self.x3: float = x3
        self.y3: float = y3
        self.col: int = col

    def adj(self):
        return self.x3 - self.x1

    def opp(self):
        return self.y3 - self.y2
    
    def hyp(self):
        return round(math.sqrt(self.adj() **2 + self.opp() **2),1)
    def sin(self):
        if self.hyp() == 0:
            return None

        return self.opp() / self.hyp()
    
    def cos(self):
        if self.hyp() == 0:
            return None
        
        return self.adj() / self.hyp()

    def tan(self):
        if self.adj() ==0:
            return None
        
        return self.opp() / self.adj()
    
    def degree(self):
        return (math.degrees(math.atan2((self.y1 - self.y2),math.fabs(self.x2 - self.x1))) )

class Circle:
    def __init__(self, x, y, r, col):
        self.x = x
        self.y = y
        self.r = r
        self.col = col
        self.closest_rect_x = 0
        self.closest_rect_y = 0

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
        pyxel.pset(self.x, self.y, 0)

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)
        self.player = Circle(x=0,y=0,r=10,col=1)
        self.rtri1 = Triangle(80, 60, 100, 30, 100, 60, 7)

        pyxel.run(self.update, self.draw)

    def update(self):
            self.rtri1.x2 = pyxel.mouse_x
            self.rtri1.x3 = pyxel.mouse_x
            self.rtri1.y2 = pyxel.mouse_y
        

    def draw(self):
        pyxel.cls(0)

        # 矩形の描画
        self.player.draw()
        pyxel.trib(
                self.rtri1.x1,
                self.rtri1.y1,
                self.rtri1.x2,
                self.rtri1.y2,
                self.rtri1.x3,
                self.rtri1.y3,
                self.rtri1.col
            )

        # p1
        pyxel.text(self.rtri1.x1-10,self.rtri1.y1+5,f'{self.rtri1.x1},{self.rtri1.y1}',7)

        # p2
        pyxel.text(self.rtri1.x2,self.rtri1.y2-10,f'{self.rtri1.x2},{self.rtri1.y2}',7)
        # p3
        pyxel.text(self.rtri1.x3,self.rtri1.y3+5,f'{self.rtri1.x3},{self.rtri1.y3}',7)

        # adj
        pyxel.text(self.rtri1.x2 - self.rtri1.x1 / 2 ,self.rtri1.y1+5,f'{self.rtri1.adj()}',8)
        # opp
        pyxel.text(self.rtri1.x2+10,self.rtri1.y3 - self.rtri1.y2 / 2,f'{self.rtri1.opp()}',8)
        # hyp
        pyxel.text(self.rtri1.x1 - 30 ,self.rtri1.y3 - self.rtri1.y2 / 2,f'{self.rtri1.hyp()}',8)

        # sin
        pyxel.text(0,0,f'sin :{self.rtri1.sin()}',8)
        # cos
        pyxel.text(0,10,f'cos :{self.rtri1.cos()}',8)
        # tan
        pyxel.text(0,20,f'tan :{self.rtri1.tan()}',8)
        # degree
        pyxel.text(0,30,f'degree: {self.rtri1.degree()}',8)




App()