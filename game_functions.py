import sys
import pygame

def check_events(ship):
    """ Define las funciones del juego asi como los listeners de eventos """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Se presiono un boton
            if event.key == pygame.K_RIGHT: # Detectamos si se presiono la tecla de fecha derecha
                # Movemos la imagen de la nave hacia la derecha
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            
def update_screen(settings, screen, ship):
    # Asignamos el color al fondo de la ventana
    screen.fill(settings.bg_color)
    
    # Posicionamos nuestra nave 
    ship.blitme()
        
    # Dibuja la ventana mas actual que creamos, por lo que cada vez que se actualice
    # Solo estarán los elementos de la nueva ventana
    pygame.display.flip()     