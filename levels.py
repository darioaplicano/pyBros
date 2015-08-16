# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame
import sys
import figures
#import Cronometer
import CountdownClock
class level1(pygame.sprite.Sprite):

    def __init__(self, screen, resolution, loads):
        self.loads =  loads
        self.screen = screen
        self.background = self.loads.background_stage1
        self.efectSound = self.loads.jumping_SoundMario
        self.resolution = resolution
        self.width = self.resolution[0]
        self.height = self.resolution[1]
        self.panel = figures.panel(self.loads.tablero,0,640)
        self.floor = figures.floor(self.loads.floor_stage1, 0, 570)
        brick0 = figures.brick(self.loads.brick, 800, 390)
        brick1 = figures.brick(self.loads.brick, 850, 390)
        brick2 = figures.brick(self.loads.brick, 900, 390)
        brick3 = figures.brick(self.loads.brick, 950, 390)
        brick4 = figures.brick(self.loads.brick, 1000, 390)
        brick5 = figures.brick(self.loads.brick, 1050, 390)
        brick6 = figures.brick(self.loads.brick, 1100, 390)
        #lista que contiene bricks
        self.listBricks = [brick0,brick1, brick2, brick3, brick4, brick5, brick6]
        self.figureMario = figures.mario(self.loads.imagesMario, 160, 480, self.floor.rect.top)
        self.hammer = figures.enemy(self.loads.imagesHammer, self.loads.smallHammer, 1050, 310, self.listBricks)
        self.fuente = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",100)
        #Realiza la activación y desactivación de los movimientos de mario
        self.key = pygame.KEYUP
        self.out = False
        self.outPause = False
        self.pressed = False
        self.temp_presx = pygame.KEYUP
        self.down = False
        self.floor_c = True
        self.jumping = False
        self.vector = (False,False)


        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()
        self.count_down = CountdownClock.CountdownClock(120)
        self.run()

        #Otras variables
        self.selected = 0
        self.total = 0
        self.cont = 0

    def run(self):


        pygame.mixer.music.load('Music/backgroundSounds/background_musicPrincipal.mp3')
        pygame.time.set_timer(pygame.USEREVENT, 50)
        pygame.time.set_timer(pygame.USEREVENT + 1,1000)
        pygame.time.set_timer(pygame.USEREVENT + 2,200)
        pygame.time.set_timer(pygame.USEREVENT + 3,150)

        while not self.out:


            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()

            # AQUI TODA LA LÓGICA DEL JUEGO
            self.validateCollisions()
            self.figureMario.everDown(self.down)
            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            self.reloj.tick(60)

    def listenEvent(self):

        self.key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.screenPaint()
                self.updateHammer()

            if event.type == pygame.USEREVENT + 2 :
                self.screenPaint()
                for brick in self.listBricks :
                  brick.update()
                self.figureMario.update()

            if event.type == pygame.USEREVENT + 1:
                self.count_down.start_clock(event)


            if event.type == pygame.USEREVENT +3:
                if (self.hammer.flag and self.hammer.throw):
                    self.hammer.saveSmallHammer(self.hammer.position[0], self.hammer.position[1])

                self.hammer.update()

            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYUP:
                if self.key[pygame.K_z]:
                    self.jumping = False
                    self.down = True
                    self.figureMario.press_time = 0



        if self.key[pygame.K_RIGHT]:
            if self.figureMario.rect.left + 20<=1220:
                self.figureMario.run(pygame.K_RIGHT)
                self.pressed = True

            else :
                self.figureMario.stopped()
            if not self.pressed:
                self.figureMario.update()

        if self.key[pygame.K_LEFT]:
            if self.figureMario.rect.left >= -10:
                self.figureMario.run(pygame.K_LEFT)



        if self.key[pygame.K_z]:
            if self.floor_c or not self.down:
                self.figureMario.jump(self.pressed)
            self.floor_c = False
            if self.figureMario.press_time == 10:
                self.down = True
            if self.figureMario.press_time == 0:
                self.jumping = False
            else:
                self.jumping = True



        if self.key[pygame.K_DOWN]:
            self.figureMario.crouch(self.jumping,self.down)

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
                        self.count_down.continue_clock()
                    if self.selected == 3:
                        self.outPause = True
                        self.out = True

    def validateCollisions(self):

        if pygame.sprite.collide_mask(self.figureMario, self.floor):
            self.down = False
            self.jumping = False









    def marioJump(self):
        if self.pressed:
            self.figureMario.updateJump()

    '''
        Este método de clase, tiene como función pausar el juego  para esperar otros eventos
    '''
    def pause(self):
        self.count_down.pause_clock()
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
        self.screen.blit(self.panel.image,self.panel.rect)
        self.screen.blit(self.count_down.return_time(),(1190,10))

        self.screen.blit(self.figureMario.image, self.figureMario.rect)
        self.screen.blit(self.hammer.image, self.hammer.position)
        for brick in self.listBricks:
            self.screen.blit(brick.image, brick.rect)
        self.screen.blit(self.floor.image, self.floor.rect)
        if self.count_down.get_remaining_time() == 0:
            self.gameOver()



    def updateHammer(self):
        if len(self.hammer.listSmallHammers) > 0:
            for hammercito in self.hammer.listSmallHammers:
                hammercito.drawHammer(self.screen)
                if pygame.sprite.collide_mask(self.figureMario,hammercito):
                    self.gameOver()
        pygame.display.flip()


    def gameOver(self):
        fuente  = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",60)
        texto = fuente.render("game over",1, (255,255,255))
        clock = CountdownClock.CountdownClock(2)
        exit = True
        while exit:
            for event in pygame.event.get():

                clock.start_clock(event)
                if clock.get_remaining_time()==0:
                   exit = False
                self.screen.blit(texto,(436,304))
                pygame.display.flip()
        self.out = True

