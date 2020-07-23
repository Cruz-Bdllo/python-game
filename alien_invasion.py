import pygame # Contiene todos los elementos para crear un videjuego
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group # Permite instanciar un grupo de elementos
from game_stats import GameStats
from button import Button
from scoreborad import Scoreboard


def run_game():
    """ Función principal para ejecutar el juego """
    
    # Inicializa la configuración de fondo para que pygame pueda funcionar correctamente
    pygame.init() 
    
    # Instanciamos la clase Setting para establecer las configuraciones del juego
    game_settings = Setting()
    
    # Establecemos las propiedades de la ventana, dando una tupla como argumento
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    
    # Instanciamos GameStats para almacenar el puntaje del jugador y la tabla de puntaje
    stats = GameStats(game_settings)
    sb = Scoreboard(screen, game_settings, stats)
    
    
    # Definimos un titulo en la ventana del juego
    pygame.display.set_caption("Alien Invasion")
    
    # Instanciamos el boton de inicio
    play_button = Button(game_settings, screen, "Jugar")
    
    # Creamos nuestra navecita, grupo de balas y flota de aliencitos
    my_ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    
    # Flota de aliens
    gf.create_fleet_aliens(game_settings, screen, my_ship, aliens)
    
    
    # Declaramos un ciclo principal del juego
    while True:
        # Observamos los eventos generados por el teclado y el mouse
        # Estos se generan al mover algún elemento del juego
        gf.check_events(game_settings, screen, stats, sb, play_button, my_ship, aliens, bullets)
        
        if stats.game_active:     
            my_ship.update() # Actualiza el movimiento del elemento nave
            bullets.update() # Actualiza el movimiento de las balas
        
            # Eliminar los elementos bullet del grupo bullets
            gf.update_bullets(game_settings, screen, stats, sb, my_ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, my_ship, aliens, bullets)
                
        # Actualizamos la posiciones de los elementos
        gf.update_screen(game_settings, screen, stats, sb, my_ship, aliens, bullets, play_button)                             
        
# Ejecutamos nuestra función principal        
run_game()
