import random

cartas =  ["Payne","Hendrix","Stone","Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" ,"Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

lista_prueba = [1,2,3,4,5,6,7,8,9,10]

def imprimir(lista):
    print("La lista tiene",len(lista),"elementos")
    print("Los cuales son:",lista)

def generador(lista_a,n):
    lista_r = []
    lista_numeros = []
    contador = 0
    if n<=len(lista_a):
        while contador<n:
            numero = random.randint(0,n)
            if numero not in lista_numeros:
                lista_numeros.append(numero)
                contador+=1
        for i in lista_numeros:
                lista_r.append(lista_a[i])
        print(lista_r)
    else:
        print("La cantidad de elemendos que ingreso estan fuera del limite")

n = int(input("Ingrese la cantidad de elementos que desea: "))

generador(lista_prueba,n)

