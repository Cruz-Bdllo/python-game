import sys
import pygame
from bullet import Bullet
from alien import Alien



def check_events(settings, screen, ship, bullets):
    """ Define las funciones del juego asi como los listeners de eventos """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Se presiono una tecla
            check_key_down_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # Se deja de presionar la tecla
            check_key_up_events(event, ship)
        
            
def update_screen(settings, screen, ship, aliens, bullets):
    # Asignamos el color al fondo de la ventana
    screen.fill(settings.bg_color)
    
    # Iteramos los elementos almacenados en el grupo de balas
    for bullet in bullets.sprites():
        # Dibujamos cada bala
        bullet.draw_bullet()
    
    # Invocamos el método que dibuje los elementos y grupos
    ship.blitme()
    aliens.draw(screen)
        
    # Dibuja la ventana mas actual que creamos, por lo que cada vez que se actualice
    # Solo estarán los elementos de la nueva ventana
    pygame.display.flip()     
    
    
    
def update_bullets(bullets):
    """ Actualiza la posición de las balas y elimina las ya disparadas """
    # Eliminar los elementos bullet del grupo bullets
    # una vez que lleguen al borde de la ventana
    # Metodo copy() nos permite modificar la lista de bullets
    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)


def check_key_down_events(event, settings, screen, ship, bullets):
    """ Realiza las acciones para los eventos cuando se PRESIONA alguna tecla """
    if event.key == pygame.K_RIGHT: # Detectamos si se presiono la tecla de fecha derecha
        # Movemos la imagen de la nave hacia la derecha
        ship.moving_right = True
    if event.key == pygame.K_LEFT: # Detectamos si se presiono la tecla de fecha derecha
        # Movemos la imagen de la nave hacia la derecha
        ship.moving_left = True
    if event.key == pygame.K_SPACE: # Detectamos cuando queramos disparar, el cual creara un obj bala
        file_bullet(bullets, settings, screen, ship)
    if event.key == pygame.K_q:
        sys.exit()
        

def check_key_up_events(event, ship):
    """ Realiza las acciones para los eventos cuando se DEJA de PRESIONAR alguna tecla """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    

def file_bullet(bullets, settings, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet) # Agrega la bala al grupo de balas (Group())
        
def get_number_aliens_x(settings, alien_width):
    """ Obtenemos el numero de elementos alien que se pueden ajustar al ancho de la ventana """
    # Al ancho de la ventana le restamos el ancho de 2 elementos alien 
    available_space_x = settings.screen_width - 2 * alien_width
    # Mediante el espacio disponible determinamos el número total de alien que se pueden desplegar
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    return number_aliens_x
        
def create_alien(screen, settings, aliens, alien_number, row_number):
    """ Creamos un alien dando el margen al que serán posicionados """
    # Creamos un alien para obtener las dimesiones del elementos para realizar los calculoe
    alien = Alien(screen, settings)
    alien_width = alien.rect.width

    # Crear y posicionar
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    

def create_fleet_aliens(settings, screen, ship, aliens):
    """ Función que crea la flota de elementos alien, con un margen entre ellos """
    # Creamos un alien para obtener las dimesiones del elementos para realizar los calculoe
    alien = Alien(screen, settings)
    # Mediante el espacio disponible determinamos el número total de alien que se pueden desplegar
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_row(settings, ship.rect.height, alien.rect.height)
    
    # Creamos las FILAS del grupo de aliens
    for row_number in range(number_rows):
        # Creamos la fila para los N elementos que se pieden ajustar al ancho de la ventana
        for alien_number in range(number_aliens_x):
            # Crear y posicionar
            create_alien(screen, settings, aliens, alien_number, row_number)
    
def get_number_row(settings, ship_height, alien_height):
    """ Obtendremos el numero de filas que se pueden generar """
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    
    return number_rows



 
        