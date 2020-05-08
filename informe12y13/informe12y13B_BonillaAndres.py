import random

ponderado = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"J":10,"Q":10,"K":10}
simbolos = ["♥(C)","♦(D)","♣(T)","♠(P)"]

def combinar(ponderado,simbolos):
    baraja = {}
    for i in simbolos:
        for a in ponderado:
            baraja[i+a] = ponderado[a]
    return baraja

baraja = combinar(ponderado,simbolos)

def revolver(baraja):
    lista = []
    nuevo_diccionario = {}
    for i in baraja:
        lista.append(i)
    random.shuffle(lista)
    for i in lista:
        nuevo_diccionario[i] = baraja[i]
    return nuevo_diccionario

baraja = revolver(baraja)

cartas_jugador = []
cartas_tallador = []
lista_baraja = []

def repartir(baraja,cartas_repartir,lista_baraja):
    if lista_baraja:
        None
    else:
        for i in baraja:
            lista_baraja.append(i)
    if cartas_repartir:
        if len(cartas_repartir) >= 2:
            numero = random.randint(0,len(lista_baraja)-1)
            cartas_repartir.append(lista_baraja[numero])
            lista_baraja.pop(numero)
    else:
        for i in range(0,2):
            numero = random.randint(0,len(lista_baraja)-1)
            cartas_repartir.append(lista_baraja[numero])
            lista_baraja.pop(numero)
    return cartas_repartir,lista_baraja


cartas_jugador, lista_baraja = repartir(baraja,cartas_jugador,lista_baraja)
cartas_tallador, lista_baraja = repartir(baraja,cartas_tallador,lista_baraja)

print(cartas_jugador)
print(cartas_tallador)
print(len(lista_baraja))