import random

cartas =  ["Payne","Hendrix","Stone","Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" ,"Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

def imprimir(lista):
    print("La lista tiene",len(lista),"elementos")
    print("Los cuales son:",lista)

def generador(lista_a,n):
    lista_r = []
    lista_numeros = []
    contador = 0
    if n<=len(lista_a):
        while contador<n:
            numero = random.randint(0,len(lista_a)-1)
            if numero not in lista_numeros:
                lista_numeros.append(numero)
                contador+=1
        for i in lista_numeros:
                lista_r.append(lista_a[i])
        return lista_r
    else:
        print("La cantidad de elemendos que ingreso estan fuera del limite")
        return None

jugador = generador(cartas,10)

def combinador(lista_a,lista_b):
    lista_r = []
    for i in lista_a:
        lista_r.append(i)
    for i in lista_b:
        lista_r.append(i)
    return lista_r

juego = combinador(cartas,premium)

sobre_uno = generador(juego,5)
sobre_dos = generador(juego,5)
sobre_tres = generador(juego,5)

antes_paquete = combinador(sobre_uno,sobre_dos)
paquete = combinador(antes_paquete,sobre_tres)

def loteria (premium,paquete,jugador):
    repetida = []
    unico = []
    carta_premium = []
    for x in paquete:
        if x not in unico:
            unico.append(x)
        else:
            if x not in repetida:
                repetida.append(x)
    for i in paquete:
        for a in premium:
            if i == a:
                carta_premium.append(i)
    if repetida and len(carta_premium)<=1:
        numero = random.randint(0,9)
        if numero == 6:
            print("Felizitaciones")
            for i in jugador:
                for a in premium:
                    if i == a:
                        carta_premium.append(i)
            premium_no_repetidas = [carta for carta in premium if carta not in carta_premium]
            numero_al = random.randint(0,len(premium_no_repetidas)-1)
            if premium_no_repetidas:
                paquete.append(premium_no_repetidas[numero_al])

loteria(premium,paquete,jugador)
for i in paquete:
    jugador.append(i)

jugador = [carta.lower() for carta in jugador]
premium = [carta.lower() for carta in premium]

def cuantas_premium(jugador,premium):
    cuantas_premium = []
    for i in jugador:
        for a in premium:
                    if i == a:
                        cuantas_premium.append(i)
    if cuantas_premium:
        print("El jugador si obtuvo cartas premium y son",cuantas_premium)
    else:
        print("No obtuvo cartas premium")

def cuantas_repetidas(jugador):
    repetida = []
    unico = []
    for x in jugador:
        if x not in unico:
            unico.append(x)
        else:
            if x not in repetida:
                repetida.append(x)
    print("Tiene",len(repetida),"cartas repetidas")
    print(repetida)

def cuantas_veces_aparece(jugador):
    contador = 0
    repetida = []
    unico = []
    for x in jugador:
        if x not in unico:
            unico.append(x)
        else:
            if x not in repetida:
                repetida.append(x)
    for i in range(0,len(unico)):
        for a in jugador:
            if unico[i] == a:
                contador += 1
        print("La carta",jugador[i],"aparece",contador,"veces")
        contador = 0
    print(jugador)

def cuantas_empiezan(jugador):
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for letra in abecedario:
        lista =  [ carta  for carta in jugador if letra in carta[0] ]
        print("Empiezan {} cartas con la letra '{}' y son {}".format(len(lista),letra,lista))

def mayor_menor_longitud(jugador):
    mayor = 0
    menor = 0
    for i in range(0,len(jugador)):
        if i == 0:
            mayor = jugador[i]
            menor = jugador[i]
        if len(jugador[i])>len(mayor):
            mayor = jugador[i]
        if len(jugador[i])<len(menor):
            menor = jugador[i]
    print("La carta con mayor longitud tiene",len(mayor),"palabras y es",mayor)
    print("La carta con menor longitud tiene",len(menor),"palabras y es",menor)

def cuantas_empiezan_premium(jugador,premium):
    cuantas_premium = []
    for i in jugador:
        for a in premium:
                    if i == a:
                        cuantas_premium.append(i)
    if cuantas_premium:
        lista =  [ carta[0]  for carta in cuantas_premium]
        lista2 =  [ carta  for carta in jugador if carta[-1] in lista]
        print(cuantas_premium)
        print(lista)
        print(jugador)
        print(lista2)
        print("Hay",len(lista2),"cartas que terminan con la letra con la que empieza la(s) cartas premium ")
    else:
        print("No tiene cartas premium")

def letras_seguidas(jugador):
    contador_letra = 0
    contado_consecuticas = 0
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista_cant = []
    for letra in abecedario:
        for a in jugador:
            for i in range(0,len(a)):
                if letra == a[i]:
                    contador_letra += 1
                else:
                    if contador_letra > 1:
                        contado_consecuticas += 1
                    contador_letra = 0
            if contador_letra > 1:
                contado_consecuticas += 1
            if contado_consecuticas > 0:
                lista_cant.append(contado_consecuticas)
            contador_letra = 0
            contado_consecuticas = 0
        suma = 0
        for i in lista_cant:
            suma = suma + i
        if suma != 0:
            print("La letra '{}' aparece {} veces de manera consecutiva".format(letra,suma) )
        lista_cant = []

lista_prueba = ["ab","abc","abcd"]

def cantidad_cada_letra(jugador):
    contador_letra = 0
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for letra in abecedario:
        for a in jugador:
            for i in range(0,len(a)):
                if letra == a[i]:
                    contador_letra += 1
        if contador_letra != 0:
            print("La letra '{}' aparece un total de {} veces".format(letra,contador_letra))
        contador_letra = 0

cantidad_cada_letra(jugador)
print(jugador)






