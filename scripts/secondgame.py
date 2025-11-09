import pyxel

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
        return False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
        pyxel.pset(self.x, self.y, 0)

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player_circle = Circle(0, 0, 8, 8)
        self.static_circle = Circle(80, 60, 16, 9)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_circle.x -= 1
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_circle.x += 1
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player_circle.y -= 1
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player_circle.y += 1

        if self.player_circle.intersects(self.static_circle):
            self.player_circle.col = 11
        else:
            self.player_circle.col = 8

    def draw(self):
        pyxel.cls(6)

        self.static_circle.draw()
        self.player_circle.draw()

App()