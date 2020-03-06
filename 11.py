import arcade
from random import randint, random
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


class Velocity:
    def __init__(self, dx, dy):
        self.dy = dy
        self.dx = dx


class FlyingObject:
    def __init__(self):
        self.velocity = Velocity(0, 0)
        self.height = 0
        self.width = 0
        self.center = Point(0, 0)
        self.alive = True
        self.height = 0
        self.width = 0
        self.rotation = 0
        self.alpha = 1000
        self.radius = 0

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        pass


class Ship(FlyingObject):
    def __init__(self):
        super(self).__init__()
        self.center = Point(0, 0)
        self.thrust = 0.0
        self.rotation = 0.0
        self.angle = 0

    def draw(self):
        pass

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class Asteroid(FlyingObject):
    def __init__(self):
        super().__init__()
        self.velocity.dx = 1.5
        self.velocity.dy = 1.5
        self.radius = 0
        self.rotation = 0
        self.angle = 0

    def draw(self):
        pass

    def hit(self):
        pass


class LargeAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.center = Point(0, 0)
        self.velocity = Velocity(0, 0)
        self.center.y = random.uniform(200, SCREEN_HEIGHT)
        self.center.x = random.uniform(200, SCREEN_WIDTH)
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        self.health = 1
        self.angle = 0

    def draw(self):
        image = "meteorGrey_big1.png"
        texture = arcade.load_texture(image)
        width = texture.width
        height = texture.height
        angle = self.angle

        arcade.draw_rectangle_filled(self.center.x, self.center.y, width, height, color=arcade.color.RED)

    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx * BIG_ROCK_SPEED
        self.center.y += self.velocity.dy * BIG_ROCK_SPEED

    def hit(self):
        self.health -= 1

    def split(self):
        pass


class MediumAsteroid(Asteroid):
    def __init__(self):
        super(self).__init__()
        self.rotation = 0
        self.velocity = Velocity(0, 0)
        self.height = 0
        self.width = 0
        self.alive = True
        self.center.x = randint(0, 10)
        self.center.y = randint(0, 10)

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, radius=BIG_ROCK_RADIUS, color=arcade.color.RED)

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def hit(self):
        pass

    def split(self):
        pass


class SmallAsteroid(Asteroid):
    def __init__(self):
        super(self).__init__()
        self.rotation = 0
        self.velocity = Velocity(0, 0)
        self.height = 0
        self.width = 0
        self.alive = True
        self.center.x = randint(0, 10)
        self.center.y = randint(0, 10)

    def draw(self):
        pass

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def hit(self):
        pass

    def split(self):
        pass


class Bullet(FlyingObject):
    def __init__(self):
        super(self).__init__()
        self.velocity = Velocity(0, 0)
        self.radius = 0.0

    def draw(self):
        pass

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def hit(self):
        pass


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.asteroids = [LargeAsteroid(), LargeAsteroid(), LargeAsteroid(),
                      LargeAsteroid(), LargeAsteroid()]

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object

        # start at with 5 asteroids incoming
        for asteroid in self.asteroids:
            asteroid.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()

        # TODO: Check for collisions

    def create_asteroids(self):
        if randint(1, 2) == 1:
            lasteroid = LargeAsteroid()
            lasteroid.center.x = random.uniform(10, SCREEN_WIDTH / 2)
            lasteroid.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
            lasteroid.velocity.dx = random.randint(1, 3)
            lasteroid.velocity.dy = random.randint(-2, 3)
            self.asteroids.append(lasteroid)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
