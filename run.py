# -*- encoding: utf-8 -*-
#!/usr/bin/env python


#Se importan los archivos necesarios para la correcta ejecucion del juego
import pygame
import loads
import figures
import splashScreen
import pygame.event

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
        self.height= 500

        #Creamos el area de trabajo y visualizacion de archivos
        self.resolucion = (self.width, self.height)
        self.workSpace = pygame.display.set_mode(self.resolucion)
        pygame.display.set_caption('pyBros '+str(pygame.ver))

        #Instanciamos variables a los archivos externos necesarios.
        self.loads = loads.loads()
        self.figureMario = figures.mario(self.loads.imagesMario, 150, 300)

        #Iniciamos la pantalla de bienvenida
        splashScreen.splashScreen(self.workSpace, self.loads.pyBros_Logo, self.width/2, self.height/2)

        #Esta variable representa la inexistencia del evento type quit de pygame, tal que mientras sea False el
        #juego funcionará bien, sin embargo al llegar a ser True, este se cesarra automaticamente.
        self.out = False

        #Realiza la activación y desactivación de los movimientos de mario
        self.motionActivated = False
        self.combinationKeyActivated = False
        self.key = pygame.KEYUP
        self.combinationKey = pygame.KEYUP
         
        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()

    '''
        Este metodo contiene la logica total del juego, donde se maneja un ciclo infinito hasta la escucha de cualquier
        evento
    '''
    def run(self):
        #Musica de fondo de entrada del juego
        pygame.mixer.music.load('Music/backgroundSounds/smb3_whistle.wav')
        pygame.mixer.music.play(-1)
        while not self.out:
            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()
            
            # AQUI TODA LA LÓGICA DEL JUEGO
            self.mariosMoves()
            self.screenPaint()

            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            self.reloj.tick(20)

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
                if not self.motionActivated:
                    if event.key == pygame.K_RIGHT:
                        self.key = pygame.K_RIGHT
                        print self.key
                    if event.key == pygame.K_LEFT:
                        self.key = pygame.K_LEFT
                        print self.key
                    if event.key == pygame.K_UP:
                        self.key == pygame.K_UP
                        print self.key
                    self.motionActivated = True
                else:
                    if event.key == pygame.K_RIGHT:
                        self.combinationKey = pygame.K_RIGHT
                        print self.combinationKey
                    if event.key == pygame.K_LEFT:
                        self.combinationKey = pygame.K_LEFT
                        print self.combinationKey
                    if event.key == pygame.K_UP:
                        self.combinationKey == pygame.K_UP
                        print self.combinationKey
                    self.combinationKeyActivated = True
            #Si esta decision llega a retornar verdadero, se guardará el tipo de evento y se desactivará motionActivated
            if event.type == pygame.KEYUP:
                self.key = pygame.KEYUP
                self.motionActivated = False

    '''
        Este método de clase, maneja el comportamiento de mario
    '''
    def mariosMoves(self):
        #Si esta decisión llega a retornar verdadero, se realizarán los movimientos en mario, sino mario se detendrá
        if self.motionActivated:
            if self.key == pygame.KEYUP:
                self.key = pygame.K_UP
            self.figureMario.update(self.key, self.loads.jumping_SoundMario)
            if self.combinationKeyActivated:
                self.figureMario.update(self.combinationKey, '')
        else:
            if self.key == pygame.KEYUP:
                self.figureMario.update(self.key, '')

    '''
        Este método de clase, pinta en el área de trabajo todo lo necesario para la parte vistosa del juego
    '''
    def screenPaint(self):
        # Pintado de pantalla
        self.workSpace.fill((255,255,255))
        imageBackGround = pygame.transform.scale(self.loads.backGround_Image,(self.resolucion))
        self.workSpace.blit(imageBackGround,(0,0))
        self.workSpace.blit(self.figureMario.image, self.figureMario.rect)

#Se crea una instancia al juego para comenzar el mismo
iniciar = main()
iniciar.run()