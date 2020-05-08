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

print(baraja)
