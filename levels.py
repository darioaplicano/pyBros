# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame
import sys
import figures
import Cronometer

class level1(pygame.sprite.Sprite):

    def __init__(self, screen, resolution, loads):
        self.loads =  loads
        self.screen = screen
        self.background = self.loads.background_stage1
        self.efectSound = self.loads.jumping_SoundMario
        self.resolution = resolution
        self.width = self.resolution[0]
        self.height = self.resolution[1]
        self.floor = figures.floor(self.loads.floor_stage1, 0, 650)
        self.brick = figures.brick(self.loads.brick, 800, 480)
        self.figureMario = figures.mario(self.loads.imagesMario, 150, 400, self.floor.rect.top)
        self.hammer = figures.enemy(self.loads.imagesHammer, self.loads.smallHammer, 1050, 433)
        #Realiza la activación y desactivación de los movimientos de mario
        self.key = pygame.KEYUP
        self.out = False
        self.outPause = False
        self.pressed = False

        # Se usa para gestionar cuan rápido se actualiza la pantalla
        #self.reloj = pygame.time.Clock()
        self.cronometro = Cronometer.Cronometer(120)
        self.run()

        #Otras variables
        self.selected = 0
        self.total = 0

    def run(self):


        pygame.mixer.music.load('Music/backgroundSounds/background_musicPrincipal.mp3')
        pygame.time.set_timer(pygame.USEREVENT, 160)
        while not self.out:


            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()

            # AQUI TODA LA LÓGICA DEL JUEGO
            self.figureMario.everDown()
            self.validateCollisions()
            self.marioJump()
            self.screenPaint()

            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            #self.reloj.tick(60)

    def listenEvent(self):
        self.key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.update()

            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYUP:
                if not self.pressed:
                    self.figureMario.stopped()

        if self.key[pygame.K_RIGHT]:
            self.figureMario.run(pygame.K_RIGHT)
            if not self.pressed:
                self.figureMario.update()

        if self.key[pygame.K_LEFT]:
            self.figureMario.run(pygame.K_LEFT)
            if not self.pressed:
                self.figureMario.update()

        if self.key[pygame.K_UP]:
            if not self.pressed and pygame.sprite.collide_mask(self.figureMario, self.floor):
                self.figureMario.jump()
                self.figureMario.updateJump()
                self.pressed = True

        if self.key[pygame.K_SPACE]:
            self.loads.pause.play()
            self.pause()
            self.outPause = False

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
                        self.cronometro.continue_clock()
                    if self.selected == 3:
                        self.outPause = True
                        self.out = True

    def validateCollisions(self):
        if pygame.sprite.collide_mask(self.figureMario, self.floor):
            if self.pressed:
                self.figureMario.moveUp(4)
            else:
                self.figureMario.moveUp()
            self.pressed = False

    def marioJump(self):
        if self.pressed:
            self.figureMario.updateJump()

    '''
        Este método de clase, tiene como función pausar el juego  para esperar otros eventos
    '''
    def pause(self):
        self.cronometro.pause_clock()
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

    def screenPaint(self):
        # Pintado de pantalla
        self.screen.fill((0,0,0))
        imageBackGround = pygame.transform.scale(self.background,(1280, 720))
        self.screen.blit(imageBackGround,(0,0))
        self.screen.blit(self.cronometro.start_clock(),(1190,10))
        self.screen.blit(self.figureMario.image, self.figureMario.rect)
        self.screen.blit(self.hammer.image, self.hammer.position)
        for i in range(8):
            self.screen.blit(self.brick.image, (self.brick.rect.left + i*50, self.brick.rect.top))
        self.screen.blit(self.floor.image, self.floor.rect)


    def update(self):
        self.hammer.update()
        self.brick.update()