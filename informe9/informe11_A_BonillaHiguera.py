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


print(ingresos)
imprimir(ingresos)
print(egresos)
imprimir(egresos)