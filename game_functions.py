import sys
import pygame
from bullet import Bullet

def check_key_down_events(event, settings, screen, ship, bullets):
    """ Realiza las acciones para los eventos cuando se PRESIONA alguna tecla """
    if event.key == pygame.K_RIGHT: # Detectamos si se presiono la tecla de fecha derecha
        # Movemos la imagen de la nave hacia la derecha
        ship.moving_right = True
    if event.key == pygame.K_LEFT: # Detectamos si se presiono la tecla de fecha derecha
        # Movemos la imagen de la nave hacia la derecha
        ship.moving_left = True
    if event.key == pygame.K_SPACE: # Detectamos cuando queramos disparar, el cual creara un obj bala
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet) # Agrega la bala al grupo de balas (Group())
        

def check_key_up_events(event, ship):
    """ Realiza las acciones para los eventos cuando se DEJA de PRESIONAR alguna tecla """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, ship, bullets):
    """ Define las funciones del juego asi como los listeners de eventos """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Se presiono una tecla
            check_key_down_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # Se deja de presionar la tecla
            check_key_up_events(event, ship)
        
            
def update_screen(settings, screen, ship, bullets):
    # Asignamos el color al fondo de la ventana
    screen.fill(settings.bg_color)
    
    # Iteramos los elementos almacenados en el grupo de balas
    for bullet in bullets.sprites():
        # Dibujamos cada bala
        bullet.draw_bullet()
    
    # Posicionamos nuestra nave 
    ship.blitme()
        
    # Dibuja la ventana mas actual que creamos, por lo que cada vez que se actualice
    # Solo estarán los elementos de la nueva ventana
    pygame.display.flip()     
    
