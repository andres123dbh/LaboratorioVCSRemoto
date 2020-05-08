import random
partidas_ganadas = 0
partidas_perdidas = 0 
seguir_jugando = "YES"
while seguir_jugando != "NO":
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

    def sumar_cartas(lista_cartas,baraja):
        suma = 0
        for i in lista_cartas:
            suma = suma + baraja[i]
        if suma <= 10:
            baraja["♥(C)A"] = 11
            baraja["♦(D)A"] = 11
            baraja["♣(T)A"] = 11
            baraja["♠(P)A"] = 11
            suma = 0
            for i in lista_cartas:
                suma = suma + baraja[i]
        if suma == 21:
            mensaje = ("Felcitaciones,ganó el juego con 21")
            return mensaje
        elif suma > 21:
            mensaje = ("Perdistes el juego")
            return mensaje
        else:
            return suma

    resultado = sumar_cartas(cartas_jugador,baraja)

    def mostrar(lista_cartas,baraja):
        suma = 0
        for i in lista_cartas:
            suma = suma + baraja[i]
        if suma <= 10:
            baraja["♥(C)A"] = 11
            baraja["♦(D)A"] = 11
            baraja["♣(T)A"] = 11
            baraja["♠(P)A"] = 11
            suma = 0
            for i in lista_cartas:
                suma = suma + baraja[i]
        print("Sus cartas son:",lista_cartas)
        print("La suma de su cartas es:",suma)
        return suma

    mostrar(cartas_jugador,baraja)

    if isinstance(resultado, str):
        print(resultado)
    elif isinstance(resultado, int):
        if resultado < 21:
            juega = int(input("Si desea mas cartas escriba 1 de lo contrario 2: "))
            while juega != 2:
                if juega == 1:
                    cartas_jugador, lista_baraja = repartir(baraja,cartas_jugador,lista_baraja)
                    resultado = sumar_cartas(cartas_jugador,baraja)
                    mostrar(cartas_jugador,baraja)
                    if isinstance(resultado, str):
                        print(resultado)
                        break
                    else:
                        juega = int(input("Si desea mas cartas escriba 1 de lo contrario 2: "))
                else:
                    while juega != 1 and juega != 2:
                        print("No registro una opcion valida")
                        juega = int(input("Si desea mas cartas escriba 1 de lo contrario 2: "))

    print("El jugador quedo con:")
    mostrar(cartas_jugador,baraja)
    print("Turno del tallador")
    if isinstance(resultado, str):
        print("El tallador no juega porque al jugador le salio el mensaje:")
        print(resultado)
    else:
        cartas_tallador, lista_baraja = repartir(baraja,cartas_tallador,lista_baraja)
        resultado2 = sumar_cartas(cartas_tallador,baraja)
        mostrar(cartas_tallador,baraja)
        while resultado2 < 21:
            if resultado2 <= resultado: 
                cartas_tallador, lista_baraja = repartir(baraja,cartas_tallador,lista_baraja)
                resultado2 = sumar_cartas(cartas_tallador,baraja)
                mostrar(cartas_tallador,baraja)
                if isinstance(resultado2, str):
                            print(resultado2)
                            break
            elif resultado2 > resultado:
                print("Gano el tallador con:")
                mostrar(cartas_tallador,baraja)
                break

    print("Recuento final del juego")
    print("")
    print("El jugador quedo con:")
    jugador = mostrar(cartas_jugador,baraja)
    print("El tallador quedo con:")
    tallador = mostrar(cartas_tallador,baraja)

    if jugador > tallador and jugador <= 21:
        print("Gano el jugador")
        partidas_ganadas += 1
    elif tallador > jugador and tallador <= 21:
        print("Gano el tallador")
        partidas_perdidas += 1
    elif jugador > tallador and jugador > 21:
        print("Gano el tallador")
        partidas_perdidas += 1
    elif tallador > jugador and tallador > 21:
        print("Gano el jugador")
        partidas_ganadas += 1

    print("Partidas ganadas:",partidas_ganadas)
    print("Partidas perdidas:",partidas_perdidas)

    seguir_jugando = input("Escriba YES si desea seguir jugando y NO para dejar de jugar: ")
    while seguir_jugando != "NO" and seguir_jugando != "YES":
        print("Digito una opcion invalida")
        seguir_jugando = input("Escriba YES para seguir jugando y NO para dejar de jugar: ")

