# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame
import json

class loads:

    def __init__(self):
        pygame.init()

        #En esta seccion se cargan las imagenes a utilizar en el juego
        self.tablero = pygame.image.load("Images/tablero.png")
        resting_Mario = pygame.image.load('Images/mario_move1.png')
        walkRight_Mario = pygame.image.load('Images/mario_move2.png')
        walkLeft_Mario = pygame.image.load('Images/mario_move3.png')
        walkRight2_Mario = pygame.image.load('Images/mario_move4.png')
        jump_Mario = pygame.image.load('Images/mario_move5.png')
        image_Mario6 = pygame.image.load("Images/mario_move6.png")
        image_Mario7 = pygame.image.load("Images/mario_move7.png")
        self.imagesMario = [resting_Mario, walkRight_Mario, walkLeft_Mario, walkRight2_Mario, jump_Mario,image_Mario6,image_Mario7]
        self.pyBros_Logo = pygame.image.load('Images/pyBros_Logo.png')
        self.backgroundSplas = pygame.image.load('Images/backgroundsplash.png')
        self.floorSplas = pygame.image.load('Images/floorsplash.png')
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
        level1 = pygame.image.load('Images/level1.png')
        level2 = pygame.image.load('Images/level2.png')
        self.imagesLevel = [level1, level2]
        self.castle = pygame.image.load('Images/castle.png')
        self.bowser_castle = pygame.image.load('Images/bowser_castle.png')

        #Imagenes pertenecientes a Mario sin transformacion
        small_Mario1 = pygame.image.load("Images/small_mario1.png")
        small_Mario2 = pygame.image.load("Images/small_mario2.png")
        small_Mario3 = pygame.image.load("Images/small_mario3.png")
        small_Mario4 = pygame.image.load("Images/small_mario4.png")
        self.small_Mario = [small_Mario1,small_Mario2,small_Mario3,small_Mario4]

        #Las imagenes de la historia
        historia_1 = pygame.image.load('Images/historia_1.png')
        historia_2 = pygame.image.load('Images/historia_2.png')
        historia_3 = pygame.image.load('Images/historia_3.png')
        self.historia = [historia_1,historia_2,historia_3]

        #En esta sección se cargan los sonidos a utilizar en el juego
        self.jumping_SoundMario = pygame.mixer.Sound('Music/effectSounds/smb3_jump.wav')
        self.pause = pygame.mixer.Sound('Music/effectSounds/smb3_pause.wav')
        self.travel_Principal = pygame.mixer.Sound('Music/effectSounds/smb3_map_travel.wav')


        #En esta sección se cargan las fuentes necesarias
        self.font_Mario = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf", 25)
        self.font_Mario2 = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf", 20)

        #En esta seccion se cargan los archivos json necesarios para la correcta comunicacion del juego
        self.moves_MainMario()

    def moves_MainMario(self):
        self.moves_MainMario = json.loads(open("Comunication/moves_MainMario.json").read())