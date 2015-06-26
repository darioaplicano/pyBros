# -*- encoding: utf-8 -*-
#!/usr/bin/env python

import pygame

class loads:

    def __init__(self):
        pygame.init()

        #En esta seccion se cargan las imagenes a utilizar en el juego
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
        bush1 = pygame.image.load('Images/bush1.png')
        bush2 = pygame.image.load('Images/bush2.png')
        bush3 = pygame.image.load('Images/bush3.png')
        self.imagesBush = [bush1, bush2, bush3]
        bones1 = pygame.image.load('Images/bones1.png')
        bones2 = pygame.image.load('Images/bones2.png')
        bones3 = pygame.image.load('Images/bones3.png')
        self.imagesBones = [bones1, bones2, bones3]
        point1 = pygame.image.load('Images/point1.png')
        point2 = pygame.image.load('Images/point2.png')
        point3 = pygame.image.load('Images/point3.png')
        self.imagesPoint = [point1, point2, point3]
        flower1 = pygame.image.load('Images/flower1.png')
        flower2 = pygame.image.load('Images/flower2.png')
        self.imagesFlower = [flower1, flower2]

        #En esta seccion se cargan los sonidos a utilizar en el juego
        self.jumping_SoundMario = pygame.mixer.Sound('Music/effectSounds/smb3_jump.wav')
        self.pause = pygame.mixer.Sound('Music/effectSounds/smb3_pause.wav')
        self.travel_Principal = pygame.mixer.Sound('Music/effectSounds/smb3_map_travel.wav')


        #En esta sección se cargan las fuentes necesarias
        self.font_Mario = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf", 25)