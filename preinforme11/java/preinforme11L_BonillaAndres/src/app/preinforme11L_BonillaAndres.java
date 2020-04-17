package app;
import java.util.Arrays;

public class preinforme11L_BonillaAndres {
    public static void main(String[] args) throws Exception {
        final String nombre_videojuegos[] = {"Final Fantasy VII Remake","Persona 5: Royal","Call of Duty: Modern Warfare 2 Campaign Remastered","Resident Evil 3","Nioh 2","Days Gone","Death Stranding","Call of Duty: Modern Warfare","Star Wars Jedi: Fallen Order","Call of Duty: Warzone","Dragon Ball Z Kakarot","One Piece: Pirate Warriors 4","Paper Beast","Control","PES 2020","Granblue Fantasy: Versus","DOOM Eternal","FIFA 20","NBA 2K20","A Plague Tale: Innocence","Remnant: From the Ashes","Ghost Recon: Breakpoint","Dreams","Borderlands 3","GreedFall"};

        double videojuegos[][]={{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25},
        {9,9.5,8.5,8,7.5,7.5,9,9,9,8.5,8,7,7,8,8.5,7.5,9,8.5,8.5,9,8.5,6.5,9,9,8},
        {60,60,20,60,60,40,60,60,60,0,78,60,30,60,60,60,60,60,60,50,40,60,40,60,50}};

        promedio_valoracion(videojuegos);
        
    }

    public static void promedio_precio(double videojuegos[][]){
        double suma = 0;
        for(int i=0;i<25;i++){
            suma = suma + (videojuegos[2][i]);
        }
        double promedio = suma/25;
        System.out.println("El promedio del precio de los videojuegos es "+promedio+" dolares");

    }

    public static double mayor_precio(double videojuegos[][]){
        double mayor = 0;
        for(int i=0;i<25;i++){
            if (i == 0){
                mayor = videojuegos[2][i];
            }
            if (videojuegos[2][i]>mayor){
                mayor = videojuegos[2][i];
            }
        }
        return mayor;
    }

    public static double menor_precio(double videojuegos[][]){
        double menor = 0;
        for(int i=0;i<25;i++){
            if (i == 0){
                menor = videojuegos[2][i];
            }
            if (videojuegos[2][i]<menor){
                menor = videojuegos[2][i];
            }
        }
        return menor;
    }

    public static double mayor_valoracion(double videojuegos[][]){
        double mayor = 0;
        for(int i=0;i<25;i++){
            if (i == 0){
                mayor = videojuegos[1][i];
            }
            if (videojuegos[1][i]>mayor){
                mayor = videojuegos[1][i];
            }
        }
        return mayor;
    }

    public static double menor_valoracion(double videojuegos[][]){
        double menor = 0;
        for(int i=0;i<25;i++){
            if (i == 0){
                menor = videojuegos[1][i];
            }
            if (videojuegos[1][i]<menor){
                menor = videojuegos[1][i];
            }
        }
        return menor;
    }

    public static void diferencia_precio(double menor,double mayor){
        System.out.println("La diferencia de precio entre el mas costoso y el mas economico de los juegos es "+ (mayor-menor));
    }

    public static void promedio_valoracion(double videojuegos[][]){
        double suma = 0;
        for(int i=0;i<25;i++){
            suma = suma + (videojuegos[1][i]);
        }
        double promedio = suma/25;
        System.out.println("El promedio de las valoraciones de los juegos es "+promedio+" dolares");
    }

}