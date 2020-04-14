import numpy as np

utilidad = np.array([27834 ,23789 ,30189 ,30967 ,32501 ,32701 ,31665 ,17155 , 4614 ,834])

año = np.array ([2008 ,2009 ,2010 ,2011 ,2012 ,2013 ,2014 ,2015 ,2016 ,2017])

def diferencia_promedio(utilidad):
    promedio_ultimos_años=(utilidad[8]+utilidad[9])/2
    promedio_primeros_años=(utilidad[0]+utilidad[1])/2
    diferencia_promedio=promedio_ultimos_años-promedio_primeros_años
    print("La diferencia del promedio de los dos ultimos años respecto a los dos primeros es: ",diferencia_promedio)

def diferencia_mayor_menor(utilidad):
    a=np.amin(utilidad)
    b=np.amax(utilidad)
    print("La diferencia del valor mayor y el valor menor es: ",b-a)

def mediana(utilidad):
    print(np.sort(utilidad))
    print("La mediana de los datos es: ",np.median(utilidad))
    print("Esto significa que el 50 por ciento de los datos estan debajo de este valor \n y el otro 50 por ciento encima del valor")

def comparar(utilidad):
    print("Comparando la mediana es ",np.median(utilidad)," y la media es ",np.mean(utilidad))
    print("La diferencia se debe a que la mediana solo tiene en cuenta los datos centrales a diferencia")
    print("de la media que toma en cuenta todos los valores")
    print("Ventajas mediana:")
    print("- Facil de calcular")
    print("- Interpretacion sencilla")
    print("- Se puede calcular si se desconocen los valores extremos")
    print("- Medida mas representativa de datos de escala ordinal")
    print("Desventajas mediana:")
    print("- No intervienen todos los valores")
    print("- No puede definirse para variables cualitativas puras")
    print("Ventajas media:")
    print("- Medida de tendencia mas usada")
    print("- Utiliza todos los datos")
    print("- Sensible a cualquier cambio en los datos")
    print("Desventajas media:")
    print("- No recomendable para distribuciones muy asimetricas")
    print("- No puede calcular para datos cualitativos")

def aporte_utilidad_acumulada(utilidad):
    suma=np.sum(utilidad)
    print(suma)
    a=0
    for i in range(0,10):
        porcentaje=(utilidad[i]*100)/suma
        a=a+porcentaje
        print("En la pocicion ",i+1," aporta un ",porcentaje,"%")
        print(a)


aporte_utilidad_acumulada(utilidad)