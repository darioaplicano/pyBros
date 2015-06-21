#!/usr/bin/env python
__author__ = 'adfa'


import pygame

class loads:

    def __init__(self):
        pygame.init()

        #En esta seccion se cargan las imagenes a utilizar en el juego
        self.backGround_Image = pygame.image.load('Images/backGround_Image.png')
        jumping_Mario = pygame.image.load('Images/jumping_Mario.png')
        resting_Mario = pygame.image.load('Images/resting_Mario.png')
        walkRight_Mario = pygame.image.load('Images/walkRight_Mario.png')
        walkLeft_Mario = pygame.image.load('Images/jumping_Mario.png')
        self.imagesMario = [resting_Mario, walkRight_Mario, walkLeft_Mario, jumping_Mario]
        self.pyBros_Logo = pygame.image.load('Images/pyBros_Logo.png')

        #En esta seccion se cargan los sonidos a utilizar en el juego