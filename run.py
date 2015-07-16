# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame
import loads
import figures
import splashScreen
import levels
import sys

'''
    Esta es la clase principal en todo el juego, contiene todos los métodos necesarios para una estadía agradable en
    el juego
'''
class main:
    '''
        Es el inicializador del juego, mediante este método de clase, se puede inicializar el area de juego, colocar
        un nombre y version del mismo, además de cargar todo lo necesario para divertido y fluido momento de
        entretenimiento
    '''
    def __init__(self):
        #Inicializa todos los componentes de pygame
        pygame.init()

        #resolución de la pantalla.
        self.width = 1280
        self.height= 720

        #Creamos el area de trabajo y visualizacion de archivos
        self.resolution = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('pyBros '+ str(pygame.ver))

        #Instanciamos variables a los archivos externos necesarios.
        self.loads = loads.loads()
        self.imageBackGround = pygame.transform.scale(self.loads.main_Screen,(self.resolution))
        self.main_mario = figures.main_mario(self.loads.main_Mario, 333, 200)
        self.bush = figures.bush(self.loads.imagesBush, 387, 208)
        self.bone = figures.bone(self.loads.imagesBones, 918,486)
        self.point = figures.point(self.loads.imagesPoint, 556, 334)
        self.flower = figures.flower(self.loads.imagesFlower, 380, 360)
        self.level1 = figures.level(self.loads.imagesLevel, 215, 200)
        self.level2 = figures.level(self.loads.imagesLevel, 215, 100)
        self.level3 = figures.level(self.loads.imagesLevel, 440, 100)
        self.level4 = figures.level(self.loads.imagesLevel, 705, 210)
        self.level5 = figures.level(self.loads.imagesLevel, 830, 110)
        self.level6 = figures.level(self.loads.imagesLevel, 1020, 100)
        self.level7 = figures.level(self.loads.imagesLevel, 273, 422)
        self.level8 = figures.level(self.loads.imagesLevel, 273, 310)
        self.level9 = figures.level(self.loads.imagesLevel, 650, 320)
        self.castle1 = figures.castle(self.loads.castle, 648, 418, (55, 57))
        self.castle2 = figures.castle(self.loads.castle, 758, 418, (55, 57))
        self.castle3 = figures.castle(self.loads.bowser_castle, 921, 368, (108, 110))

        #Iniciamos la pantalla de bienvenida
        splashScreen.splashScreen(self.screen, self.loads.backgroundSplas, self.loads.floorSplas, self.width/2, self.height/2)

        #Esta variable representa la inexistencia del evento type quit de pygame, tal que mientras sea False el
        #juego funcionará bien, sin embargo al llegar a ser True, este se cerarra automaticamente.
        self.out = False

        #Variables necesarias para el buen funcionamiento del menú pausa
        self.outPause = False #En este caso se sale del menu pausa
        self.selected = 0
        self.total = 0

        #Realiza la activación y desactivación de los movimientos de mario
        self.key = pygame.KEYUP
        self.move = True
        self.levelCollision = 0
        self.collision = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()

    '''
        Este método contiene la lógica total del juego, donde se maneja un ciclo infinito hasta la escucha de cualquier
        evento
    '''
    def run(self):
        #Música de fondo de entrada del juego
        pygame.mixer.music.load('Music/backgroundSounds/background_musicPrincipal.mp3')
        pygame.time.set_timer(pygame.USEREVENT, 250)
        while not self.out:
            # Esta función tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()

            # Esta función tiene el fin de pintar todos los objetos en el área de juego
            self.screenPaint()

            #Esta función mueve el personaje de mario
            self.movesMario()

            #Se valida la colisión de mario con los objetos de los niveles
            self.validateCollisions()

            # Limita a 60 fotogramas por segundo el pintado de la pantalla
            self.reloj.tick(60)
            pygame.display.flip()

    '''
        Este método escucha todos los eventos realizados ya sea por el ratón o el teclado, capturando la tecla
        presionada la cual permite la direccion de los movimientos de mario
    '''
    def listenEvent(self):
        #Se esperan todos los eventos producidos por el teclado y ratón del computador
        for event in pygame.event.get():
            #SI esta decision llega a retornar verdadero se actualizaran las imagenes para manejar el movimiento de las cosas
            if event.type == pygame.USEREVENT:
                self.update()
            #Si esta decisiṕn llega a retornar verdadero, se cerrará automáticamente la pantalla del juego
            if event.type == pygame.QUIT:
                self.out = True
            #Si esta decisión llega a retornar verdadero, se guardará la tecla persionada
            if self.move == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause()
                        self.outPause = False
                    if event.key == self.loads.moves_MainMario[self.levelCollision][3][0] or event.key == self.loads.moves_MainMario[self.levelCollision][3][1]:
                        self.key = event.key
                        self.move = False
                    #Si el evento representa la presión de la tecla return, se verificará si es permitido el acceso al
                    #nivel correspondiente
                    if event.key == pygame.K_RETURN:
                        self.levels()

    '''
        Este método tiene un fin muy parecido a listenEvent, sin embargo, éste método solo funciona cuando se ha
        activado el método pause(), desplazandose entre las opciones
    '''
    def listenEventPause(self):
        for event in pygame.event.get():
            #Si esta decisión llega a retornar verdadero, se cerrará automáticamente la pantalla del juego
            if event.type == pygame.QUIT:
                self.outPause = True
            #Si esta decisión llega a retornar verdadero, se reproducirá un sonido de cambio de opción, además de eso
            #se intercalará la opción seleccionada
            if event.type == pygame.KEYDOWN:
                self.loads.travel_Principal.play()
                if event.key == pygame.K_UP:
                    if self.selected > 0:
                        self.selected -= 1
                    else:
                        self.selected = self.total - 1
                if event.key == pygame.K_DOWN:
                    if self.selected < self.total-1:
                        self.selected += 1
                    else:
                        self.selected = 0
                if event.key == pygame.K_RETURN:
                    if self.selected == 2 or self.selected == 0:
                        self.outPause = True
                    if self.selected == 3:
                        sys.exit(0)
                if event.key == pygame.K_BACKSPACE:
                    self.outPause = True

    '''
        Este método de clase, pinta en el área de trabajo todo lo necesario para la parte vistosa del juego
    '''
    def screenPaint(self):
        # Pintado de pantalla
        self.screen.fill((255,255,255))
        self.screen.blit(self.imageBackGround,(0,0))
        #Pintamos 7 captus bailarines en la pantalla principal
        self.screen.blit(self.bush.image, self.bush.rect)
        self.screen.blit(self.bush.image, (330, 156))
        self.screen.blit(self.bush.image, (490, 156))
        self.screen.blit(self.bush.image, (647, 151))
        self.screen.blit(self.bush.image, (752, 151))
        self.screen.blit(self.bush.image, (647, 103))
        self.screen.blit(self.bush.image, (752, 103))
        #Pintamos 2 calaberas con ojos brillantes
        self.screen.blit(self.bone.image, self.bone.rect)
        self.screen.blit(self.bone.image, (974,486))
        #Pintamos 2 puntos brillantes
        self.screen.blit(self.point.image, self.point.rect)
        self.screen.blit(self.point.image, (836, 226))
        #Pintamos 5 flores come carne
        self.screen.blit(self.flower.image, self.flower.rect)
        self.screen.blit(self.flower.image, (440, 360))
        self.screen.blit(self.flower.image, (320, 360))
        self.screen.blit(self.flower.image, (440, 303))
        self.screen.blit(self.flower.image, (440, 417))
        #Pintamos los bloques de nivel
        self.screen.blit(self.level1.image, self.level1.rect)
        self.screen.blit(self.level2.image, self.level2.rect)
        self.screen.blit(self.level3.image, self.level3.rect)
        self.screen.blit(self.level4.image, self.level4.rect)
        self.screen.blit(self.level5.image, self.level5.rect)
        self.screen.blit(self.level6.image, self.level6.rect)
        self.screen.blit(self.level7.image, self.level7.rect)
        self.screen.blit(self.level8.image, self.level8.rect)
        self.screen.blit(self.level9.image, self.level9.rect)
        self.screen.blit(self.castle1.image, self.castle1.rect)
        self.screen.blit(self.castle2.image, self.castle2.rect)
        self.screen.blit(self.castle3.image, self.castle3.rect)
        #Pintamos a mario desplazandose por los caminos en la pantalla principal
        self.screen.blit(self.main_mario.image, self.main_mario.rect)
        #Se pinta un poligono donde internamente se pintara una M, representando que se juega con mario y otros textos
        posX = 560
        posY = 646
        pygame.draw.polygon(self.screen, (0,0,0), [[posX, posY],           [posX + 5, posY],       [posX + 5, posY - 5],
                                                   [posX + 45, posY - 5],  [posX + 45, posY],      [posX + 50, posY],
                                                   [posX + 50, posY + 15], [posX + 45, posY + 15], [posX + 45, posY + 20],
                                                   [posX + 5,  posY + 20], [posX + 5,  posY + 15], [posX, posY + 15]], 5)
        text = self.loads.font_Mario.render("m", 2, (255, 255, 255, 255))
        self.screen.blit(text, (577, 638))
        text = self.loads.font_Mario2.render("x", 2, (0, 0, 0, 255))
        self.screen.blit(text, (616, 641))
        text = self.loads.font_Mario2.render("world", 2, (255, 255, 255, 255))
        self.screen.blit(text, (558, 616))

    '''
        Este método de clase, actualiza los personajes para sus movimientos
    '''
    def update(self):
        self.main_mario.update()
        self.point.update()
        self.bone.update()
        self.flower.update()
        self.bush.update()
        self.level1.update()
        self.level2.update()
        self.level3.update()
        self.level4.update()
        self.level5.update()
        self.level6.update()
        self.level7.update()
        self.level8.update()
        self.level9.update()

    def movesMario(self):
        self.main_mario.movesMario(self.key)

    def levels(self):
        levels.level1(self.screen, self.resolution, self.loads)

    def fillZero(self):
        for number in range(len(self.collision)):
            self.collision[number] = 0

    def validateCollisions(self):
        if pygame.sprite.collide_mask(self.level1, self.main_mario) and self.collision[0] == 0:
            self.fillZero()
            self.levelCollision = 1
            self.move = True
            self.main_mario.movesMario(self.key, 30)
            self.key = pygame.KEYUP
            self.collision[0] = self.levelCollision
        if pygame.sprite.collide_mask(self.level2, self.main_mario) and self.collision[1] == 0:
            self.fillZero()
            self.levelCollision = 2
            self.move = True
            self.main_mario.movesMario(self.key, 40)
            self.key = pygame.KEYUP
            self.collision[1] = self.levelCollision
        if pygame.sprite.collide_mask(self.level3, self.main_mario) and self.collision[2] == 0:
            self.fillZero()
            self.levelCollision = 3
            self.move = True
            self.main_mario.movesMario(self.key)
            self.key = pygame.KEYUP
            self.collision[2] = self.levelCollision
        if pygame.sprite.collide_mask(self.level4, self.main_mario) and self.collision[3] == 0:
            self.fillZero()
            self.levelCollision = 4
            self.move = True
            self.main_mario.movesMario(self.key)
            self.key = pygame.KEYUP
            self.collision[3] = self.levelCollision

    '''
        Este método de clase, tiene como función pausar el juego  para esperar otros eventos
    '''
    def pause(self):
        self.loads.pause.play()
        options = [("continue",''),
                    ("active agent",''),
                    ("save and continue",''),
                    ("save and quit",'')]
        self.selected = 0
        self.total = len(options)
        width = 400
        height = self.total * 50
        background_pause = pygame.Surface((width,height))
        background_pause.fill((0,0,0))
        while not self.outPause:
            #Cuenta la cantidad de opciones
            counter = 0
            #Llama a los eventos del teclado destinados para pausa
            self.listenEventPause()
            #Se pinta la superficie sobre el área de trabajo
            self.screen.blit(background_pause,(self.width/2 - width/2, self.height/2 - height/2))
            for option in options:
                if self.selected == counter:
                    fungus = pygame.transform.scale(self.loads.fungus, (25,25))
                    self.screen.blit(fungus, (self.width/2 - width/2, self.height/2 - height/2 + 10 + counter * 50))
                text = self.loads.font_Mario.render(option[0], 2, (255,255,255,255))
                self.screen.blit(text, (self.width/2 - width/2 + 30, self.height/2 - height/2 + 10 + counter * 50))
                counter += 1
            pygame.display.flip()
        self.loads.pause.play()

#Se crea una instancia al juego para comenzar el mismo
iniciar = main()
iniciar.run()