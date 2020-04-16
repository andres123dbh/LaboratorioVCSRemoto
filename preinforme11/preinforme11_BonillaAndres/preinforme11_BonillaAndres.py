import numpy as np

nombres_videojuegos=np.array(
["Final Fantasy VII Remake","Persona 5: Royal","Call of Duty: Modern Warfare 2 Campaign Remastered","Resident Evil 3","Nioh 2","Days Gone","Death Stranding","Call of Duty: Modern Warfare","Star Wars Jedi: Fallen Order","Call of Duty: Warzone","Dragon Ball Z Kakarot","One Piece: Pirate Warriors 4","Paper Beast","Control","PES 2020","Granblue Fantasy: Versus","DOOM Eternal","FIFA 20","NBA 2K20","A Plague Tale: Innocence","Remnant: From the Ashes","Ghost Recon: Breakpoint","Dreams","Borderlands 3","GreedFall"])

videojuegos = np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
[9,9.5,8.5,8,7.5,7.5,9,9,9,8.5,8,7,7,8,8.5,7.5,9,8.5,8.5,9,8.5,6.5,9,9,8],
[60,60,20,60,60,40,60,60,60,0,78,60,30,60,60,60,60,60,60,50,40,60,40,60,50]])

def promedio_precio(videojuegos):
    
    print("El promedio del precio de todos los juegos de PS4 es",videojuegos[2, :].mean(),"dólares")

def menor_precio(videojuegos):
    organizados=np.sort(videojuegos[2, :])
    return organizados[0]

def mayor_precio(videojuegos):
    organizados=np.sort(videojuegos[2, :])
    return organizados[24]
    

def buscar_nombre(menor,mayor,nombres_videojuegos):
    print("El juego con mayor precio es ",nombres_videojuegos[10],"que cuesta",mayor)
    print("El juego con menor precio es ",nombres_videojuegos[9],"que cuesta",menor)

def menor_valoracion(videojuegos):
    organizados=np.sort(videojuegos[1, :])
    return organizados[0]

def mayor_valoracion(videojuegos):
    organizados=np.sort(videojuegos[1, :])
    return organizados[24]
    

def buscar_nombre_valoracion(menor,mayor,nombres_videojuegos):
    print("El juego con mayor valoracion es ",nombres_videojuegos[1],"con",mayor)
    print("El juego con menor valoracion es ",nombres_videojuegos[21],"con",menor)

mayor = float(mayor_precio(videojuegos))
menor = float(menor_precio(videojuegos))

def diferencia_precio(menor,mayor):
    print("La diferencia de precio entre el mas costoso y el mas economico de los juegos es",mayor-menor)

def promedio_valoracion(videojuegos):
    
    print("El promedio de la valoracion de todos los juegos de PS4 es",videojuegos[1, :].mean())

def comparar(videojuegos,nombres_videojuegos):
    print("El",int(videojuegos[0,0]),"del ranking es",nombres_videojuegos[0],"tiene una valoracion de",videojuegos[1,0],"y tiene un precio de",videojuegos[2,0],"dolares")
    print("El",int(videojuegos[0,24]),"del ranking es",nombres_videojuegos[24],"tiene una valoracion de",videojuegos[1,24],"y tiene un precio de",videojuegos[2,24],"dolares")

def todos(videojuegos,nombres_videojuegos):
    for i in range(0,25):
        print("El",int(videojuegos[0,i]),"del ranking es",nombres_videojuegos[i],"tiene un precio de",videojuegos[2,i],"dolares")
todos(videojuegos,nombres_videojuegos)