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

clase_1 = random.randint(0,7)
clase_2 = random.randint(0,7)
clase_3 = random.randint(0,7)

personaje_1 = random.randint(0,2)
personaje_2 = random.randint(0,2)
personaje_3 = random.randint(0,2)

if clase_1 == 0 or clase_1 == 4 or clase_1 == 6 or clase_1 == 7:
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_1,personaje_1,i]<15:
            clases_personaje_caracteristica[clase_1,personaje_1,i] = clases_personaje_caracteristica[clase_1,personaje_1,i] + 2
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_1,personaje_1,i]>14:
            clases_personaje_caracteristica[clase_1,personaje_1,i] = clases_personaje_caracteristica[clase_1,personaje_1,i] - 3

if clase_2 == 0 or clase_2 == 4 or clase_2 == 6 or clase_2 == 7:
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_2,personaje_2,i]<15:
            clases_personaje_caracteristica[clase_2,personaje_2,i] = clases_personaje_caracteristica[clase_2,personaje_2,i] + 2
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_2,personaje_2,i]>14:
            clases_personaje_caracteristica[clase_2,personaje_2,i] = clases_personaje_caracteristica[clase_2,personaje_2,i] - 3

if clase_3 == 0 or clase_3 == 4 or clase_3 == 6 or clase_3 == 7:
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_3,personaje_3,i]<15:
            clases_personaje_caracteristica[clase_3,personaje_3,i] = clases_personaje_caracteristica[clase_3,personaje_3,i] + 2
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_3,personaje_3,i]>14:
            clases_personaje_caracteristica[clase_3,personaje_3,i] = clases_personaje_caracteristica[clase_3,personaje_3,i] - 3
    

if clase_1 == 1 or clase_1 == 2 or clase_1 == 3 or clase_1 == 5:
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_1,personaje_1,i]<15:
            clases_personaje_caracteristica[clase_1,personaje_1,i] = clases_personaje_caracteristica[clase_1,personaje_1,i] + 2
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_1,personaje_1,i]>14:
            clases_personaje_caracteristica[clase_1,personaje_1,i] = clases_personaje_caracteristica[clase_1,personaje_1,i] - 3

if clase_2 == 1 or clase_2 == 2 or clase_2 == 3 or clase_2 == 5:
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_2,personaje_2,i]<15:
            clases_personaje_caracteristica[clase_2,personaje_2,i] = clases_personaje_caracteristica[clase_2,personaje_2,i] + 2
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_2,personaje_2,i]>14:
            clases_personaje_caracteristica[clase_2,personaje_2,i] = clases_personaje_caracteristica[clase_2,personaje_2,i] - 3

if clase_3 == 1 or clase_3 == 2 or clase_3 == 3 or clase_3 == 5:
    for i in range (3,6):
        if clases_personaje_caracteristica[clase_3,personaje_3,i]<15:
            clases_personaje_caracteristica[clase_3,personaje_3,i] = clases_personaje_caracteristica[clase_3,personaje_3,i] + 2
    for i in range (0,3):
        if clases_personaje_caracteristica[clase_3,personaje_3,i]>14:
            clases_personaje_caracteristica[clase_3,personaje_3,i] = clases_personaje_caracteristica[clase_3,personaje_3,i] - 3

nombre_clase_1 = nombre_clase(clase_1)
nombre = input("Digite el nombre del personaje: ")

def imprimir(clases_personaje_caracteristica,nombre):
    indices=[nombre]
    df = pd.DataFrame({"Fuerza":clases_personaje_caracteristica[clase_1,personaje_1,0],
    "Destreza":clases_personaje_caracteristica[clase_1,personaje_1,1],
    "Constitución":clases_personaje_caracteristica[clase_1,personaje_1,2],
    "Inteligencia":clases_personaje_caracteristica[clase_1,personaje_1,3],
    "Sabiduría":clases_personaje_caracteristica[clase_1,personaje_1,4],
    "Carisma":clases_personaje_caracteristica[clase_1,personaje_1,5]},index = indices)
    print(df.head())

print("El personaje ",nombre," es un ",nombre_clase_1," y sus caracteristicas son: ")

imprimir(clases_personaje_caracteristica,nombre)
