__author__ = 'adfa'

import pygame

class splashScreen(pygame.sprite.Sprite):

    def __init__(self, workSpace, pyBros_Logo, posX, posY):
        self.workSpace = workSpace
        self.pyBrosLogo_width = 600
        self.pyBrosLogo_height = 300
        resolution = (self.pyBrosLogo_width, self.pyBrosLogo_height)
        self.pyBros_Logo = pygame.transform.scale(pyBros_Logo, resolution)
        self.position = (posX - self.pyBrosLogo_width/2, posY - self.pyBrosLogo_height/2)
        self.bar = pygame.Surface(((self.pyBrosLogo_width - 100) / 10, 40))
        self.actived()

    def actived(self):
        self.workSpace.blit(self.pyBros_Logo, self.position)
        pygame.display.flip()
        self.animationBar()

    def animationBar(self):
        self.bar.fill((255,255,255))
        for i in range(11):
            self.workSpace.blit(self.bar, (self.position[0] + i*((self.pyBrosLogo_width - 100) / 10 + 10), self.position[1] + self.pyBrosLogo_height))
            pygame.display.flip()
            pygame.time.wait(300)
        pygame.time.wait(500)
