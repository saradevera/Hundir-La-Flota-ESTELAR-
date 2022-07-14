import numpy as np
# import pandas as pd
import functions as f
from time import sleep
# from clase import *
import pygame

pygame.init()
pygame.mixer.init()

sonido_fondo = pygame.mixer.Sound("imperial_march.wav")
pygame.mixer.Sound.play(sonido_fondo)

print('Bienvenido a "HUNDIR LA FLOTA ESTELAR"')
sleep(0.5)

nombre_jugador = input('¿Cuál es tu nombre?')
sleep(0.5)

print('Hola', nombre_jugador,'!, Bienvenida :)')
sleep(0.5)

print("Las naves vienen representadas por un '\U0001F680'")
sleep(0.5)

print("El símbolo '\U0001F537' hace referencia a un disparo fallido")
sleep(0.5)

print("El símbolo '\U00002B55' hace referencia a un barco tocado")
sleep(0.5)

print('A continuación colocarás los barcos según coordenadas y orientación...')
sleep(0.5)

print("CARGANDO...")
sleep(1.5)

input("Presiona ENTER para continuar")
sleep(0.5)

import variables as v

f.colocar_barcos_jugador(v.tablero_jugador, v.lista_de_barcos_jug)

f.colocar_barcos_maquina(v.tablero_maquina, v.lista_de_barcos_maq)

print('A continuación empezarás a disparar a las naves de la máquina')
sleep(1.5)
print(v.tablero_maquina)


while np.sum(v.tablero_maquina == '\U00002B55') <= 4:

    if np.sum(v.tablero_jugador == '\U00002B55') == 4:
        sonido_perder = pygame.mixer.Sound("hoho.wav")
        pygame.mixer.Sound.play(sonido_perder)
        print('Lo siento, has perdido todas tus naves')
        break
    
    f.disparo_por_coordenadas_DOBLE_TAB(v.tablero_maquina, v.tablero_maquina_SHOW)
    print('Has acertado ', np.sum(v.tablero_maquina == '\U00002B55'), 'disparos')
    sleep(0.5)

    if np.sum(v.tablero_maquina == '\U00002B55') == 4:
        sonido_ganar = pygame.mixer.Sound("r2.wav")
        pygame.mixer.Sound.play(sonido_ganar)
        # print('Has ganado el juego, ¡Enhorabuena!')
        # print(v.tablero_maquina)
        break

    f.disparo_aleatorio_con_bucle(v.tablero_jugador)
    print('La máquina ha acertado', np.sum(v.tablero_jugador == '\U00002B55'), 'disparos')
    sleep(0.5)