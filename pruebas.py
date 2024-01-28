import pygame,sys
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()
ventana_de_juego = pygame.display.set_mode((500,500))
pygame.display.set_caption('Globo')

clock = pygame.time.Clock()            #get a pygame clock object

colorpygame = pygame.Color(25,120,9)
colorline = pygame.Color(230,35,90)

class Jugador:
    def __init__(self, posicion, tamaño_colision):
        self.imagen =  pygame.image.load("./img/globo.png")
        self.posicion = posicion
        self.rect_imagen = self.imagen.get_rect()
        self.rect_colision = self.rect_imagen.inflate(-tamaño_colision, -tamaño_colision)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion)

    def mover(self, velocidad, direccion="horizontal"):
        # Actualiza la posición del jugador
        posicion_lista = list(self.posicion)
        if direccion == "horizontal":
            posicion_lista[0] += velocidad
        elif direccion == "vertical":
            posicion_lista[1] += velocidad
        self.posicion = tuple(posicion_lista)
        self.rect_imagen.topleft = self.posicion
        self.rect_colision.topleft = self.posicion


class Nube:
    def __init__(self, posicion, tamaño_colision):
        self.posicion = posicion
        self.imagen = pygame.image.load("./img/nube.png")
        self.ancho, self.alto = self.imagen.get_size()
        ancho_colision, alto_colision = tamaño_colision
        self.rect_colision = pygame.Rect(posicion[0], posicion[1], ancho_colision, alto_colision)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion)

    def mover(self, velocidad, jugador):
        # Obtén los rectángulos de colisión
        rect_jugador = jugador.rect_colision

        # Comprueba si hay una colisión
        if rect_jugador.colliderect(self.rect_colision):
            return

        # Actualiza la posición de la nube
        posicion_lista = list(self.posicion)
        posicion_lista[1] += velocidad_nube
        self.posicion = tuple(posicion_lista)
        self.rect_colision.topleft = (self.posicion[0], self.posicion[1])

        # Restablece la posición de la nube si ha llegado al borde inferior de la ventana
        if self.posicion[1] > 500:
            posicion_lista = list(self.posicion)
            posicion_lista[1] = 0
            self.posicion = tuple(posicion_lista)
            self.rect_colision.topleft = (self.posicion[0], self.posicion[1])


posX = 190
posY = 250
margen = True
velocidad = 10
velocidad_nube = 2
posX_nube = [50, 120, 190, 260, 330, 400]
tamaño_colision = 10

player = Jugador((posX, posY), tamaño_colision)


nubes = []
for i in range(6): # Crea 10 nubes iniciales
    nube = Nube((posX_nube[randint(0, 5)], 0), (40,20))
    nubes.append(nube)
    sleep(randint(1, 3))



juego_comenzado = False
while True:
    ventana_de_juego.fill(colorpygame)
    player.dibujar(ventana_de_juego)


    for nube in nubes:
        nube.dibujar(ventana_de_juego)
        nube.mover(velocidad, player)
    

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                juego_comenzado = True
            
    keys = pygame.key.get_pressed()
    ancho_ventana, alto_ventana = pygame.display.get_surface().get_size()
    ancho_personaje = player.rect_imagen.width
    alto_personaje = player.rect_imagen.height
    limite_superior = int(alto_ventana * 0.1)
    limite_inferior = int(alto_ventana * 0.8)
    limite_derecho = int(ancho_ventana * 0.8)
    limite_izquierdo = int(ancho_ventana * 0.2)


    if juego_comenzado:
        if keys[pygame.K_LEFT] and player.rect_imagen.left > limite_izquierdo:
            player.mover(-velocidad, "horizontal")
        if keys[pygame.K_RIGHT] and player.rect_imagen.right < limite_derecho:
            player.mover(velocidad, "horizontal")
        if keys[pygame.K_UP] and player.rect_imagen.top > limite_superior:
            player.mover(-velocidad, "vertical")
        if keys[pygame.K_DOWN] and player.rect_imagen.bottom < limite_inferior:
            player.mover(velocidad, "vertical")


            
    pygame.display.update()
    clock.tick(60)
