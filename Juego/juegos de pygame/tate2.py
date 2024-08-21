import pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Triqui")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CELESTE = (0, 255, 255)
BLANCO = (255, 255, 255)

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
    pygame.draw.line(screen, ROJO, (x, y), (x + 100, y + 100), 5)
    pygame.draw.line(screen, ROJO, (x + 100, y), (x, y + 100), 5)

# Función para dibujar un círculo
def dibujar_circulo(x, y):
    pygame.draw.circle(screen, CELESTE, (x + 50, y + 50), 50, 5)

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
