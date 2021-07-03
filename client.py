"""
Platformer Game
"""
import arcade
import random
import math
from network import Network

from arcade.text import draw_text

clientNumber = 0

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.5
TILE_SCALING = 0.25
METEOR_SCALING = 0.12

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.n = Network()
        self.startPosPlayer = read_pos(self.n.getPos())
        self.startPosOpponent = read_pos(self.n.getPos())


        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.meteor_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.opponent_sprite = None

        # Our physics engine
        self.physics_engine_1 = None
        self.physics_engine_2 = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # self.num_meteors = 0

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = "images/player_1/player_stand.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = self.startPosPlayer[0]
        self.player_sprite.center_y = self.startPosPlayer[1]
        self.player_list.append(self.player_sprite)

        image_source = "images/player_2/player_stand.png"
        self.opponent_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.opponent_sprite.center_x = self.startPosOpponent[0]
        self.opponent_sprite.center_y = self.startPosOpponent[1]
        self.player_list.append(self.opponent_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 32):
            wall = arcade.Sprite("images/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        # Create the 'physics engine'
        self.physics_engine_1 = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)
        self.physics_engine_2 = arcade.PhysicsEnginePlatformer(self.opponent_sprite,
                                                             self.wall_list,
                                                             GRAVITY)


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            if self.physics_engine_1.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        p2Pos = read_pos(self.n.send(make_pos((self.player_sprite.center_x, self.player_sprite.center_y))))
        self.opponent_sprite.center_x = p2Pos[0]
        self.opponent_sprite.center_y = p2Pos[1]

        # Creates meteors
        # if self.num_meteors != 7:
        #     meteor = arcade.Sprite("images/meteor.jpg", METEOR_SCALING)
        #     meteor.center_x = random.randint(0, 1000)
        #     meteor.center_y = 650
        #     meteor.change_x = random.randint(-1, 1)
        #     meteor.change_y = random.randint(-5, -3)
        #     if meteor.change_x != 0:
        #         theta = math.degrees(math.atan(meteor.change_y / meteor.change_x))
        #         meteor.turn_right(theta)
        #     self.wall_list.append(meteor)
        #     self.num_meteors += 1

        # for i in self.wall_list:
        #     if i.center_y < 0:
        #         self.wall_list.remove(i)
        #         self.num_meteors -= 1

        # Move the player with the physics engine
        self.physics_engine_1.update()
        self.physics_engine_2.update()

def read_pos(str):
        str = str.split(",")
        return float(str[0]), float(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()