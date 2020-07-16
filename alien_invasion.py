import sys # Libreria que permite salir del juego una vez que lo decida el jugador
import pygame # Contiene todos los elementos para crear un videjuego

def run_game():
    """ Función principal para ejecutar el juego """
    
    # Inicializa la configuración de fondo para que pygame pueda funcionar correctamente
    pygame.init() 
    
    # Establecemos las propiedades de la ventana, dando una tupla como argumento
    screen = pygame.display.set_mode((1200, 800))
    
    # Definimos un titulo en la ventana del juego
    pygame.display.set_caption("Alien Invasion")
    
    # Creamos una tupla que almacena el color de fondo
    bg_color = (93, 109, 126)
    
    # Declaramos un ciclo principal del juego
    while True:
        # Observamos los eventos generados por el teclado y el mouse
        for event in pygame.event.get(): # obtenemos los eventos generados
            
            # Evaluamos el evento que genere el jugador durante el juego, 
            # para decidir si salimos del juego
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Asignamos el color al fondo de la ventana
        screen.fill(bg_color)
            
        # Dibuja la ventana mas actual que creamos, por lo que cada vez que se actualice
        # Solo estarán los elementos de la nueva ventana
        pygame.display.flip()                             
        
# Ejecutamos nuestra función principal        
run_game()