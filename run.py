# -*- encoding: utf-8 -*-
#!/usr/bin/env python


#Se importan los archivos necesarios para la correcta ejecucion del juego
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
        pygame.display.set_caption('pyBros '+str(pygame.ver))

        #Instanciamos variables a los archivos externos necesarios.
        self.loads = loads.loads()
        self.figureMario = figures.mario(self.loads.imagesMario, 150, 573)
        self.main_mario = figures.main_mario(self.loads.main_Mario, 333, 200)
        self.hammer = figures.enemy(self.loads.imagesHammer, self.loads.smallHammer, 1050, 433)
        self.brick = figures.brick(self.loads.brick, 800, 500)
        self.bush = figures.bush(self.loads.imagesBush, 387, 208)
        self.bone = figures.bone(self.loads.imagesBones, 918,486)
        self.point = figures.point(self.loads.imagesPoint, 556, 334)
        self.flower = figures.flower(self.loads.imagesFlower, 380, 360)

        #Iniciamos la pantalla de bienvenida
        splashScreen.splashScreen(self.screen, self.loads.pyBros_Logo, self.width/2, self.height/2)

        #Esta variable representa la inexistencia del evento type quit de pygame, tal que mientras sea False el
        #juego funcionará bien, sin embargo al llegar a ser True, este se cesarra automaticamente.
        self.out = False

        #Variables necesarias para el buen funcionamiento del menú pausa
        self.outPause = False #En este caso se sale del menu pausa
        self.selected = 0
        self.total = 0

        #Realiza la activación y desactivación de los movimientos de mario
        self.key = pygame.KEYUP
         
        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()

    '''
        Este metodo contiene la logica total del juego, donde se maneja un ciclo infinito hasta la escucha de cualquier
        evento
    '''
    def run(self):
        #Musica de fondo de entrada del juego
        pygame.mixer.music.load('Music/backgroundSounds/background_musicPrincipal.mp3')
        while not self.out:
            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()
            
            # AQUI TODA LA LÓGICA DEL JUEGO
            self.screenPaint()

            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            self.reloj.tick(5)

    '''
        Este método escucha todos los eventos realizados ya sea por el mouse o el teclado, además que inicializa
        la variable motionActivated, la cual permite la activación y desactivacion de los movimientos de mario
    '''
    def listenEvent(self):
        #Se esperan todos los eventos producidos por el teclado y ratón del computador
        for event in pygame.event.get():
            #Si esta decision llega a retornar verdadero, se cerrará automáticamente la pantalla del juego
            if event.type == pygame.QUIT:
                self.out = True
            #Si esta decision llega a retornar verdadero, se guardara la tecla persionada y se activara motionActivated
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause()
                    self.outPause = False
                if event.key == pygame.K_RETURN:
                    levels.level1(self.screen, self.resolution, self.loads.background_stage1,
                                  self.loads.jumping_SoundMario, self.loads.floor_stage1, self.brick, self.figureMario,
                                  self.hammer)

    def listenEventPause(self):
        for event in pygame.event.get():
            #Si esta decision llega a retornar verdadero, se cerrará automáticamente la pantalla del juego
            if event.type == pygame.QUIT:
                sys.exit(0)
            #Si esta decision llega a retornar verdadero, se guardara la tecla persionada y se activara motionActivated
            if event.type == pygame.KEYDOWN:
                self.loads.travel_Principal.play()
                if event.key == pygame.K_UP:
                    if self.selected > 0:
                        self.selected -= 1
                    else:
                        self.selected = 3
                if event.key == pygame.K_DOWN:
                    if self.selected < self.total-1:
                        self.selected += 1
                    else:
                        self.selected = 0
                if event.key == pygame.K_RETURN:
                    if self.selected == 2:
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
        imageBackGround = pygame.transform.scale(self.loads.main_Screen,(self.resolution))
        self.screen.blit(imageBackGround,(0,0))
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
        #Pintamos 5 flores
        self.screen.blit(self.flower.image, self.flower.rect)
        self.screen.blit(self.flower.image, (440, 360))
        self.screen.blit(self.flower.image, (320, 360))
        self.screen.blit(self.flower.image, (440, 303))
        self.screen.blit(self.flower.image, (440, 417))
        #Pintamos a mario moviendose para que se desplace por los caminos en la pantalla principal
        self.screen.blit(self.main_mario.image, self.main_mario.rect)
        self.update()

    '''
        Este método de clase, actualiza los personajes para sus movimientos
    '''
    def update(self):
        self.main_mario.update()
        self.point.update()
        self.bone.update()
        self.flower.update()
        self.bush.update()

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
            #Se pinta la superficie sobre la imagen
            self.screen.blit(background_pause,(self.width/2 - width/2, self.height/2 - height/2))
            for option in options:
                if self.selected == counter:
                    fungus = pygame.transform.scale(self.loads.fungus, (25,25))
                    self.screen.blit(fungus, (self.width/2 - width/2, self.height/2 - height/2 + 10 + counter * 50))
                text = self.loads.font_Mario.render(option[0], 0, (255,255,255,255))
                self.screen.blit(text, (self.width/2 - width/2 + 30, self.height/2 - height/2 + 10 + counter * 50))
                counter += 1
            pygame.display.flip()
        self.loads.pause.play()

#Se crea una instancia al juego para comenzar el mismo
iniciar = main()
iniciar.run()