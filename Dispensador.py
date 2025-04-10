import threading
from time import sleep
from random import randint
from enum import Enum

class EstadoDispensador(Enum):
    CERRADO = 1
    ABIERTO = 2
    ALERTA = 3

class Dispensador:
    
    def __init__(self, platos): # Inicializa el dispensador con los platos que administra a traves de una lista llamada platos
        self.platos= platos
        self.estado = Dispensador.CERRADO
        self.gato_invasor = False
    
    def dispensar(self, cantidad):
        # Simula el tiempo de dispensado
        sleep(1)
        print(f"Dispensando {cantidad} gramos de comida.")
        return cantidad
    
    def detectarGatoInvasor(self):
      with self.Lock:
        self.gato_invasor = True
        self.estado = EstadoDispensador.ALERTA
    
    def retiradaGatoInvasor(self):
      with self.Lock:
        self.gato_invasor = False
        self.estado = EstadoDispensador.ABIERTO
        self.dispensar()
        self.estado = EstadoDispensador.CERRADO