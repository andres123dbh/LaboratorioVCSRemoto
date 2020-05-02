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

print(paquete)
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
    print(repetida)
    for i in paquete:
        for a in premium:
            if i == a:
                carta_premium.append(i)
    print(carta_premium)
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
print(paquete)
print(jugador)
