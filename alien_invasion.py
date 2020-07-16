import pygame # Contiene todos los elementos para crear un videjuego
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    """ Función principal para ejecutar el juego """
    
    # Inicializa la configuración de fondo para que pygame pueda funcionar correctamente
    pygame.init() 
    
    # Instanciamos la clase Setting para establecer las configuraciones del juego
    game_settings = Setting()
    
    # Establecemos las propiedades de la ventana, dando una tupla como argumento
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    
    # Definimos un titulo en la ventana del juego
    pygame.display.set_caption("Alien Invasion")
    
    # Creamos nuestra navecita
    my_ship = Ship(screen)
    
    # Declaramos un ciclo principal del juego
    while True:
        # Observamos los eventos generados por el teclado y el mouse
        gf.check_events(my_ship)
        
        my_ship.update()
        
        # Asignamos fondo, posicionamos la nave y dibujamos la ventana
        gf.update_screen(game_settings, screen, my_ship)                             
        
# Ejecutamos nuestra función principal        
run_game()
