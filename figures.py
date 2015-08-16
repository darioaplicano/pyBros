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
        self.resolution = (50, 90)
        self.images = imagesMario
        self.soilLevel = soilLevel
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.invert = False
        self.press_time = 0
        self.image_cont = 0
        self.rect_temp = 0
        self.vector = [False,True,False]
        self.contador = 0



    #def update(self):
    #    '''
    #    Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario
    #
    #    variables:
    #    '''
    #    if vector[1]:
    #        if self.imageNumber >= 0 and self.imageNumber <= 3:
    #            self.imageNumber += 1
    #        if self.imageNumber == 4:
    #            self.imageNumber = 0
    #
    #    self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
    #    if self.invert:
    #        self.image = pygame.transform.flip(self.image, self.invert, False)
    #    if self.imageNumber == 6 :
    #        self.imageNumber = 1
    #        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

    def changeImage(self):
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)
        if self.invert:
            self.image = pygame.transform.flip(self.image, self.invert, False)

    def update(self):
           if self.vector == [True,False,False]:
               self.imageNumber = 2
               self.changeImage()
               self.vector = [False,False, False]
           elif self.vector[1] :
               self.imageNumber = 0
               self.changeImage()
               self.vector =  [False,False, False]
           elif self.vector == [False,True,True]:
               self.rect = self.rect_temp
               self.rect.size = self.resolution
               self.imageNumber = 0
               self.changeImage()











    def everDown(self,down):
        if down :
             self.rect.move_ip(0, 4)
             self.vector = [True,False,False]

        else :
            self.rect.move_ip(0,0)
            self.vector[1] = [False,True,False]

    def run(self, key):
        if (key == pygame.K_LEFT):
            self.rect.move_ip(-5, 0)

            self.invert = True
        if (key == pygame.K_RIGHT):
            self.rect.move_ip(5, 0)
            self.invert = False

    def crouch(self, jumping,falling):
        resolution = (40,49)
        self.imageNumber = 6

        if not jumping and not falling:
            self.image = pygame.transform.scale(self.images[self.imageNumber],resolution)
            self.rect_temp = self.rect
            self.rect.size = resolution
            self.rect.top = self.rect_temp.top + 40
            if self.invert:
                self.image = pygame.transform.flip(self.image, self.invert, False)
            self.vector = [False,True,True]
        if falling :
            self.image = pygame.transform.scale(self.images[self.imageNumber],resolution)
            if self.invert:
                self.image = pygame.transform.flip(self.image, self.invert, False)
            self.vector = [True,False,True]


    def stopped(self):
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber],self.resolution)

    def jump(self,press):
        jump = 4
        move = 2
        self.imageNumber = 4
        self.image = pygame.transform.scale(self.images[self.imageNumber], self.resolution)

        self.press_time +=1

        if press:
            if self.press_time <=10:
                self.rect.move_ip(move,-move*move*self.press_time)
        else:
            if self.press_time <=10:
                self.rect.move_ip(0,-jump*self.press_time)
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
        self.resolution = (50, 50)
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
        self.resolution = (1280, 70)
        self.image = pygame.transform.scale(imageFloor, self.resolution)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy

class panel(pygame.sprite.Sprite):
    def __init__(self, imagePanel, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (1280, 80)
        self.image = pygame.transform.scale(imagePanel, self.resolution)
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
    def __init__(self, imageH, posX, posY):
        # Intancializar la clase sprite
        pygame.sprite.Sprite.__init__(self)
        self.randomt = random.uniform(0.4, 2)
        # Cargamos la imagen del martillo
        self.image = imageH
        self.size=(35,45)
        self.image = pygame.transform.scale(self.image, self.size)
        # Dibuja una superficie segun el tamanio de la imagen
        self.rect = self.image.get_rect()
        # Posicion inicial del martillo
        self.rect.center = [posX, posY]
        # La gravedad que es cte
        self.gravity = 1
        # El tiempo
        self.timeH = self.randomt
        # Velocidad inicial
        self.vO = 16
        # El angulo de 45 grados
        self.angle = 30
        self.rectHammer= []

    def throwHammer(self):
         # Calcular la velocidad inicial en x
        self.voX = self.vO * (math.cos(math.radians(self.angle)))
        # Calcular la velcidad inicial en y
        self.voY = self.vO * (math.sin(math.radians(self.angle)))
        speed = [-(self.voX), (self.voY)]
        # Incrementa o disminuye la velocidad en y por la formula
        speed[1] -= (self.gravity * self.timeH * self.timeH)
        # Movimiento del martillo
        self.rect.move_ip(speed[0], speed[1])

    def drawHammer(self, screen):
        self.image = pygame.transform.rotate(self.image, 90)
        screen.blit(self.image, self.rect)
        self.throwHammer()

class enemy(pygame.sprite.Sprite):
     # Inicializa la clase
    def __init__(self, images, smallhammer, posX, posY, listBricks):
        # Intancializar la clase sprite
        pygame.sprite.Sprite.__init__(self)
        # Obtener lista de todas las imagenes del sprite
        self.listImages = images
        # Tamaño del enemigo y el martillo
        self.size = (70,80)
        # Imagen del martillo
        self.imageSH = smallhammer
        self.listB = self.rectBricks(listBricks)
        # Variable para la primera posicion que esta la imagen
        self.firstImage = 0
        # El tamanio del objeto en x
        self.tamObject = 260
        self.tamObjectCopy = self.tamObject
        # Variable para cambio direccion
        self.n = 1
        # Tamanio de la lista de imagenes
        self.lastImage = len(self.listImages) - 1
        # Carga la primera imagen
        self.image = pygame.transform.scale(self.listImages[0], self.size)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rectHammer = self.image.get_rect()
        self.rectHammer.left = posX
        self.posX = posX
        self.posY = posY
        self.rectHammer.top = posY
        # Posicion de imagen en la pantalla
        self.position = [posX, posY]
        self.listSmallHammers = []  # Lista de hammers
        self.recentImage = 0
        # Bandera de comprobacion para el lanzamiento de martillo
        self.flag = False
        #cntador para cada tiempo que tiene que saltar el hammer
        self.counter=0
        self.down = True
        self.timer = 0 #Tiempo para tirar el martillo
        self.throw = False
        self.lvl = 1

    def rectBricks(self, listBricks):
        listRect = []
        for brick in listBricks:
            self.rectBrick = pygame.Rect((brick.rect.left, brick.rect.top),(brick.resolution))
            # La superficie de los bricks se agregan a una lista
            listRect.append(self.rectBrick)
        return listRect

    # Esta funcion fue creada para guardar todos los martillos
    # Recibiendo paramatros de la posicion actual del martillo
    def saveSmallHammer(self, posXH, posYH):
        # Cracion de objeto killerHammer temporal
        khammer = smallHammer(self.imageSH, posXH, posYH)
        # Se agrega a la lista el objeto anterior para guardar el martillo
        self.listSmallHammers.append(khammer)

    #Esta funcion es para el salto del Hammer segun el nivel
    def jump(self, lvl):
        if lvl > 1:
            if self.down:
                if self.posY > self.tamObject/ 3 :
                    self.posY -= 30
                else: self.down = False
            else:
                if self.rectHammer.collidelist(self.listB) > -1:
                    self.counter = 0
                    self.down = True
                else: self.posY += 30

    def update(self):
        self.flag = False
        self.throw = False
        # Tiempo que dura en permanecer una imagen
        if self.tamObject == 0:
            # Cambio de signo a la variable
            self.n = -(self.n)
            # Asignacion de su valor original
            self.tamObject = self.tamObjectCopy
        # Nueva posicion en x del Sprite
        self.posX -= self.n
        self.tamObject -= 1
        if self.counter > 20:
            self.jump(self.lvl)
        if self.timer == 10: #comprueba el contador
            self.throw = True
            self.timer = 0 #Asigna de nuevo cero al timer
        else:
            self.timer += 1 # se incrementa si es falso
        # Para controlar el rango de la lista de imagenes
        if self.firstImage > self.lastImage:
            self.firstImage = 0 # Se asigna cero para que recorra de nuevo la lista
            self.flag = True
        # Carga la siguiente imagen y se le asigana la posicion
        self.image = pygame.transform.scale(self.listImages[self.firstImage], self.size)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rectHammer =self.image.get_rect()
        self.rectHammer.left = self.posX
        self.rectHammer.top = self.posY
        self.position = [self.posX, self.posY]
        self.firstImage += 1 #Incremento para la siguiente imagen
        self.counter += 1 # Incremento en el contador para el salto