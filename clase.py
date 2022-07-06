import numpy as np
import pandas as pd



class Tablero:
    
    def __init__(self, alto=10, ancho=10, barcos=[]):
        self.alto = alto
        self.ancho = ancho
        self.tablero = np.full((ancho, alto), fill_value="\U000026AA")

    def inicia_tablero(self):
        return np.array(self.tablero)

    def imprime_tablero(self):
        print(self.tablero)
