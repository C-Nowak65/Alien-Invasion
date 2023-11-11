import pygame
from settings import Settings
import sys
from ship import Ship

class AlienInvasion:
    '''Overall class to manage the game assets and behavior'''
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            '''watch for keyboard and mouse events'''
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
            '''Respond to keypresses and mouse events.'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        '''Update images on the screen, and flip to a new screen.'''
        #Redraw the screen each time through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
            
if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()