"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random
from abc import ABC, abstractmethod
from random import randint

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


class Point:
    # initialize point
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    # initialize velocity
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


class Projectile(ABC):
    # create projectile class to be used for both bullets and targets
    def __init__(self):
        self.center = Point(0, 0)
        self.velocity = Velocity(0, 0)
        self.alive = True

    # advances both bullets and targets
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    # checks if projectile is on the screen or not
    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x < screen_width) and (self.center.y < screen_height):
            on_screen = False
        else:
            on_screen = True
        return on_screen

    @abstractmethod
    def draw(self):
        pass


class Bullet(Projectile):
    # initialize bullet
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.center.x = 0
        self.center.y = 0

    #  draws a bullet
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, color=BULLET_COLOR)


    # fires a bullet
    def fire(self, angle: float):
        # 1 in 5 chance that the bullet will be twice as fast
        fast = randint(1, 5)
        if fast > 3:
            self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
            self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        else:
            self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED * 2
            self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED * 2



class Target(Projectile):
    # initializes target
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.lives = 0
        self.type = 0
        # sets sounds for good and bad kills
        self.hit_sound = arcade.load_sound("Skeet/Super Mario Bros.-Coin Sound Effect.mp3")
        self.bad_hit = arcade.load_sound("Skeet/buzzer wrong sound effect.mp3")

    # draws different types of targets
    def draw(self):
        if self.type == 0:
            arcade.draw_circle_filled(self.center.x, self.center.y, radius=TARGET_RADIUS, color=TARGET_COLOR)
        elif self.type == 1:
            arcade.draw_circle_outline(self.center.x, self.center.y, radius=TARGET_RADIUS, color=TARGET_COLOR)
            arcade.draw_text(repr(self.lives), self.center.x, self.center.y, TARGET_COLOR, font_size=15)
        elif self.type == 2:
            arcade.draw_rectangle_filled(self.center.x, self.center.y, TARGET_SAFE_RADIUS,
                                         TARGET_SAFE_RADIUS, color=TARGET_SAFE_COLOR)

    #  sets the alive and the score when hit
    def hit(self):
        if self.type == 0:
            self.alive = False
            # plays good sound
            arcade.play_sound(self.hit_sound)
            return 1

        elif self.type == 1:
            if self.lives == 1:
                self.alive = False
                # plays good sound
                arcade.play_sound(self.hit_sound)
                return 5
            else:
                self.lives -= 1
                return 1

        elif self.type == 2:
            self.alive = False
            # plays bad sound
            arcade.play_sound(self.bad_hit)
            return -10


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point(0, 0)
        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        self.rifle = Rifle()
        self.score = 0
        self.targets = []
        self.bullets = []
        # sets background
        self.background = arcade.load_texture("Skeet/birb.png")
        # plays Here Comes the Sun as background music
        self.background_music = arcade.load_sound("Skeet/07 Here Comes The Sun.mp3")
        arcade.play_sound(self.background_music)
        # set shooting noise
        self.shoot = arcade.load_sound("Skeet/Single gunshot - Sound effect.mp3")
        # sets killed noise
        self.kill_target = arcade.load_sound("Skeet/Window glass breaking sound effect.mp3")


    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """


        # clear the screen to begin drawing
        arcade.start_render()
        # draw background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # draw each object
        self.rifle.draw()
        #  draws bullets
        for bullet in self.bullets:
            bullet.draw()
        #  draws targets
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.GRAY)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()
        #  moves bullets
        for bullet in self.bullets:
            bullet.advance()
        #  moves targets
        for target in self.targets:
            target.advance()


    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        target = Target()
        target.center.x = random.uniform(10, SCREEN_WIDTH / 2)
        target.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        random_target = random.randint(0, 2)
        #  sets the target type that will get created
        if random_target == 0:
            target.type = 0
            target.velocity.dx = random.randint(1, 5)
            target.velocity.dy = random.randint(-2, 5)
        elif random_target == 1:
            target.lives = 3
            target.type = 1
            target.velocity.dx = random.randint(1, 3)
            target.velocity.dy = random.randint(-2, 3)
        elif random_target == 2:
            target.type = 2
            target.velocity.dx = random.randint(1, 5)
            target.velocity.dy = random.randint(-2, 5)

        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()
                        # plays crashing sound when killed
                        arcade.play_sound(self.kill_target)
                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)
        # plays shot sound
        arcade.play_sound(self.shoot)

        self.bullets.append(bullet)


    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
