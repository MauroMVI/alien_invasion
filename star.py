import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the space."""
    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star_10.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.y = float(self.rect.y)
