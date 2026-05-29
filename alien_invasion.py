import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        #setting background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start main loop for game"""
        while True:
            #Watch for kb & m events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #Redraw screen durring each pass through loop
                self.screen.fill(self.bg_color)

                #Make the most recently drawn screen size visible.
                pygame.display.flip()
                self.clock.tick(60)

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()