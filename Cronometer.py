__author__ = 'Josue'

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
        self.fuente  = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",30)
        self.texto = 0      # Inicializacion de la superficie

    def get_remaining_time(self):
        return self.remaining_t

    def start_clock(self):
        """
        Metodo utilizado para reducir segundo a segundo con cada llamada el tiempo restantante.
        Genera un objeto de tipo superfice en la que se imprime la cuenta, los parametros del
        texto de la superficie se definen en el init de la clase.
        :return: surface.
        """
        self.seconds += self.reloj.tick(60)

        if self.seconds/1000== 1 and not(self.lock_time) and self.get_remaining_time()> 0:
            self.remaining_t -= 1
            self.seconds = 0
        self.texto = self.fuente.render(str(self.get_remaining_time()),1,(255,255,255))
        return self.texto

    def pause_clock(self):
        """
        Metodo utilizado para pausar la cuenta regresiva. Se utiliza una variable de bloqueo llamada lock_time
        para evitar que se continue restando los segundos de remaining_t.
        lock_time cambia su valor a True indicando que la cuenta regresiva se detiene temporalmente
        :return:None
        """
        self.temp = self.seconds
        self.lock_time = True
        return None

    def continue_clock(self):
        """
        Deshabilita el bloqueo que con anterioridad se coloco a traves de una llamada a pause_clock.
        Asigna a lock_time el valor False, permitiendo a la cuenta regresiva continuar.
        Se realiza una llamada a tick para reiniciar en los milisegundos que se acumularon antes del pause.
        Tambien almacena los milisegundos transcurridos antes de la llamada a pause_clock

        :return: None
        """
        self.lock_time = False
        self.seconds = self.reloj.tick(60)
        self.seconds = self.temp

        return None
