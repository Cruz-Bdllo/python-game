import pygame # Contiene todos los elementos para crear un videjuego
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group # Permite instanciar un grupo de elementos


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
    my_ship = Ship(screen, game_settings)
    
    # Creamos un grupo de balas
    bullets = Group()
    
    # Declaramos un ciclo principal del juego
    while True:
        # Observamos los eventos generados por el teclado y el mouse
        # Estos se generan al mover algún elemento del juego
        gf.check_events(game_settings, screen, my_ship, bullets)
        my_ship.update() # Actualiza el movimiento del elemento nave
        bullets.update() # Actualiza el movimiento de las balas
        
        # Eliminar los elementos bullet del grupo bullets
        gf.update_bullets(bullets)
        
        
        # Asignamos fondo, posicionamos la nave y dibujamos la ventana
        gf.update_screen(game_settings, screen, my_ship, bullets)                             
        
# Ejecutamos nuestra función principal        
run_game()
