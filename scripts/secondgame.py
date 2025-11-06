import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.circ1_r = 8
        self.circ1_col = 8
        self.circ2_x = 80
        self.circ2_y = 60
        self.circ2_r = 16
        self.circ2_col = 9
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
        
        dx = self.circ2_x - self.x
        dy = self.circ2_y - self.y
        dist = math.sqrt(dx * dx + dy * dy)

        if dist < self.circ1_r + self.circ2_r:
            self.collision = True
        else:
            self.collision = False

    def draw(self):
        pyxel.cls(6)

        # circ2
        pyxel.circ(self.circ2_x, self.circ2_y, self.circ2_r, self.circ2_col)
        pyxel.pset(self.circ2_x, self.circ2_y, 0)

        # circ1
        pyxel.circ(self.x, self.y, self.circ1_r, self.circ1_col)
        pyxel.pset(self.x, self.y, 0)


        if hasattr(self, 'collision') and self.collision:
            pyxel.text(0, 0, "Collision!", 8)
App()