ponderado = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"J":10,"Q":10,"K":10}
simbolos = ["♥(C)","♦(D)","♣(T)","♠(P)"]

def combinar(ponderado,simbolos):
    baraja = {}
    for i in simbolos:
        for a in ponderado:
            baraja[i+a] = ponderado[a]
    return baraja

baraja = combinar(ponderado,simbolos)
print(baraja)