import numpy as np
import functions as f
from time import sleep

        
# TABLEROS
tablero_jugador = np.full((10,10), fill_value="\U000026AA")
tablero_maquina = np.full((10,10), fill_value="\U000026AA")
tablero_maquina_SHOW = np.full((10,10), fill_value="\U000026AA")


# VERSIÓN JUEGO COMPLETO

# BARCOS JUGADOR
ala_x = f.barco_por_coordenadas_jugador(1)
ala_x_2 = f.barco_por_coordenadas_jugador(1)
ala_x_3 = f.barco_por_coordenadas_jugador(1)
ala_x_4 = f.barco_por_coordenadas_jugador(1)
lanzadera_tidirium = f.barco_por_coordenadas_jugador(2)
lanzadera_imperial = f.barco_por_coordenadas_jugador(2)
destructor_estelar = f.barco_por_coordenadas_jugador(3)
nave_nodriza = f.barco_por_coordenadas_jugador(3)
estrella_de_la_muerte = f.barco_por_coordenadas_jugador(4)
halcon_milenario = f.barco_por_coordenadas_jugador(4)

# BARCOS MÁQUINA
maquina_1a = f.barco_aleatorio_maquina(1)
maquina_1b = f.barco_aleatorio_maquina(1)
maquina_1c = f.barco_aleatorio_maquina(1)
maquina_1d = f.barco_aleatorio_maquina(1)
maquina_2a = f.barco_aleatorio_maquina(2)
maquina_2b = f.barco_aleatorio_maquina(2)
maquina_3a = f.barco_aleatorio_maquina(3)
maquina_3b = f.barco_aleatorio_maquina(3)
maquina_4a = f.barco_aleatorio_maquina(4)
maquina_4b = f.barco_aleatorio_maquina(4)

# LISTA DE BARCOS
lista_de_barcos_jug = [ala_x, ala_x_2, ala_x_3, ala_x_4, lanzadera_tidirium, lanzadera_imperial, destructor_estelar, nave_nodriza, estrella_de_la_muerte, halcon_milenario]
lista_de_barcos_maq = [maquina_1a, maquina_1b, maquina_1c, maquina_1d, maquina_2a, maquina_2b, maquina_3a, maquina_3b, maquina_4a, maquina_4b]



# VERSIÓN DEMO

# BARCOS JUGADOR VERSION DEMO
# ala_x = f.barco_por_coordenadas_jugador(1)
# estrella_de_la_muerte = f.barco_por_coordenadas_jugador(4)
# halcon_milenario = f.barco_por_coordenadas_jugador(4)

# BARCOS MÁQUINA ALEATORIOS VERSION DEMO
# maquina_1a = f.barco_aleatorio_maquina(1)
# maquina_4b = f.barco_aleatorio_maquina(4)
# maquina_4a = f.barco_aleatorio_maquina(4)

# BARCOS MÁQUINA FIJOS VERSION DEMO
# maquina_1a = [(0,0),(0,1)]
# maquina_4b = [(2,2),(3,2),(4,2),(5,2)]
# maquina_4a = [(5,5),(5,6),(5,7),(5,8)]


# LISTA DE BARCOS
# lista_de_barcos_jug = [ala_x, estrella_de_la_muerte, halcon_milenario]
# lista_de_barcos_maq = [maquina_1a, maquina_4a, maquina_4b]
