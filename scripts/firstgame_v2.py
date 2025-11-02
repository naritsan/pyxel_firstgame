import pyxel

class App:
    def __init__(self):
        pyxel.init(
            40, 30, title="secondgame!", fps=20, display_scale=20
        )
        self.x = 0
        self.y = 0
        self.apple_x = 20
        self.apple_y = 15
        self.apple_eaten = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x += 1
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.y -= 1
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.y += 1

        if self.x == self.apple_x and self.y == self.apple_y:
            self.apple_eaten = True

    def draw(self):
        pyxel.cls(6)
        pyxel.pset(self.x, self.y,1)
        if not self.apple_eaten:
            pyxel.pset(self.apple_x, self.apple_y,8)

App()