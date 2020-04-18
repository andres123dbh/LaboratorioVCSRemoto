import numpy as np
import pandas as pd
import random 

clases_personaje_caracteristica  = np.random.randint(10,19, size=[8,3,6])

def nombre_clase(clase):
    if clase == 0:
        nombre_clase = "Bárbaro"
    elif clase == 1:
        nombre_clase = "Bardo"
    elif clase == 2:
        nombre_clase = "Clérigo"
    elif clase == 3:
        nombre_clase = "Druida"
    elif clase == 4:
        nombre_clase = "Guerrero"
    elif clase == 5:
        nombre_clase = "Mago"
    elif clase == 6:
        nombre_clase = "Paladin"
    elif clase == 7:
        nombre_clase = "Pícaro"
    return nombre_clase

clase_1 = random.randint(0,8)
clase_2 = random.randint(0,8)
clase_3 = random.randint(0,8)

personaje_1 = random.randint(0,3)
personaje_2 = random.randint(0,3)
personaje_3 = random.randint(0,3)

print(clase_2)

nombre_clase_1 = nombre_clase(clase_1)

print(clases_personaje_caracteristica)

print("El primer personaje es un ",nombre_clase_1," y sus caracteristicas son: ",clases_personaje_caracteristica[clase_1,personaje_1,:])

nombre_clase_2 = nombre_clase(clase_2)

print("El primer personaje es un ",nombre_clase_2," y sus caracteristicas son: ",clases_personaje_caracteristica[clase_2,personaje_2,:])

nombre_clase_3 = nombre_clase(clase_3)

print("El primer personaje es un ",nombre_clase_3," y sus caracteristicas son: ",clases_personaje_caracteristica[clase_3,personaje_3,:])

