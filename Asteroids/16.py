import arcade
from random import randint, random
import random
import math
from abc import ABC, abstractmethod

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
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Velocity:
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0


class FlyingObject:

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True
        self.angle = 0

    def wrapping(self):
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        if self.center.x < 0:
            self.center.x = SCREEN_WIDTH

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class Ship(FlyingObject):

    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH * .5
        self.center.y = SCREEN_HEIGHT * .5
        self.speed = SHIP_THRUST_AMOUNT / 3
        self.angle = 90
        self.radius = SHIP_RADIUS

    def draw(self):
        image = "Asteroids/playerShip1_orange.png"
        texture = arcade.load_texture(image)
        width = texture.width
        height = texture.height
        angle = self.angle
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, angle)

    def turn_right(self):
        self.angle -= SHIP_TURN_AMOUNT

    def turn_left(self):
        self.angle += SHIP_TURN_AMOUNT

    def move_backwards(self):
        self.velocity.dx -= self.speed * math.cos(math.radians(self.angle + 90))
        self.velocity.dy -= self.speed * math.sin(math.radians(self.angle + 90))

    def move_forward(self):
        self.velocity.dx += self.speed * math.cos(math.radians(self.angle + 90))
        self.velocity.dy += self.speed * math.sin(math.radians(self.angle + 90))


class Asteroid(FlyingObject, ABC):

    def __init__(self):
        super().__init__()
        self.velocity.dx = 1.5
        self.velocity.dy = 1.5
        self.radius = 0
        self.angle = 0
        self.rotation = 0

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def hit(self):
        pass


class LargeAsteroid(Asteroid):

    def __init__(self):
        super().__init__()
        self.center.y = random.uniform(0, SCREEN_HEIGHT - 800)
        self.center.x = random.uniform(0, SCREEN_WIDTH - 500)
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS

    def draw(self):
        image = "Asteroids/meteorGrey_big1.png"
        texture = arcade.load_texture(image)

        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle)

    def hit(self):
        new_asteroids = []
        self.alive = False
        medium_asteroid = MediumAsteroid(self)
        medium_asteroid.velocity.dy = self.velocity.dy + 2
        small_asteroid = SmallAsteroid(self)
        small_asteroid.velocity.dx = self.velocity.dx + 5
        new_asteroids.append(medium_asteroid)
        new_asteroids.append(medium_asteroid)
        new_asteroids.append(small_asteroid)
        return new_asteroids

    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class MediumAsteroid(Asteroid):

    def __init__(self, large_asteroid):
        super().__init__()
        self.center.x = large_asteroid.center.x
        self.center.y = large_asteroid.center.y
        self.rotation = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS

    def draw(self):
        img = "Asteroids/meteorGrey_med1.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle)

    def hit(self):
        new_asteroids = []
        self.alive = False
        small_asteroid = SmallAsteroid(self)
        small_asteroid.velocity.dy = self.velocity.dy + 1.5
        small_asteroid.velocity.dx = self.velocity.dx + 1.5
        new_asteroids.append(small_asteroid)
        new_asteroids.append(small_asteroid)
        return new_asteroids

    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class SmallAsteroid(Asteroid):

    def __init__(self, medium_asteroid):
        super().__init__()
        self.center.x = medium_asteroid.center.x
        self.center.y = medium_asteroid.center.y
        self.rotation = SMALL_ROCK_SPIN
        self.radius = SMALL_ROCK_RADIUS

    def draw(self):
        img = "Asteroids/meteorGrey_small1.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle)

    def hit(self):
        self.alive = False
        return list()

    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class Bullet(FlyingObject):

    def __init__(self, ship):
        super().__init__()
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.age = BULLET_LIFE
        self.angle = ship.angle + 90
        self.radius = BULLET_RADIUS

    def draw(self):
        image = "Asteroids/laserBlue01.png"
        texture = arcade.load_texture(image)
        width = texture.width
        height = texture.height
        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle)

    def advance(self):
        self.age -= 1
        if self.age < 0:
            self.alive = False

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def fire(self):
        self.velocity.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED


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
        self.ship = Ship()
        self.held_keys = set()
        self.asteroids = [LargeAsteroid(), LargeAsteroid(), LargeAsteroid(), LargeAsteroid(), LargeAsteroid()]
        self.asteroids = []
        self.bullets = []

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        for asteroid in self.asteroids:
            asteroid.draw()

        for bullet in self.bullets:
            bullet.draw()

        if self.ship.alive:
            self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.ship.advance()
        self.wrap_check()
        self.check_collision()
        for asteroid in self.asteroids:
            asteroid.advance()
        for bullet in self.bullets:
            bullet.advance()
        if random.randint(1, 500) == 1:
            self.asteroids.append(LargeAsteroid())

    def wrap_check(self):
        self.ship.wrapping()
        for asteroid in self.asteroids:
            asteroid.wrapping()
        for bullet in self.bullets:
            bullet.wrapping()

    def check_collision(self):

        new_asteroid = []
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                            abs(bullet.center.y - asteroid.center.y) < too_close):
                        bullet.alive = False
                        new_asteroid += asteroid.hit()
            self.asteroids += new_asteroid
        for asteroid in self.asteroids:
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius
                if (abs(asteroid.center.x - self.ship.center.x) < too_close and
                        abs(asteroid.center.y - self.ship.center.y) < too_close):
                    self.ship.alive = False

        self.cleanup_zombies()

    def cleanup_zombies(self):

        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.move_forward()

        if arcade.key.DOWN in self.held_keys:
            self.ship.move_backwards()

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
                bullet = Bullet(self.ship)
                bullet.fire()
                bullet.advance()
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
