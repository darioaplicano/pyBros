__author__ = 'loot'

import pygame
import sys
from pygame.locals import *

class Cronometer :
    """ Crea un objeto que gestiona una cuenta regresiva, que posteriormente
        se visualizara en una superficie.
    """

    def __init__(self,time):
        self.remaining_t = time     # Inicializa la cuenta regresiva
        self.temp = 0       # Almacena el valor del tiempo restante cuando ocurre una pausa
        self.reloj = pygame.time.Clock()
        self.seconds = 0    # Almacena los milisegundos
        self.lock_time = False  # Almacena el estado de la pausa, True: pausa activada
        pygame.font.init()
        self.fuente  = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",20)
        self.texto = 0      # Inicializacion de la superficie

    def get_remaining_time(self):
        return self.remaining_t

    def set_remaining_time(self,time):
        self.remaining_t = time
        return None

    def get_temp(self):
        return self.temp

    def set_temp(self,time):
        self.temp = time
        return None

    def start_clock(self):
        """
        Metodo utilizado para reducir segundo a segundo con cada llamada el tiempo restantante.
        Genera un objeto de tipo superfice en la que se imprime la cuenta, los parametros del
        texto de la superficie se definen en el init de la clase.
        :return: surface.
        """
        self.seconds += self.reloj.tick(60)
        if self.seconds/1000 == 1 and not(self.lock_time) and self.get_remaining_time()> 0:
            self.remaining_t -= 1
            self.seconds = 0

        self.texto = self.fuente.render(str(self.get_remaining_time()),1,(255,255,255))

        return self.texto

    def pause_clock(self):
        """
        Metodo utilizado para pausar la cuenta regresiva. Se utiliza una variable de bloqueo llamada lock_time
        para evitar que se continue restando los segundos de remaining_t.
        lock_time cambia su valor a True indicando que la cuenta regresiva se para temporalmente
        :return:None
        """
        self.set_temp(self.get_remaining_time())

        self.lock_time = True
        return None

    def continue_clock(self):
        """
        Deshabilita el bloqueo que con anterioridad se colo con una llamada a pause_clock.
        Asigna a lock_time el valor False, permitiendo a la cuenta regresiva continuar.

        :return: None
        """
        self.lock_time = False
        self.set_remaining_time(self.temp)
        self.start_clock()
        return None
