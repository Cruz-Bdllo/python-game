import pygame.font
from pygame.sprite import Group

from ship import Ship 

class Scoreboard():
    """ Representación del puntaje del jugador """
    def __init__(self, screen, settings, stats):
        """ Inicializando las propiedades para la instancia """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        
        # Configuración del formato de despliegue
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        # Imagen del record, puntaje mas alto y nivel
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    
    def prep_score(self):
        """ Asignamos las propiedades para renderizar el elemento """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Mostramos el puntaje en el borde superior de la ventana
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """ Dibuja la tabla de puntaje """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
        
    def prep_high_score(self):
        """ Renderizamos el record del puntaje mas alto """
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Posicionamos el record
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
        
    def prep_level(self):
        """ Cambia el nivel del juego """
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)
        
        # Posicionamos la imagen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10
        
        
    def prep_ships(self):
        """ Mostrara cuantas naves hay """
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
        
        
        