class Setting():
    """ Clase que permite manejar las configuraciones del juego """
    
    def __init__(self):
        """ Inicializa configuraciones predeterminadas """
        # Configuración de la pantall
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (133, 193, 233)
        self.ship_speed_factor = 1.5