import numpy as np

def generador(v_minimo,v_maximo):
    generado = np.random.randint(v_minimo,v_maximo+1, size=48).reshape(4,12)
    return generado

ingresos = generador(100,180)
egresos = generador(60,130)

print("Ingresos: ",ingresos)
print("Egresos: ",egresos)