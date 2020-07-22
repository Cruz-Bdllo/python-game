import pygame.font # Renderiza texto en pantalla

class Button():
    """ Representación del boton que comienza el juego """
    
    def __init__(self, settings, screen, msg):
        """ Inicializar las propiedades del botón """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Establecemos las propiedades del botón
        self.width, self.height = 600, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        
        # Posicionamos el botón
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Preparamos el mensaja a desplegar
        self.prep_msg(msg) 
        
        
    def prep_msg(self, msg):
        """ Asigna el mensaje a mostrar en el botón """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    
    def draw_botton(self):
        """ Dibujamos el botón en la ventana """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        