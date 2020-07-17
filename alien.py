import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Clase que representa al elemento alien en el juego """
    def __init__(self, screen, settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        
        # Cargamos la imagen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        # Posicionamos la imagen al borde superior izquierdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Almacenamos la posición exacta del alien
        self.x = float(self.rect.x)
        
    def blitme(self):
        """ Dibuja la imagen del alien """
        self.screen.blit(self.image, self.rect)
        
        