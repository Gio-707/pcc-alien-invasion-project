import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in fleet"""

    def __init__(self, ai_game):
        """Inititalize alien and start postition"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load alien image and its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store exact horizontal position of alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if alien at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <=0)
    
    def update(self):
        """Move alien to right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x