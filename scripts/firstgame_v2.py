import pyxel

class App:
    def __init__(self):
        pyxel.init(
            40, 30, title="secondgame!", fps=20, display_scale=20
        )
        self.x = 30
        self.y = 10
        self.apple_x = pyxel.rndi(19, pyxel.width - 1)
        self.apple_y = pyxel.rndi(9, pyxel.height - 1)
        self.rotten_apple_x = pyxel.rndi(19, pyxel.width - 1)
        self.rotten_apple_y = pyxel.rndi(9, pyxel.height - 1)
        self.score = 0
        self.game_over = False
        self.time_up = False
        self.timer = 10

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over or self.time_up:
            return

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x += 1
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.y -= 1
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.y += 1

        # 衝突判定
        if self.x == self.apple_x and self.y == self.apple_y:
            self.score += 100
            self.apple_x = pyxel.rndi(19, pyxel.width - 1)
            self.apple_y = pyxel.rndi(9, pyxel.height - 1)
            self.rotten_apple_x = pyxel.rndi(19, pyxel.width - 1)
            self.rotten_apple_y = pyxel.rndi(9, pyxel.height - 1)
        
        if self.x == self.rotten_apple_x and self.y == self.rotten_apple_y:
            self.game_over = True
        
        if pyxel.frame_count != 0 and pyxel.frame_count % 20 == 0 and not self.game_over:
            self.timer -= 1
            if self.timer <= 0:
                self.time_up = True

    def draw(self):
        if self.game_over:
            pyxel.cls(0)
            pyxel.text(4, 11, "GAMEOVER", 8)
        elif self.time_up:
            pyxel.cls(0)
            pyxel.text(0, 11, f"SCORE:{self.score} ", 7)
        else:
            pyxel.cls(6)
            pyxel.pset(self.rotten_apple_x, self.rotten_apple_y, 3)
            pyxel.pset(self.apple_x, self.apple_y,8)
            pyxel.rect(0, 0, 40, 8, 0)
            pyxel.rect(30, 0, 10, 8, 14)
            pyxel.text(32,1,f"{self.timer}",7)
            pyxel.text(1, 1, f"{self.score}", 7)
            pyxel.pset(self.x, self.y,1)

App()