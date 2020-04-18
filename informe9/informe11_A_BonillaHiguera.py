import numpy as np
import pandas as pd

def generador(v_minimo,v_maximo):
    generado = np.random.randint(v_minimo,v_maximo+1, size=48).reshape(4,12)
    return generado

ingresos = generador(100,180)
egresos = generador(60,130)

def imprimir(arreglo):
    indices=["Bucaramanga","Floridablanca","Girón","Piedecuesta"]
    df = pd.DataFrame({"Enero":arreglo[:,0],
    "Febrero":arreglo[:,1],
    "Marzo":arreglo[:,2],
    "Abril":arreglo[:,3],
    "Mayo":arreglo[:,4],
    "Junio":arreglo[:,5],
    "Julio":arreglo[:,6],
    "Agosto":arreglo[:,7],
    "Septiembre":arreglo[:,8],
    "Octubre":arreglo[:,9],
    "Noviembre":arreglo[:,10],
    "Diciembre":arreglo[:,11]},index = indices)
    print(df.head())

def calculador(arreglo_1,arreglo_2):
    ganancias = np.random.randint(1,3, size=48).reshape(4,12)
    for i in range(0,4):
        for n in range(0,12):
            ganancias[i,n] = arreglo_1[i,n] -  arreglo_2[i,n] 
    return ganancias

ganancias=calculador(ingresos,egresos)
print("Las ganancias o perdidas son:")
imprimir(ganancias)
print("Los ingresos son:")
imprimir(ingresos)
print("Los egresos son:")
imprimir(egresos)