import numpy as np

utilidad = np.array([27834 ,23789 ,30189 ,30967 ,32501 ,32701 ,31665 ,17155 , 4614 ,834])

año = np.array ([2008 ,2009 ,2010 ,2011 ,2012 ,2013 ,2014 ,2015 ,2016 ,2017])

def diferencia_promedio(utilidad,año):
    promedio_ultimos_años=(utilidad[8]+utilidad[9])/2
    promedio_primeros_años=(utilidad[0]+utilidad[1])/2
    diferencia_promedio=promedio_ultimos_años-promedio_primeros_años
    print("La diferencia del promedio de los dos ultimos años respecto a los dos primeros es: ",diferencia_promedio)

diferencia_promedio(utilidad,año)

