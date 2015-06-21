# -*- encoding: utf-8 -*-
# !/usr/bin/env python

import pygame


class mario(pygame.sprite.Sprite):
    def __init__(self, imagesMario, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.resolution = (150, 170)
        self.images = imagesMario
        self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber],self.resolution)
        self.rect = self.images[self.imageNumber].get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = posx
        self.rect.top = posy

    def update(self, key):
        if self.imageNumber >= 0 and self.imageNumber <= 2:
            self.imageNumber += 1
        if self.imageNumber == 3:
            self.imageNumber = 1

        if (key == pygame.K_LEFT):
            self.rect.move_ip(-40, 0)
        if (key == pygame.K_RIGHT):
            self.rect.move_ip(40, 0)
        if (key == pygame.KEYUP):
            self.imageNumber = 0
        self.image = pygame.transform.scale(self.images[self.imageNumber],self.resolution)