package app;
import java.util.Arrays;

public class preinforme10L_BonillaAndres {
    public static void main(String[] args) throws Exception {
        final int utilidades[] = new int[10];
        utilidades[0]=27834;
        utilidades[1]=23789;
        utilidades[2]=30189;
        utilidades[3]=30967;
        utilidades[4]=32501;
        utilidades[5]=32701;
        utilidades[6]=31665;
        utilidades[7]=17155;
        utilidades[8]=4614;
        utilidades[9]=834;
        mediana(utilidades);
    }

    public static void diferencia_promedio(int utilidades[]) {
        int promedio_ultimos_años=(utilidades[8]+utilidades[9])/2;
        int promedio_primeros_años=(utilidades[0]+utilidades[1])/2;
        int diferencia_promedio=promedio_ultimos_años-promedio_primeros_años;
        System.out.println("La diferencia del promedio de los dos ultimos años respecto a los dos primeros es: "+diferencia_promedio);
    }

    public static void diferencia_mayor_menor(int utilidades[]) {
        Arrays.sort(utilidades);
        int b=utilidades[0];
        int a=utilidades[utilidades. length-1];
        int c=a-b;
        System.out.println("La diferencia del valor mayor y el valor menor es: "+c);
    }

    public static void mediana(int utilidades[]) {
        Arrays.sort(utilidades);
        int mediana = 0;
        if (utilidades.length%2==0){
            mediana =  (utilidades[utilidades.length/2]+ utilidades[(utilidades.length/2)-1] )/ 2;
            System.out.println("La mediana de los datos es: " + mediana+".5");
        }
        else{
            mediana = utilidades[(utilidades.length-1)/2];
            System.out.println("La mediana de los datos es: " + mediana);
        }
        
        
    }
}