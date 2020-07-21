class GameStats():
    """ Permite representar el seguimiento del record de un jugador """
    def __init__(self, settings):
        """ Inicializamos nuestras propiedades """
        self.settings = settings
        self.reset_stats()
        
    def reset_stats(self):
        """ Reinicia el contador del jugador """
        self.ship_left = self.settings.ship_limit