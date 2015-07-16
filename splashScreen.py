# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#Se importan los archivos necesarios para la correcta ejecución del juego
import pygame

class splashScreen(pygame.sprite.Sprite):

    def __init__(self, workSpace, backgroundSplash, floorSplash, posX, posY):
        self.workSpace = workSpace
        self.backgroundSplash_width = 600
        self.backgroundSplash_height = 300
        resolution = (self.backgroundSplash_width, self.backgroundSplash_height)
        self.backgroundSplash = backgroundSplash
        self.floorSplash = floorSplash
        self.position = (posX - self.backgroundSplash_width/2, posY - self.backgroundSplash_height/2)
        self.bar = pygame.Surface(((self.backgroundSplash_width - 100) / 11, 40))
        self.actived()

    def actived(self):
        self.workSpace.blit(self.backgroundSplash, (0,0))
        self.workSpace.blit(self.floorSplash, (0, 629))
        pygame.display.flip()
        self.animationBar()

    def animationBar(self):
        self.bar.fill((255,255,255))
        for i in range(11):
            self.workSpace.blit(self.bar, (self.position[0] + i*((self.backgroundSplash_width - 100) / 11 + 10),
                                           self.position[1] + self.backgroundSplash_height))
            pygame.display.flip()
            pygame.time.wait(300)
        pygame.time.wait(500)
