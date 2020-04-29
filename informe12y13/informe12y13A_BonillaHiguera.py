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

lista_prueba1 = [1,2,3,4,5,6,7,8,9,10] 
lista_prueba2 = [11,12,13,14,15,16,17]
lista_r = combinador(lista_prueba1,lista_prueba2)
print(lista_r)

