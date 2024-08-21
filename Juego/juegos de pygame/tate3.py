import pygame
import time

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Triqui")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CELESTE = (0, 255, 255)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)  # Color para el fondo del mensaje

# Crear el fondo negro
def dibujar_fondo():
    screen.fill(NEGRO)
    
    # Dibujar las líneas del tablero
    pygame.draw.line(screen, BLANCO, (150, 0), (150, 450), 5)
    pygame.draw.line(screen, BLANCO, (300, 0), (300, 450), 5)
    pygame.draw.line(screen, BLANCO, (0, 150), (450, 150), 5)
    pygame.draw.line(screen, BLANCO, (0, 300), (450, 300), 5)

# Función para dibujar una X
def dibujar_x(x, y):
    pygame.draw.line(screen, ROJO, (x + 15, y + 15), (x + 135, y + 135), 5)
    pygame.draw.line(screen, ROJO, (x + 135, y + 15), (x + 15, y + 135), 5)

# Función para dibujar un círculo
def dibujar_circulo(x, y):
    pygame.draw.circle(screen, CELESTE, (x + 75, y + 75), 60, 5)

# Función para mostrar el mensaje de presentación
def mostrar_mensaje(mensaje):
    font = pygame.font.Font(None, 24)  # Ajusta el tamaño del texto
    text = font.render(mensaje, True, BLANCO)
    text_rect = text.get_rect(center=(225, 225))
    pygame.draw.rect(screen, AZUL, (text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20))
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(3)  # Mostrar el mensaje por 3 segundos

# Función para verificar si hay un ganador
def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
            return tablero[0][i]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return tablero[0][2]

    return None

# Inicialización
coor = [[(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)]]
tablero = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]
turno = "X"  # Empieza el turno de X
game_over = False
clock = pygame.time.Clock()

# Mostrar mensaje de presentación
dibujar_fondo()
mostrar_mensaje("Juego desarrollado por Lic. Santino Dacuy")

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            fila = y // 150
            columna = x // 150
            if tablero[fila][columna] == "":
                if turno == "X":
                    tablero[fila][columna] = "X"
                else:
                    tablero[fila][columna] = "O"
                
                # Alternar turno
                turno = "O" if turno == "X" else "X"

                # Verificar si hay un ganador
                ganador = verificar_ganador()
                if ganador:
                    dibujar_fondo()
                    if ganador == "X":
                        mensaje = "Ganador: Jugador 1 (X)"
                    else:
                        mensaje = "Ganador: Jugador 2 (O)"
                    mostrar_mensaje(mensaje)
                    game_over = True
    
    dibujar_fondo()
    
    # Dibujar el tablero según el estado actual
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == "X":
                dibujar_x(columna * 150, fila * 150)
            elif tablero[fila][columna] == "O":
                dibujar_circulo(columna * 150, fila * 150)
    
    pygame.display.update()

pygame.quit()
