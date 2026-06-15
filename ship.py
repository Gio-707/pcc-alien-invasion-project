import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Manages game ship"""
    
    def __init__(self, ai_game):
        """Initialize ship and set start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store float value of ships postition horizontally
        self.x = float(self.rect.x)

        #Movement flag, begin with unmoving ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update postition based on movement flage"""
        # Upadte ships x cordinate bases on movement direction
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update ships rect based on ships x cordinate
        self.rect.x = self.x
    
    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image,self.rect)