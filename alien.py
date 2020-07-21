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
    
    
    def update(self):
        """ Actualiza la posición hacia la derecha del alien de acuerdo a la 
            unidad de velocidad especificada """
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
    
    
    def check_edges(self):
        """ Retorna True si el alien esta en algún borde de la ventana """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
        
        
    
        