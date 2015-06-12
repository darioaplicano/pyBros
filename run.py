#!/usr/bin/env python
__author__ = 'adfa'

#Se importan los archivos necesarios para la correcta ejecucion del juego
import pygame
import loads

class main:

    def __init__(self):
        pygame.init()

        #Instanciamos variables a los archivos externos necesarios
        self.loads = loads.loads()

        #Creamos el area principal del trabajo
        self.sizePA_X = 800
        self.sizePA_Y = 453
        self.principalArea = pygame.Surface((self.sizePA_X,self.sizePA_Y))

        #Creamos el area de trabajo
        self.sizeWS_X = 1080
        self.sizeWS_Y = 720
        self.workSpace = pygame.display.set_mode((self.sizeWS_X, self.sizeWS_Y))
        pygame.display.set_caption('pyBros')

    def run(self):
        t = 0
        while t < 3:
            self.principalArea.blit(self.loads.backGround_Image,(0,0))
            self.workSpace.blit(self.principalArea,(0,0))
            pygame.time.wait(3000)
            t = t + 1


#Se crea una instancia al juego para comenzar el mismo
iniciar = main()
iniciar.run()