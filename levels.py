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
        self.brick1 = figures.brick(self.loads.brick, 850, 470)
        brick2 = figures.brick(self.loads.brick, 900, 470)
        brick3 = figures.brick(self.loads.brick, 950, 470)
        brick4 = figures.brick(self.loads.brick, 1000, 470)
        brick5 = figures.brick(self.loads.brick, 1050, 470)
        brick6 = figures.brick(self.loads.brick, 1100, 470)
        #lista que contiene bricks
        self.listBricks = [self.brick1, brick2, brick3, brick4, brick5, brick6]
        self.figureMario = figures.mario(self.loads.imagesMario, 160, 561, self.floor.rect.top)
        self.hammer = figures.enemy(self.loads.imagesHammer, self.loads.smallHammer, 1050, 402, self.listBricks)
        self.fuente = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",100)
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
        pygame.time.set_timer(pygame.USEREVENT, 250)
        pygame.time.set_timer(pygame.USEREVENT + 1,250)
        pygame.time.set_timer(pygame.USEREVENT + 2,300)
        while not self.out:

            self.screenPaint()
            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()

            # AQUI TODA LA LÓGICA DEL JUEGO
            self.validateCollisions()
            self.figureMario.everDown()

            self.marioJump()
            self.updateCollide()    

            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            #self.reloj.tick(60)

    def listenEvent(self):
        self.key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.brick1.update()

            if event.type == pygame.USEREVENT +1:
                if (self.hammer.flag and self.hammer.throw):
                    self.hammer.saveSmallHammer(self.hammer.position[0], self.hammer.position[1])
                self.updateHammer()
                

            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYUP:
                if not self.pressed:
                    self.figureMario.stopped()

        if self.key[pygame.K_RIGHT]:
            if self.figureMario.rect.left + 20<=1220:
                self.figureMario.run(pygame.K_RIGHT)

            else :
                self.figureMario.stopped()
            if not self.pressed:
                self.figureMario.update()

        if self.key[pygame.K_LEFT]:
            if self.figureMario.rect.left >= -10:

                self.figureMario.run(pygame.K_LEFT)
            else:
                self.figureMario.stopped()
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
        for brick in self.listBricks:
            self.screen.blit(brick.image, brick.rect)
        self.screen.blit(self.floor.image, self.floor.rect)
        if self.cronometro.get_remaining_time() == 0:
            self.gameOver()
        self.hammer.update()


    def updateHammer(self):
        if len(self.hammer.listSmallHammers) > 0:
            for hammercito in self.hammer.listSmallHammers:
                hammercito.drawHammer(self.screen)
                if pygame.sprite.collide_mask(self.figureMario,hammercito):
                    self.gameOver()
                if pygame.sprite.collide_mask(self.floor, hammercito):
                    ubication = self.hammer.listSmallHammers.index(hammercito)
                    del self.hammer.listSmallHammers[ubication]

    #Verifica si hay colision mario con los bricks y los elimina, tambien verifica si arriba esta hammer 
    def updateCollide(self):
        n = self.figureMario.collideBricks(self.figureMario, self.listBricks)
        if n > -1 :
            if pygame.sprite.collide_mask(self.listBricks[n], self.hammer):
                print "Hammer die"
            del self.listBricks[n]

    def gameOver(self):
        fuente  = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",60)
        texto = fuente.render("game over",1, (255,255,255))
        clock = Cronometer.Cronometer(2)
        exit = True
        while exit:
            clock.start_clock()
            if clock.get_remaining_time()==0:
               exit = False
            self.screen.blit(texto,(436,304))
            pygame.display.flip()
        self.out = True

