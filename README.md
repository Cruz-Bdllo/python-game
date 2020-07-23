# Alien Invasión con PYTHON y PyGame
## Descripción
- Este repositorio contiene el proyecto número 1 del libro  **Python Crash Course 2da edición** del autor **Eric Matthes**.
- Versiones y herramientas usadas:
    >- Python 3.8.3
    >- Pygame 1.9.6
    >- Eclipse 2020-06 (4.6)
    >- Git 2.27

## Objetivo
- Teniendo conocimientos básicos sobre POO, funciones y estructuras de datos (diccionarios, listas y tuplas) poder usar la biblioteca pygame, la cual permite el desarrollo de videojuegos en 2D.
- Conocer el entorno y ambiente de **pygame**.
- Estructuración y organización del sistema de archivos generados en un proyecto de desarrollo.
- Usar buenas prácticas de programación basado en PEP 8.
- Manejo para la captura de eventos generados por la entrada estandar.

## Jugabilidad
- En Alien Invasion, el jugador controla una nave que aparece en la parte
inferior centrado de la pantalla.
- El jugador puede mover la nave hacia la derecha o hacia la izquierda con las teclas de dirección 
y disparara usando la barra espaciadora.
- El jugador podrá salir del juego ya sea cerrando la ventana o presionando la tecla **q**.
- Cuando el juego comienza, una flota de aliens llena la parte superior moviendose a hacia los lados y hacia abajo de la pantalla.
- El jugador disparará y destruira a los aliens, si el jugador elimina a todos los aliens una nueva flota deberá aparecer siendo esta mas rapida que la flota anterior.
- Al eliminar un flota completa se incrementara la dificultad del juego incrementando la velocidad.
- Al eliminar un alien el jugador ira sumando puntos.
- Si un alien golpea al jugar o alcanza la parte inferior donde se encuentra la nave del jugador este perdera una vida.
- Si el jugador pierde 3 de sus vidas el juego termina. 

### Enlaces
>- Libro **Python Crash Course** 2da edición.
	- [https://nostarch.com/pythoncrashcourse2e](https://nostarch.com/pythoncrashcourse2e)

### Imagenes
- Pantalla principal
	- ![imagen-init][img-init]
- Eliminación de aliens
	- ![imagen-del][img-del]
- Siguiente nivel
	- ![imagen-sig][img-next]




[img-init]: https://raw.githubusercontent.com/Cruz-Bdllo/python-game/master/images_game/pantalla_inicial.png "Pantalla de inicio"
[img-del]: https://raw.githubusercontent.com/Cruz-Bdllo/python-game/master/images_game/eliminar_aliens.png "Eliminando aliens"
[img-next]: https://raw.githubusercontent.com/Cruz-Bdllo/python-game/master/images_game/sig_nivel.png "Siguiente nivel"
