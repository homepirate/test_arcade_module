import arcade


class Mygame(arcade.Window):
    WIDTH = 700
    HEIGHT = 600

    def __init__(self):
        super().__init__(self.WIDTH, self.HEIGHT, "First Game")
        self.background_color = arcade.color.GOLD

        self.player = arcade.Sprite('icons/1.png', scale=0.2)
        self.set_player_start()

        self.ground = arcade.create_rectangle_filled(self.WIDTH // 2, self.HEIGHT // 2, 100, 50, arcade.color.GUPPIE_GREEN)

    def set_player_start(self):
        self.player.center_x = 200
        self.player.center_y = 200

    def update(self, delta_time: float):
        self.player.update()
        if self.player.center_x > self.WIDTH-30 or self.player.center_x < 0+30:
            self.player.change_x = 0
        elif self.player.center_y > self.HEIGHT-55 or self.player.center_y < 0+55:
            self.player.change_y = 0

        elif (self.WIDTH // 2 - 80 < self.player.center_x < self.WIDTH // 2 + 100) and (self.HEIGHT // 2 - 75 < self.player.center_y < self.HEIGHT // 2 + 55):
            self.player.change_x = 0
        elif ((self.HEIGHT // 2 - 80 <= self.player.center_y <= self.HEIGHT // 2) or (self.HEIGHT // 2 + 30 <= self.player.center_y - 30 <= self.HEIGHT // 2 + 50)) and (self.WIDTH // 2 - 75 <= self.player.center_x <= self.WIDTH // 2 + 80):
            self.player.change_y = 0
            print(self.player.center_x)

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.ground.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 1
        elif symbol == arcade.key.S:
            self.player.change_y -= 1
        elif symbol == arcade.key.D:
            self.player.change_x = 1
        elif symbol == arcade.key.A:
            self.player.change_x -= 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        elif symbol == arcade.key.S:
            self.player.change_y = 0
        elif symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0


if __name__ == '__main__':
    mg = Mygame()
    mg.run()
