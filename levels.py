# -*- encoding: utf-8 -*-
# !/usr/bin/env python

import pygame
import sys

class level1(pygame.sprite.Sprite):

    def __init__(self, screen, resolution, background, efectSound, floor, brick, mario, enemy):
        self.screen = screen
        self.background = background
        self.efectSound = efectSound
        self.resolution = resolution
        self.floor = floor
        self.brick = brick
        self.figureMario = mario
        self.hammer = enemy
        #Realiza la activación y desactivación de los movimientos de mario
        self.motionActivated = False
        self.combinationKeyActivated = False
        self.key = pygame.KEYUP
        self.combinationKey = pygame.KEYUP
        self.out = False

        # Se usa para gestionar cuan rápido se actualiza la pantalla
        self.reloj = pygame.time.Clock()
        self.run()

    def run(self):
        pygame.mixer.music.load('Music/backgroundSounds/background_musicPrincipal.mp3')
        while not self.out:
            # Esta funcion tiene el fin de manejar el comportamiento de los eventos
            self.listenEvent()

            # AQUI TODA LA LÓGICA DEL JUEGO
            self.mariosMoves()
            self.screenPaint()

            # Limita a 20 fotogramas por segundo el pintado de la pantalla
            pygame.display.flip()
            self.reloj.tick(15)

    def listenEvent(self):
        #Se esperan todos los eventos producidos por el teclado y ratón del computador
        for event in pygame.event.get():
            #Si esta decision llega a retornar verdadero, se cerrará automáticamente la pantalla del juego
            if event.type == pygame.QUIT:
                sys.exit(0)
            #Si esta decision llega a retornar verdadero, se guardara la tecla persionada y se activara motionActivated
            if event.type == pygame.KEYDOWN:
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
            self.figureMario.update(self.key, self.efectSound)
        else:
            if self.key == pygame.KEYUP:
                self.figureMario.update(self.key, '')

    def screenPaint(self):
        # Pintado de pantalla
        self.screen.fill((255,255,255))
        imageBackGround = pygame.transform.scale(self.background,(self.resolution))
        self.screen.blit(imageBackGround,(0,0))
        self.screen.blit(self.figureMario.image, self.figureMario.rect)
        self.screen.blit(self.hammer.image, self.hammer.position)
        for i in range(8):
            self.screen.blit(self.brick.image, (self.brick.rect.left + i*40, self.brick.rect.top))
        imageFloor = pygame.transform.scale(self.floor, (1280, 60))
        self.screen.blit(imageFloor, (0, 660))
        self.update()

    def update(self):
        self.hammer.update()
        self.brick.update()