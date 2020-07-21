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
        self.ship_limit = 3
        
        # Configuración para las balas
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 118, 51)
        self.bullets_allowed = 3
        
        # Configuración de alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Dirección a la que cada fila de alien se movera (1? derecha, -1 izquierda)
        self.fleet_direction = 1
        
        