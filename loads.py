#!/usr/bin/env python
__author__ = 'adfa'


import pygame

class loads:

    def __init__(self):
        pygame.init()

        #En esta seccion se cargan las imagenes a utilizar en el juego
        self.backGround_Image = pygame.image.load('Images/backGround_Image.png')