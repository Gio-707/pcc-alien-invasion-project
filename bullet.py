import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""

    def __init__(self,ai_game):
        """Create bullet object where ship positioned"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create rect at (0,0) then set correct cordinates
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        """Moves bullet up screen"""
        # Update exact position
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)