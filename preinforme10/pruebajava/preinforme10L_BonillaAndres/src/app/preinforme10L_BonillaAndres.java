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
        defisit_cada_año(utilidades);
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
            System.out.println("Esto significa que el 50 por ciento de los datos estan debajo de este valor \n y el otro 50 por ciento encima del valor");
        }
        else{
            mediana = utilidades[(utilidades.length-1)/2];
            System.out.println("La mediana de los datos es: " + mediana);
            System.out.println("Esto significa que el 50 por ciento de los datos estan debajo de este valor \n y el otro 50 por ciento encima del valor");
        }
        
        
    }

    public static void comparar(int utilidades[]) {
        Arrays.sort(utilidades);
        int mediana = 0;
        if (utilidades.length%2==0){
            mediana =  (utilidades[utilidades.length/2]+ utilidades[(utilidades.length/2)-1] )/ 2;
        }
        else{
            mediana = utilidades[(utilidades.length-1)/2];
        }
        float suma = 0;
        for (int i=0;i<utilidades.length;i++){
            suma=suma+utilidades[i];
        }
        System.out.println("La media es "+suma/utilidades.length+", la mediana de los datos es " + mediana+".5");
        System.out.println("La diferencia se debe a que la mediana solo tiene en cuenta los datos centrales a diferencia");
        System.out.println("de la media que toma en cuenta todos los valores");
        System.out.println("Ventajas mediana:");
        System.out.println("- Facil de calcular");
        System.out.println("- Interpretacion sencilla");
        System.out.println("- Se puede calcular si se desconocen los valores extremos");
        System.out.println("- Medida mas representativa de datos de escala ordinal");
        System.out.println("Desventajas mediana:");
        System.out.println("- No intervienen todos los valores");
        System.out.println("- No puede definirse para variables cualitativas puras");
        System.out.println("Ventajas media:");
        System.out.println("- Medida de tendencia mas usada");
        System.out.println("- Utiliza todos los datos");
        System.out.println("- Sensible a cualquier cambio en los datos");
        System.out.println("Desventajas media:");
        System.out.println("- No recomendable para distribuciones muy asimetricas");
        System.out.println("- No puede calcular para datos cualitativos");
    }

    public static void aporte_utilidad_acumulada(int utilidades[]) {
        float suma = 0;
        for (int i=0;i<utilidades.length;i++){
            suma=suma+utilidades[i];
        }
        System.out.println(suma);
        for (int i=0;i<10;i++){
            float porcentaje=(utilidades[i]*100)/suma;
            System.out.println("El porsentaje del "+utilidades[i]+" es "+porcentaje);
        }

    }

    public static void defisit_2017(int utilidades[]) {
            int defisit = utilidades[8]-utilidades[9];
            System.out.println("El déficit en la utilidad operacional del año 2017 con respecto a la del año pasado: "+defisit+" Millones COP");
    }

    public static void defisit_cada_año(int utilidades[]) {
        for (int i=0;i<10;i++){
            if (i==9){
                break;
            }
            else{
                float defisit=utilidades[i+1]-utilidades[i];
                float porsentaje_defisit=(defisit*100)/utilidades[i];
                if (porsentaje_defisit>=0){
                    System.out.println("No hubo deficit por que no tuvieron perdidas, el porsentaje de ganancia es: "+porsentaje_defisit);
                }
                else{
                    System.out.println("El deficit del año fue: "+(-1*porsentaje_defisit));
                }
            }
        }   
    }
}