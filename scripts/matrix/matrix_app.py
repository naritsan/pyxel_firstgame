import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            pass
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            pass
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            pass
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            pass
        

    def draw(self):
        pyxel.cls(6)

App()