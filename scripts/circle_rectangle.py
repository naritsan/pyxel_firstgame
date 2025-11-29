import pyxel
import math


class Rectangle:    
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col


    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)
        pyxel.pset(self.x, self.y, 0)
    
    def intersects(self, other):
        if isinstance(other, Rectangle):
            return (
                        self.x + self.w >= other.x and
                        self.x <= other.x + other.w and
                        self.y + self.h >= other.y and
                        self.y <= other.y + other.h
                    )
        return False

class Circle:
    def __init__(self, x, y, r, col):
        self.x = x
        self.y = y
        self.r = r
        self.col = col

    def intersects(self, other):
        if isinstance(other, Circle):
            dx = self.x - other.x
            dy = self.y - other.y
            dist_square = dx * dx + dy * dy
            return dist_square <= (self.r + other.r) ** 2
        
        if isinstance(other, Rectangle):
            is_vertical_collide = \
            (
                self.x > other.x and
                self.x < other.x + other.w and
                self.y >= other.y - self.r and
                self.y < other.y+ other.h + self.r
            )

            is_horizontal_collide = \
            (
                self.x >= other.x - self.r and
                self.x < other.x + other.w + self.r and
                self.y >= other.y and
                self.y < other.y + other.h
            )

            is_left_top_collide = \
            (
                (
                    (other.x - self.x) ** 2 + (other.y - self.y) ** 2 
                ) < self.r ** 2
            )

            is_right_top_collide = \
            (
                (
                    (self.x - (other.x+other.w)) ** 2 + (other.y - self.y) ** 2
                ) < self.r ** 2
            )

            is_left_bottom_collide = \
            (
                (
                    (other.x - self.x) ** 2 + (other.y+other.h - self.y) ** 2 
                ) < self.r ** 2
            )

            is_right_bottom_collide = \
            (
                (
                    (self.x - (other.x+other.w)) ** 2 + (other.y+other.h - self.y) ** 2
                ) < self.r ** 2
            )

            return \
            (
                is_vertical_collide or 
                is_left_top_collide or 
                is_right_top_collide or 
                is_left_bottom_collide or 
                is_right_bottom_collide
            )

        return False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
        pyxel.pset(self.x, self.y, 0)

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Circle(x=0,y=0,r=10,col=1)
        self.obstacle = Rectangle(x=80, y=60, w=30, h=20, col=8)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player.x += 1
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player.y += 1
        

    def draw(self):
        pyxel.cls(6)

        # 矩形の描画
        self.obstacle.draw()
        self.player.draw()


        if self.player.intersects(self.obstacle):
            pyxel.text(50, 10, "collide", 0)
App()