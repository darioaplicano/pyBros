__author__ = 'Josue'

import pygame
from pygame.locals import *

class CountdownClock :
    """ Crea un objeto que gestiona una cuenta regresiva, que posteriormente
        se visualizara en una superficie.
    """

    def __init__(self,time):
        self.remaining_t = time     # Inicializa la cuenta regresiva
        #pygame.time.set_timer(pygame.USEREVENT + 1 ,1000)
        self.lock_time = False  # Almacena el estado de la pausa, True: pausa activada
        pygame.font.init()
        self.fuente  = pygame.font.Font("Fonts/Super-Mario-Bros--3.ttf",30)
        self.texto = 0      # Inicializacion de la superficie

    def get_remaining_time(self):
        return self.remaining_t

    def start_clock(self,event):
        """
        Metodo utilizado para reducir segundo a segundo con cada llamada el tiempo restantante.
        Genera un objeto de tipo superfice en la que se imprime la cuenta, los parametros del
        texto de la superficie se definen en el init de la clase.
        :return: surface.
        """
        if self.lock_time == False :

            if event.type == pygame.USEREVENT + 1:
                self.remaining_t -=1

        return None
    def return_time(self):
        return  self.fuente.render(str(self.get_remaining_time()),1,(255,255,255))

    def pause_clock(self):
        """
        Metodo utilizado para pausar la cuenta regresiva. Se utiliza una variable de bloqueo llamada lock_time
        para evitar que se continue con la cuenta regresiva..
        lock_time cambia su valor a True indicando que la cuenta regresiva se detiene temporalmente
        :return:None
        """
        self.lock_time = True
        return None

    def continue_clock(self):
        """
        Deshabilita el bloqueo que con anterioridad se coloco a traves de una llamada a pause_clock.
        Asigna a lock_time el valor False, permitiendo a la cuenta regresiva continuar.


        :return: None
        """
        self.lock_time = False

        return None
