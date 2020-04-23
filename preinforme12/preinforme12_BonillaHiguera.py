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

    print("La mediana es ",mediana," y la media ",media,". La diferencia es")
    print("porque la media tiene en cuenta todos los valores de la lista y la")
    print("mediana los dos o unico valor del centro")

def media(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    media = suma / len(lista)
    return media

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

def temperatura(lista):
    semana = 1
    for i in lista:
        temperatura = (i*0.51)/(0.01716*8.3145)
        temperatura = temperatura - 273.15
        print("En la semana",semana,"la temperatura promedio fue",temperatura,"Celsius")
        semana += 1

def desviacion_estandar(lista):
    media = 0
    sumatoria = 0
    for i in lista:
        temperatura = (i*0.51)/(0.01716*8.3145)
        media = media + (temperatura - 273.15)
    media = media / len(lista)
    for i in lista:
        temperatura = (i*0.51)/(0.01716*8.3145)
        temperatura = temperatura - 273.15
        diferencia = (temperatura - media)**2
        sumatoria = sumatoria + diferencia
    desviacion = (sumatoria/(len(lista)-1))**(1/2)
    return desviacion

def semanas_consecutivas_temperatura (lista):
    suma = 0
    semana = 1
    nueva_lista = []
    lista_supera = []
    lista_bajo = []
    for i in lista:
        temperatura = (i*0.51)/(0.01716*8.3145)
        suma = suma + (temperatura - 273.15)
    media = suma / len(lista)
    for i in lista:
        temperatura = (i*0.51)/(0.01716*8.3145)
        temperatura = temperatura - 273.15
        if temperatura < media:
            lista_bajo.append(semana)
            semana += 1
        elif lista_bajo:
            nueva_lista.append(lista_bajo)
            lista_bajo = []
        if temperatura  == ((lista[len(lista)-1]*0.51)/(0.01716*8.3145)) - 273.15 and lista_bajo:
            nueva_lista.append(lista_bajo)
        if temperatura > media:
            lista_supera.append(semana)
            semana += 1
        elif lista_supera:
            nueva_lista.append(lista_supera)
            lista_supera = []
        if temperatura  == ((lista[len(lista)-1]*0.51)/(0.01716*8.3145)) - 273.15 and lista_supera:
            nueva_lista.append(lista_supera)

    return nueva_lista

lista_2 = semanas_consecutivas_temperatura(presion_promedio)

def desviacion_estandar_a_listas(lista):
    media = 0
    sumatoria = 0
    suma_desviacion = 0
    for i in range (0,len(lista)):
        for a in lista[i]:
            temperatura = (a*0.51)/(0.01716*8.3145)
            media = media + (temperatura - 273.15)
        media = media / len(lista)
        for a in lista[i]:
            temperatura = (a*0.51)/(0.01716*8.3145)
            temperatura = temperatura - 273.15
            diferencia = (temperatura - media)**2
            sumatoria = sumatoria + diferencia
        desviacion = (sumatoria/(len(lista[i])-1))**(1/2)
        suma_desviacion = suma_desviacion + desviacion
    media_desviacion = suma_desviacion / len(lista[i])
    return media_desviacion

media_desviacion = desviacion_estandar_a_listas(lista_2)
desviacion_estandar = desviacion_estandar(presion_promedio)

print ("La media de la media de la desviacion estandar a cada listas es",media_desviacion,"y la desviacion estandar de todo es",desviacion_estandar)
print ("Se diferencia porque en la primera se toman rangos por separado donde son superiores o por debajo \n de la media para sacar una desviacion estandar por cada lista que hay para al final calcular la media de \n estas desviaciones y en el segundo se toman en cuenta todos los datos para una unica desviacio estandar, \n por esto es que dan diferentes desviaciones")
        double media = 0;
        double suma = 0;
        for (int i = 0;i< 52; i++){
            suma = suma + presion_promedio.get(i);
        media = suma / presion_promedio.size();
        }
        int cont_mayores = 0;
        int cont_menores = 0;
        ArrayList nueva_lista = new ArrayList<>();
        for (int i = 0;i< 52; i++){
            if (presion_promedio.get(i) < media){
                cont_menores = cont_menores + 1;
            }
            else if(cont_menores != 0){
                    nueva_lista.add(cont_menores);
                    
                    cont_menores = 0;
            }
            if (i == 51 && cont_menores !=0){
                nueva_lista.add(cont_menores);
            }
            if (presion_promedio.get(i) > media){
                cont_mayores = cont_mayores + 1;
            }
            else if(cont_mayores != 0){
                    nueva_lista.add(cont_mayores);
                    
                    cont_mayores = 0;
            }
            if (i == 51 && cont_mayores !=0){
                nueva_lista.add(cont_mayores);
            }
        }