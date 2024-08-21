import pygame
pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption ("Triqui")

fondo = pygame.image.load(
    "static/titactoe_backgronud.png"
)
circulo = pygame.image.load(
    "static/circle.png"
)
equis = pygame.image.load(
    "static/x.png"
)

# dale una escala para que se adapte a la pantalla definida  

fondo = pygame.transform.scale ( fondo (450,450))
circulo = pygame.transform.scale ( circulo(100,100))
equis = pygame.transform.scale (equis (100,100))

coor = [[(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0)]]
tablero = [["","",""],
           ["","",""],
           ["","",""]]
turno = "X"
game_over = False
clock = pygame.time.Clock()

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    screen.blit (fondo, (0, 0))
    screen.blit (circulo, (40, 50))
    screen.blit (equis, (160, 165))
    pygame.display.update()
pygame.quit()
