# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame
import math
import random

'''
    Esta es la clase donde se cargan los personajes en todo el juego, el comportamiento de todos estos en cada momento
'''
class mario(pygame.sprite.Sprite):
    def __init__(self, imagesMario, posx, posy, soilLevel):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (75, 87)
        self.images = imagesMario
        self.soilLevel = soilLevel
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.invert = False
        self.initial = 0

    '''
        Este metodo tiene como fin modelar los comportamientos de mario, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado que interviene en los
                movimientos de mario.
    '''
    def update(self):
        '''
        Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

        variables:
        '''
        if self.imageNumber >= 0 and self.imageNumber <= 3:
            self.imageNumber += 1
        if self.imageNumber == 4:
            self.imageNumber = 0

        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        if self.invert:
            self.image = pygame.transform.flip(self.image, self.invert, False)

    def moveUp(self, move = 1):
        self.rect.move_ip(0, -move)

    def everDown(self):
        self.rect.move_ip(0, 1)

    def run(self, key):
        if (key == pygame.K_LEFT):
            self.rect.move_ip(-20, 0)
            self.invert = True
        if (key == pygame.K_RIGHT):
            self.rect.move_ip(20, 0)
            self.invert = False

    def stopped(self):
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

    def jump(self):
        # solo evalúa un salto si está en el suelo.
        self.initial = -28
        self.imageNumber = 4
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        if self.invert:
            self.image = pygame.transform.flip(self.image, self.invert, False)

    def updateJump(self):
        # si está saltando actualiza su posición
        self.rect.y += self.initial
        self.initial += 3

'''
    Esta clase representa el mario que se desplaza a traves de los niveles para seleccionar cual jugar
'''
class main_mario(pygame.sprite.Sprite):
    def __init__(self, imagesMario, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (50, 60)
        self.images = imagesMario
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos de mario, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado que interviene en los
                movimientos de mario.
    '''
    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 1:
            self.imageNumber += 1
        if self.imageNumber == 2:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

    def movesMario(self, key, value = 30):
        if key == pygame.K_DOWN:
            self.rect.move_ip(0, value)
        if key == pygame.K_UP:
            self.rect.move_ip(0, -value)
        if key == pygame.K_LEFT:
            self.rect.move_ip(-value, 0)
        if key == pygame.K_RIGHT:
            self.rect.move_ip(value, 0)

'''
    Esta clase representa los bloques de nivel o mundo en el que se posicionará mario para entrar a el mismo
'''
class level(pygame.sprite.Sprite):
    def __init__(self, imagesLevel, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (50, 50)
        self.images = imagesLevel
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy
    '''
        Este metodo tiene como fin modelar los comportamientos de mario, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado que interviene en los
                movimientos de mario.
    '''
    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 1:
            self.imageNumber += 1
        if self.imageNumber == 2:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class brick(pygame.sprite.Sprite):
    def __init__(self, imagesBrick, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (40, 50)
        self.images = imagesBrick
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos del bloque donde se para hammerbros, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
        movimientos del bloque donde se para hammerbros.
    '''

    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 3:
            self.imageNumber += 1
        if self.imageNumber == 4:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class floor(pygame.sprite.Sprite):
    def __init__(self, imageFloor, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (1280, 100)
        self.image = pygame.transform.scale(imageFloor, self.resolution)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy

class bush(pygame.sprite.Sprite):
    def __init__(self, imagesBush, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (55, 45)
        self.images = imagesBush
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos del bloque donde se para hammerbros, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
        movimientos del bloque donde se para hammerbros.
    '''

    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 2:
            self.imageNumber += 1
        if self.imageNumber == 3:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class bone(pygame.sprite.Sprite):
    def __init__(self, imagesBone, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (53, 50)
        self.images = imagesBone
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos del bloque donde se para hammerbros, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
        movimientos del bloque donde se para hammerbros.
    '''

    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 2:
            self.imageNumber += 1
        if self.imageNumber == 3:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class point(pygame.sprite.Sprite):
    def __init__(self, imagesPoint, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (30, 30)
        self.images = imagesPoint
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos del bloque donde se para hammerbros, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
        movimientos del bloque donde se para hammerbros.
    '''

    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 2:
            self.imageNumber += 1
        if self.imageNumber == 3:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class flower(pygame.sprite.Sprite):
    def __init__(self, imagesFlower, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (50, 57)
        self.images = imagesFlower
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy

    '''
        Este metodo tiene como fin modelar los comportamientos del bloque donde se para hammerbros, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
        movimientos del bloque donde se para hammerbros.
    '''

    def update(self):
        '''
            Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

            variables:
            '''
        if self.imageNumber >= 0 and self.imageNumber <= 1:
            self.imageNumber += 1
        if self.imageNumber == 2:
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

class castle(pygame.sprite.Sprite):
    def __init__(self, imageCastle, posx, posy, resolution):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageCastle
        self.image = pygame.transform.scale(self.image, resolution)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy

class smallHammer(pygame.sprite.Sprite):
    def __init__(self, image, posX, posY):
        # Intancializar la clase sprite
        pygame.sprite.Sprite.__init__(self)
        # La posicion en x y la posicion en y, del martillo
        self.posX = posX
        self.posY = posY
        self.randomt = random.uniform(0.4, 2)
        # Cargamos la imagen del martillo
        self.sHammer = image
        # Dibuja una superficie segun el tamanio de la imagen
        self.rectH = image.get_rect()
        # Posicion inicial del martillo
        self.rectH.center = [self.posX, self.posY]
        # La gravedad que es cte
        self.gravity = 1
        # El tiempo
        self.timeH = self.randomt
        # Velocidad inicial
        self.vO = 12
        # El angulo de 45 grados
        self.angle = 38

    def throwHammer(self):
        # Calcular la velocidad inicial en x
        self.voX = self.vO * (math.cos((self.angle)))
        # Calcular la velcidad inicial en y
        self.voY = self.vO * (math.sin((self.angle)))
        speed = [-(self.voX), (self.voY)]
        # Incrementa o disminuye la velocidad en y por la formula
        speed[1] -= (self.gravity * self.timeH)
        # Movimiento del martillo
        self.rectH.move_ip(speed[0], speed[1])

    def drawHammer(self, screen):
        # pygame.time.wait(50)
        # Dibuja el martillo en la pantalla
        self.window.blit(self.sHammer, self.rectH)


class enemy(pygame.sprite.Sprite):
    # Inicializa la clase
    def __init__(self, images, smallhammer, posX, posY):
        # Intancializar la clase sprite
        pygame.sprite.Sprite.__init__(self)
        # Obtener lista de todas las imagenes del sprite
        self.listImages = images
        # Imagen del martillo
        self.imageHammer = smallHammer
        # Separa cada imagen
        self.listImages.sort()
        # Variable para la primera posicion que esta la imagen
        self.firstImage = 0
        # El tamanio del objeto en x
        self.tamObject = 260
        self.tamObjectCopy = self.tamObject
        # Variable para cambio direccion
        self.n = 1
        # Tamanio de la lista de imagenes
        self.lastImage = len(self.listImages) - 1
        # Tamaño del enemigo
        self.size = (60,70)
        # Carga la primera imagen
        self.image = pygame.transform.scale(self.listImages[0], self.size)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rectHammer = self.image.get_rect()
        self.posX = posX
        self.posY = posY
        # Posicion de imagen en la pantalla
        self.position = [posX, posY]
        # La pantalla
        # Lista de hammers
        self.listSmallHammers = []
        self.recentImage = 0
        # Bandera de comprobacion para el lanzamiento de martillo
        self.flag = False
        # Lista de posiciones del martillo
        self.drawHammer = []

    # Esta funcion fue creada para guardar todos los martillos
    # Recibiendo paramatros de la posicion actual del martillo
    def drawSmallHammer(self, posXH, posYH):
        # Cracion de objeto killerHammer temporal
        khammer = smallHammer(self.imageHammer, posXH, posYH)
        # Se agrega a la lista el objeto anterior para guardar el martillo
        self.listSmallHammers.append(khammer)

    def update(self):
        self.flag = False
        # Tiempo que dura en permanecer una imagen
        if self.tamObject == 0:
            # Cambio de signo a la variable
            self.n = -(self.n)
            # Asignacion de su valor original
            self.tamObject = self.tamObjectCopy
        # Nueva posicion en x del sprite
        self.posX -= self.n
        self.tamObject -= 1
        # Para controlar el rango de la lista de imagenes
        if self.firstImage > self.lastImage:
            # Se asigna cero para que recorra de nuevo la lista
            self.firstImage = 0
            self.flag = True
        # Carga la siguiente imagen y se le asigana la posicion
        self.image = pygame.transform.scale(self.listImages[self.firstImage], self.size)
        self.image = pygame.transform.flip(self.image, True, False)
        self.position = [self.posX, self.posY]
        # Dibuja la imagen en la pantalla
        self.firstImage += 1