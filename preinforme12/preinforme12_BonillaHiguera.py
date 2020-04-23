presion_promedio = [110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]

def diferencia_mayor_menor(lista):
    list.sort(lista)
    diferencia = lista[-1] - lista[0]
    print("La diferencia del mayor y el menor numero es: ",diferencia)

def media_mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        mediana = (lista[int(len(lista) / 2)]+lista[int((len(lista) / 2)-1)])/2
    else:
        mediana = lista[int(len(lista) / 2)]
    suma = 0
    for i in lista:
        suma = suma + i
    media = suma / len(lista)

    print("La mediana es ",mediana," y la media ",media,". La diferencia es")
    print("porque la media tiene en cuenta todos los valores de la lista y la")
    print("mediana los dos o unico valor del centro")

def media(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    media = suma / len(lista)
    return media

media = media(presion_promedio)

def semanas_consecutivas (lista,media):
    cont_mayores = 0
    cont_menores = 0
    nueva_lista = []
    for i in lista:
        if i < media:
            cont_menores += 1
        elif cont_menores != 0:
            nueva_lista.append(["Semanas consecutivas por debajo de la media:",cont_menores])
            cont_menores = 0
        if i  == lista[len(lista)-1] and cont_menores != 0:
            nueva_lista.append(["Semanas consecutivas por debajo de la media:",cont_menores])
        if i > media:
            cont_mayores += 1
        elif cont_mayores != 0:
            nueva_lista.append(["Semanas consecutivas que superan la media:",cont_mayores])
            cont_mayores = 0
        if i  == lista[len(lista)-1] and cont_mayores != 0:
            nueva_lista.append(["Semanas consecutivas que superan la media:",cont_mayores])
    print(nueva_lista)

semanas_consecutivas (presion_promedio,media)