# -*- encoding: utf-8 -*-
#!/usr/bin/env python


#Se importan los archivos necesarios para la correcta ejecucion del juego
import pygame
import loads
import figures
import pygame.event

class main:

    def __init__(self):
        pygame.init()

        #resolucion de la pantalla
        self.width = 1280
        self.height= 500

        #Creamos el area de trabajo
        self.resolucion = (self.width, self.height)
        self.visor = pygame.display.set_mode(self.resolucion)
        pygame.display.set_caption('pyBros '+str(pygame.ver))

        #Instanciamos variables a los archivos externos necesarios
        self.loads = loads.loads()
        self.figureMario = figures.mario(self.loads.imagesMario,150,300)
        
        #Itera hasta que el usuario pincha sobre el botón de cierre.
        self.out = False

        #Realiza la activación y desactivación de los movimientos de mario
        self.motionActivated = False
        self.key = pygame.KEYUP
         
        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()


    def run(self):
        pygame.mixer.music.load('Music/backgroundSounds/smb3_whistle.wav')
        pygame.mixer.music.play(-1)
        while not self.out:
            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()
            
            # AQUI TODA LA LÓGICA DEL JUEGO
            self.mariosMoves()
            self.screenPaint()

            # Limita a 20 fotogramas por segundo
            pygame.display.flip()
            self.reloj.tick(20)

    def listenEvent(self):
        #Se esperan todos los eventos producidos por el teclado y ratón del computador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.out = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.key = pygame.K_RIGHT
                    self.motionActivated = True
                if event.key == pygame.K_LEFT:
                    self.key = pygame.K_LEFT
                    self.motionActivated = True
            if event.type == pygame.KEYUP:
                self.key = pygame.KEYUP
                if event.key == pygame.K_RIGHT:
                    self.motionActivated = False
                if event.key == pygame.K_LEFT:
                    self.motionActivated = False
            print self.figureMario.imageNumber

    def mariosMoves(self):
        if self.motionActivated:
            if self.key == pygame.K_RIGHT:
                self.figureMario.update(self.key)
            if self.key == pygame.K_LEFT:
                self.figureMario.update(self.key)
        else:
            if self.key == pygame.KEYUP:
                self.figureMario.update(self.key)

    def screenPaint(self):
        # Pintado de pantalla
        self.visor.fill((255,255,255))
        imageBackGround = pygame.transform.scale(self.loads.backGround_Image,(self.resolucion))
        self.visor.blit(imageBackGround,(0,0))
        pygame.time.wait(100)
        self.visor.blit(self.figureMario.image, self.figureMario.rect)

#Se crea una instancia al juego para comenzar el mismo
iniciar = main()
iniciar.run()