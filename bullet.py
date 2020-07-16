import pygame
# Permite agrupar elementos y manejarlos como un todo
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Clase que representa las balas disparadas desde la nave """
    
    def __init__(self, screen, settings, ship):
        """ Crea una bala en la posición actual de la nave """
        super(Bullet, self).__init__()
        
        # Obtenemos las propiedades de la ventana principal del juego
        self.screen = screen
        
        # Crea una figura (Rectangulo) en posición 0, 0 y establece las dimesiones de 
        # los lados de la bala, para ello usamos el método Rect
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        
        # Ajustamos la bala a la nave
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top # Aparecera en la parte superior de la nave
        
        # Almacenamos la posicion en Y de la baja, para poder manipular la velocidad en que llega 
        # desde el origen disparado de la nave hasta el borde superior de la ventana
        self.y = float(self.rect.y)
        
        # Establecemos el color y la velocidad
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
    def update(self):
        """ Actualizamos la posición de la bala """
        # Movemos la baja hacia arriba dependiendo la velocidad
        self.y -= self.speed_factor
        # Actualizamos posición
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Dibujamos la bala en la ventana """
        # Dibujamos la bala
        pygame.draw.rect(self.screen, self.color, self.rect)
        