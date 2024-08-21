import pygame

# Inicializamos pygame
pygame.init()

ANCHO = 450
ALTO = 450

# Creamos la ventana
VENTANA = pygame.display.set_mode([ANCHO, ALTO])

# Color de fondo (gris claro)
COLOR_FONDO = (200, 200, 200)  # RGB (gris claro)

# Variable para controlar el bucle del juego
jugando = True

while jugando:
    # Capturamos eventos
    eventos = pygame.event.get()
    
    # Procesamos los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False 
    
    # Rellenamos el fondo con el color elegido
    VENTANA.fill(COLOR_FONDO)
    
    # Actualizamos la pantalla
    pygame.display.update()

# Salimos de pygame
pygame.quit()


