import pygame

class Ship():
    """ Clase que representa la nave del jugador """
    # PyGame maneja los elementos del juego como rectangulos
    
    def __init__(self, screen):
        """ Inicializa la imagen de la nave y establece la posición de inicio """
        self.screen = screen
        
        # Cargamos la imagen desde su ubicación y obtenemos su perimetro 
        self.image = pygame.image.load('images/ship.png')
        # Obtenemos el perímetro de la imagen obtenida
        self.rect = self.image.get_rect()
        # obtenemos el perimetro de la ventana
        self.screen_rect = screen.get_rect()
        
        
        # Establecemos la posición de la nave cada nueva instancia
        self.rect.centerx = self.screen_rect.centerx # Centrado en el eje X window/2
        self.rect.bottom = self.screen_rect.bottom   # Posicionado en el borde de la ventana
        
    # ------------------------------------------------------------
    
    def blitme(self):
        """ Dibuja la nave en su posición actual """
        self.screen.blit(self.image, self.rect)
    