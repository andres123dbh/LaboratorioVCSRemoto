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

def mejor_ciudad(ganancias):
    suma_bucaramanga = 0
    suma_floridablanca = 0
    suma_giron = 0
    suma_pidecuesta = 0
    for i in range(0,12):
        suma_bucaramanga = suma_bucaramanga + ganancias[0,i]
        suma_floridablanca = suma_floridablanca + ganancias[1,i]
        suma_giron = suma_giron + ganancias[2,i]
        suma_pidecuesta = suma_pidecuesta + ganancias[3,i]
    if suma_bucaramanga>suma_floridablanca and suma_bucaramanga>suma_giron and suma_bucaramanga>suma_pidecuesta:
        print("La mejor ciudad es Bucaramanga con ganancias de: ",suma_bucaramanga)
    elif suma_floridablanca>suma_bucaramanga and suma_floridablanca>suma_giron and suma_floridablanca>suma_pidecuesta:
        print("La mejor ciudad es Floridablanca con ganancias de: ",suma_floridablanca)
    elif suma_giron>suma_bucaramanga and suma_giron>suma_floridablanca and suma_giron>suma_pidecuesta:
        print("La mejor ciudad es Giron con ganancias de: ",suma_giron)
    elif suma_pidecuesta>suma_bucaramanga and suma_pidecuesta>suma_floridablanca and suma_pidecuesta>suma_giron:
        print("La mejor ciudad es Pidecuesta con ganancias de: ",suma_pidecuesta)
    print(suma_bucaramanga)
    print(suma_floridablanca)
    print(suma_giron)
    print(suma_pidecuesta)
    print(ganancias)

def peor_ciudad(ganancias):
    suma_bucaramanga = 0
    suma_floridablanca = 0
    suma_giron = 0
    suma_pidecuesta = 0
    for i in range(0,12):
        suma_bucaramanga = suma_bucaramanga + ganancias[0,i]
        suma_floridablanca = suma_floridablanca + ganancias[1,i]
        suma_giron = suma_giron + ganancias[2,i]
        suma_pidecuesta = suma_pidecuesta + ganancias[3,i]
    if suma_bucaramanga<suma_floridablanca and suma_bucaramanga<suma_giron and suma_bucaramanga<suma_pidecuesta:
        print("La ciudad con menores ganancias es Bucaramanga con ganancias de: ",suma_bucaramanga)
        if suma_bucaramanga<0:
            print("La ciudad con peores perdidas es Bucaramanga con ganancias de: ",suma_bucaramanga)
    elif suma_floridablanca<suma_bucaramanga and suma_floridablanca<suma_giron and suma_floridablanca<suma_pidecuesta:
        print("La ciudad con menores ganancias es Floridablanca con ganancias de: ",suma_floridablanca)
        if suma_floridablanca<0:
            print("La ciudad con peores perdidas es Floridablanca con ganancias de: ",suma_floridablanca)
    elif suma_giron<suma_bucaramanga and suma_giron<suma_floridablanca and suma_giron<suma_pidecuesta:
        print("La ciudad con menores ganancias es Giron con ganancias de: ",suma_giron)
        if suma_giron<0:
            print("La ciudad con peores perdidas es Giron con ganancias de: ",suma_giron)
    elif suma_pidecuesta<suma_bucaramanga and suma_pidecuesta<suma_floridablanca and suma_pidecuesta<suma_giron:
        print("La ciudad con menores ganancias es Pidecuesta con ganancias de: ",suma_pidecuesta)
        if suma_pidecuesta<0:
            print("La ciudad con peores perdidas es Pidecuesta con ganancias de: ",suma_pidecuesta)
    print(suma_bucaramanga)
    print(suma_floridablanca)
    print(suma_giron)
    print(suma_pidecuesta)
    print(ganancias)

def mejor_mes(ganancias):
    mes_bucaramanga = 0
    mes_floridablanca = 0
    mes_giron = 0
    mes_pidecuesta = 0
    for i in range(0,12):
        if i == 0:
            mes_bucaramanga=ganancias[0,i]
            mes_floridablanca=ganancias[1,i]
            mes_giron=ganancias[2,i]
            mes_pidecuesta=ganancias[3,i]
        if ganancias[0,i]>mes_bucaramanga:
            mes_bucaramanga=ganancias[0,i]
        if ganancias[1,i]>mes_floridablanca:
            mes_floridablanca=ganancias[1,i]
        if ganancias[2,i]>mes_giron:
            mes_giron=ganancias[2,i]
        if ganancias[3,i]>mes_pidecuesta:
            mes_pidecuesta=ganancias[3,i]
    meses = np.array([[ "Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]])
    print("El mejor mes de Bucaramanga es ",meses[np.where(ganancias == mes_bucaramanga)])
    print("El mejor mes de Floridablanca es ",meses[np.where(ganancias == mes_floridablanca)])
    print("El mejor mes de Giron es ",meses[np.where(ganancias == mes_giron)])
    print("El mejor mes de Piedecuesta es ",meses[np.where(ganancias == mes_pidecuesta)])
    print(ganancias)

mejor_mes(ganancias)