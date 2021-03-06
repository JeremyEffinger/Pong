import pygame
from random import randint


class Screen_Obj:
    """A class to manage the objects displayed on screen"""

    def __init__(self, pong_game):
        """Initalize the paddle and set it's starting position."""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the object at it's current location"""
        self.screen.blit(self.image, self.rect)


class P_Paddle(Screen_Obj):
    """A class for the player paddle"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        # load the  player paddle image
        self.image = pygame.image.load("images/fancy-paddle-blue.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y


class O_Paddle(Screen_Obj):
    """A class for the opponent paddle"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        # load the opponent paddle image
        self.image = pygame.image.load("images/fancy-paddle-green.png")
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y


class Ball(Screen_Obj):
    """A class for the ball"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        # load the paddle image
        self.image = pygame.image.load("images/fancy-ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.velocity = [0, 0]
        self.sfx = pygame.mixer.Sound("sounds/blip.wav")

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def blitme(self):
        """Draw the ball at it's current location"""
        self.screen.blit(self.image, self.rect)

    def center_ball(self):
        self.rect.center = self.screen_rect.center
        self.velocity = [0, 0]

    def serve_ball(self):
        self.velocity = [randint(4, 8), randint(-8, 8)]

    def move_ball_offscreen(self):
        self.rect.x = self.settings.screen_width + 100
        self.rect.y = self.settings.screen_height + 100
        self.velocity = [0, 0]

    def play_sfx(self):
        pygame.mixer.Sound.play(self.sfx)
