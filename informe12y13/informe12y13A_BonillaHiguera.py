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
    lista =  [ carta  for carta in jugador if "a" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'a' y son",lista)
    lista =  [ carta  for carta in jugador if "b" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'b' y son",lista)
    lista =  [ carta  for carta in jugador if "c" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'c' y son",lista)
    lista =  [ carta  for carta in jugador if "d" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'd' y son",lista)
    lista =  [ carta  for carta in jugador if "e" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'e' y son",lista)
    lista =  [ carta  for carta in jugador if "f" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'f' y son",lista)
    lista =  [ carta  for carta in jugador if "g" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'g' y son",lista)
    lista =  [ carta  for carta in jugador if "h" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'h' y son",lista)
    lista =  [ carta  for carta in jugador if "i" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'i' y son",lista)
    lista =  [ carta  for carta in jugador if "j" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'j' y son",lista)
    lista =  [ carta  for carta in jugador if "k" in carta[0] ]
    print("Empiezan",len(lista),"cartas cartas con la letra 'k' y son",lista)
    lista =  [ carta  for carta in jugador if "l" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'l' y son",lista)
    lista =  [ carta  for carta in jugador if "m" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'm' y son",lista)
    lista =  [ carta  for carta in jugador if "n" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'n' y son",lista)
    lista =  [ carta  for carta in jugador if "o" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'o' y son",lista)
    lista =  [ carta  for carta in jugador if "p" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'p' y son",lista)
    lista =  [ carta  for carta in jugador if "q" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'q' y son",lista)
    lista =  [ carta  for carta in jugador if "r" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'r' y son",lista)
    lista =  [ carta  for carta in jugador if "s" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 's' y son",lista)
    lista =  [ carta  for carta in jugador if "t" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 't' y son",lista)
    lista =  [ carta  for carta in jugador if "u" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'u' y son",lista)
    lista =  [ carta  for carta in jugador if "v" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'v' y son",lista)
    lista =  [ carta  for carta in jugador if "w" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'w' y son",lista)
    lista =  [ carta  for carta in jugador if "x" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'x' y son",lista)
    lista =  [ carta  for carta in jugador if "y" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'y' y son",lista)
    lista =  [ carta  for carta in jugador if "z" in carta[0] ]
    print("Empiezan",len(lista),"cartas con la letra 'z' y son",lista)

cuantas_empiezan(jugador)
print(jugador)