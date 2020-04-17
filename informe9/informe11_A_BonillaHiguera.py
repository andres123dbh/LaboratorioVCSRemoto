import numpy as np

v_minimo = int(input("Digite el vaor minomo del parametro"))
v_maximo = int(input("Digite el vaor maximo del parametro"))

def generador(v_minimo,v_maximo):
    generado = np.random.randint(v_minimo,v_maximo+1, size=48).reshape(4,12)
    print(generado)

generador(v_minimo,v_maximo)