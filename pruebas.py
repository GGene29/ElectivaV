import pygame,sys
from pygame.locals import *
from random import randint

"Realizaremos pruebas del curso"

#"Nos permite incrustar figuras geométricas"
#"primer valor, lienzo. Segundo, color. 
#"tercero, en tupla (posición en x y y) del punto de inicio. cuarto parametro, tuple de posición final)"
# la ultima y la quinta se refiere al ancho
pygame.init()
ventana_de_juego = pygame.display.set_mode((500,500))
pygame.display.set_caption('Globo')

colorpygame = pygame.Color(25,120,9)
colorline = pygame.Color(230,35,90)

#pygame.draw.line(ventana_de_juego,colorline,(100,100),(200,100),5)
#pygame.draw.line(ventana_de_juego,colorline,(180,200),(300,200),5)
#pygame.draw.line(ventana_de_juego,colorline,(200,400),(150,400),5)
pygame.draw.circle(ventana_de_juego,colorline,(230,150),10)

usernube = pygame.image.load("./img/Bob.png")
usertwo = pygame.image.load("./img/nube.png")
posX = 50
posY = 50
margen = True
velocidad = 10


while True:
    ventana_de_juego.fill(colorpygame)
    pygame.draw.circle(ventana_de_juego,colorline,(230,150),10)
    pygame.draw.line(ventana_de_juego,colorline,(180,200),(300,200),5)
    ventana_de_juego.blit(usernube,(posX,posY))
    
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_LEFT:
                posX -= velocidad
            elif evento.key == K_RIGHT:
                posX += velocidad
            elif evento.key == K_UP:
                posY -= velocidad
            elif evento.key == K_DOWN:
                posY += velocidad

        
    pygame.display.update()

