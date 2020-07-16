class Setting():
    """ Clase que permite manejar las configuraciones del juego """
    
    def __init__(self):
        """ Inicializa configuraciones predeterminadas """
        
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (133, 193, 233)
        
        # Configuración de la nave
        self.ship_speed_factor = 1.5
        
        # Configuración para las balas
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 118, 51)
        
        