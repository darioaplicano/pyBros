# -*- encoding: utf-8 -*-
#!/usr/bin/env python

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
        main_MarioMove1 = pygame.image.load('Images/main_mario_move1.png')
        main_MarioMove2 = pygame.image.load('Images/main_mario_move2.png')
        self.main_Mario = [main_MarioMove1, main_MarioMove2]
        hammer1 = pygame.image.load('Images/hammer1.png')
        hammer2 = pygame.image.load('Images/hammer2.png')
        hammer3 = pygame.image.load('Images/hammer3.png')
        self.imagesHammer = [hammer1, hammer2, hammer3]
        self.smallHammer = pygame.image.load('Images/smallHammer.png')
        self.background_stage1 = pygame.image.load('Images/background_stage1.png')
        brick1 = pygame.image.load('Images/brick1.png')
        brick2 = pygame.image.load('Images/brick2.png')
        brick3 = pygame.image.load('Images/brick3.png')
        brick4 = pygame.image.load('Images/brick4.png')
        self.brick = [brick1, brick2, brick3, brick4]
        self.floor_stage1 = pygame.image.load('Images/floor_stage1.png')

        #En esta seccion se cargan los sonidos a utilizar en el juego
        self.jumping_SoundMario = pygame.mixer.Sound('Music/effectSounds/smb3_jump.wav')
        self.pause = pygame.mixer.Sound('Music/effectSounds/smb3_pause.wav')
        self.travel_Principal = pygame.mixer.Sound('Music/effectSounds/smb3_map_travel.wav')


        #En esta sección se cargan las fuentes necesarias
        self.font_Mario = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf", 25)