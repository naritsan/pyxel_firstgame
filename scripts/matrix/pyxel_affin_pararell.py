import pyxel
from scripts.libraries.vector2 import Vector2

class Triangle:
    def __init__(self,p1:Vector2,p2:Vector2,p3:Vector2,col:int):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.col: int = col

    def draw(self):
        pyxel.trib(self.p1.x,self.p1.y,self.p2.x,self.p2.y,self.p3.x,self.p3.y,self.col)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.t1 = Triangle(Vector2(0,20),Vector2(20,0),Vector2(30,40),0)
        pyxel.run(self.update, self.draw)

    def update(self):

        Vector2.translate_2d_by_multiplication(self.t1.p1,1,1)
        Vector2.translate_2d_by_multiplication(self.t1.p2,1,1)
        Vector2.translate_2d_by_multiplication(self.t1.p3,1,1)


    def draw(self):
        pyxel.cls(6)
        # pyxel.pset(self.t1.p1.x,self.t1.p1.y,0)
        self.t1.draw()

App()