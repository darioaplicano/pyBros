# -*- encoding: utf-8 -*-
# !/usr/bin/env python

import pygame


class mario(pygame.sprite.Sprite):
    def __init__(self, imagesMario, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (75, 87)
        self.images = imagesMario
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber],self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.invert = False

    '''
        Este metodo tiene como fin modelar los comportamientos de mario, en su desplazamiento

        variables:
            key: Contiene el valor de la tecla o el tipo de evento generado en el juego principal que interviene en los
            movimientos de mario.
    '''

    def update(self, key, sound):
        '''
        Mediante estas decisiones se hace el cambio de imagenes respectivo para el desplazamiento de mario

        variables:
        '''
        if self.imageNumber >= 0 and self.imageNumber <= 2:
            self.imageNumber += 1
        if self.imageNumber == 3:
            self.imageNumber = 1

        if (key == pygame.K_LEFT):
            self.rect.move_ip(-20, 0)
            self.invert = True
        if (key == pygame.K_RIGHT):
            self.rect.move_ip(20, 0)
            self.invert = False
        if (key == pygame.K_UP):
            sound.play()
            self.rect.move_ip(0, -5)

        if (key == pygame.KEYUP):
            self.imageNumber = 0

        self.image = pygame.transform.scale(self.images[self.imageNumber],self.resolution)
        if self.invert:
            self.image = pygame.transform.flip(self.image, self.invert, False)