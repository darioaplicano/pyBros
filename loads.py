# -*- encoding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'adfa'


import pygame

class loads:

    def __init__(self):
        pygame.init()

        #En esta seccion se cargan las imagenes a utilizar en el juego
        self.backGround_Image = pygame.image.load('Images/backGround_Image.png')
        jumping_Mario = pygame.image.load('Images/jumping_Mario.png')
        resting_Mario = pygame.image.load('Images/mario_move1.png')
        walkRight_Mario = pygame.image.load('Images/mario_move2.png')
        walkLeft_Mario = pygame.image.load('Images/mario_move3.png')
        walkRight2_Mario = pygame.image.load('Images/mario_move4.png')
        self.imagesMario = [resting_Mario, walkRight_Mario, walkLeft_Mario, walkRight2_Mario]
        self.pyBros_Logo = pygame.image.load('Images/pyBros_Logo.png')
        self.main_Screen = pygame.image.load('Images/main_Screen.png')
        self.fungus =  pygame.image.load('Images/fungus.png')

        #En esta seccion se cargan los sonidos a utilizar en el juego
        self.jumping_SoundMario = pygame.mixer.Sound('Music/effectSounds/smb3_jump.wav')

        #En esta sección se cargan las fuentes necesarias
        self.font_Mario = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf", 25)