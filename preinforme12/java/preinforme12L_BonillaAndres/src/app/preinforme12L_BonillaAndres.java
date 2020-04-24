package app;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class preinforme12L_BonillaAndres {
    public static void main(String[] args) throws Exception {
        ArrayList<Double> presion_promedio = new ArrayList<>();
        presion_promedio.add(110.06);
        presion_promedio.add(107.89);
        presion_promedio.add(108.45);
        presion_promedio.add(108.49);
        presion_promedio.add(109.03);
        presion_promedio.add(110.11);
        presion_promedio.add(109.87);
        presion_promedio.add(119.38);
        presion_promedio.add(119.35);
        presion_promedio.add(116.34);
        presion_promedio.add(117.73);
        presion_promedio.add(120.01);
        presion_promedio.add(118.19);
        presion_promedio.add(119.53);
        presion_promedio.add(117.09);
        presion_promedio.add(118.03);
        presion_promedio.add(118.65);
        presion_promedio.add(117.47);
        presion_promedio.add(117.49);
        presion_promedio.add(109.65);
        presion_promedio.add(110.44);
        presion_promedio.add(110.51);
        presion_promedio.add(107.38);
        presion_promedio.add(109.26);
        presion_promedio.add(106.18);
        presion_promedio.add(109.36);
        presion_promedio.add(106.61);
        presion_promedio.add(105.16);
        presion_promedio.add(110.11);
        presion_promedio.add(105.48);
        presion_promedio.add(108.37);
        presion_promedio.add(107.59);
        presion_promedio.add(108.91);
        presion_promedio.add(108.35);
        presion_promedio.add(109.57);
        presion_promedio.add(122.56);
        presion_promedio.add(124.44);
        presion_promedio.add(125.97);
        presion_promedio.add(121.03);
        presion_promedio.add(121.22);
        presion_promedio.add(122.41);
        presion_promedio.add(122.15);
        presion_promedio.add(124.52);
        presion_promedio.add(123.35);
        presion_promedio.add(125.76);
        presion_promedio.add(121.08);
        presion_promedio.add(122.29);
        presion_promedio.add(105.42);
        presion_promedio.add(110.67);
        presion_promedio.add(107.73);
        presion_promedio.add(105.76);
        presion_promedio.add(107.85);


        double media = 0;
        double sumatoria = 0;
        double desviacion = 0;
        double diferencia = 0;
        for (int i = 0;i< 52; i++){
            double temperatura = (presion_promedio.get(i)*0.51)/(0.01716*8.3145);
            media = media + (temperatura - 273.15);
            
        }
        media = media / presion_promedio.size();
        for (int i = 0;i< 52; i++){
            double temperatura = (presion_promedio.get(i)*0.51)/(0.01716*8.3145);
            temperatura = temperatura - 273.15;
            diferencia = Math.pow((temperatura - media),2);
            sumatoria = sumatoria + diferencia;
        }
        desviacion = Math.sqrt((sumatoria/(presion_promedio.size()-1)));
        ArrayList nueva_lista = new ArrayList<>();
        ArrayList lista_supera = new ArrayList<>();
        ArrayList lista_bajo = new ArrayList<>();
        int semana = 1;
        for (int i = 0;i< 52; i++){
            double temperatura = (presion_promedio.get(i)*0.51)/(0.01716*8.3145);
            temperatura = temperatura - 273.15;
            if (temperatura < media){
                lista_bajo.add(semana);
                semana += 1;
            }
            else if(lista_bajo.size() != 0){
                    nueva_lista.add(lista_bajo);
                    lista_bajo = new ArrayList<>();
            }
            if (i == 51 && lista_bajo.size() != 0){
                nueva_lista.add(lista_bajo);
            }
            if (temperatura > media){
                lista_supera.add(semana);
                semana += 1;
            }
            else if(lista_supera.size() != 0){
                    nueva_lista.add(lista_supera);
                    lista_supera = new ArrayList<>();
            }
            if (i == 51 && lista_supera.size() != 0){
                nueva_lista.add(lista_supera);
            }
        }
        double suma_desviacion = 0;
        double media_desviacion_1 = 0;
        double media_desviacion_2 = 0;
        double media_desviacion_3 = 0;
        double media_desviacion_4 = 0;
        double media_desviacion_5 = 0;
        double suma_desviacion_total = 0;
            for (int a = 0;a < 7; a++){
                double temperatura = (presion_promedio.get(a)*0.51)/(0.01716*8.3145);
            media = media + (temperatura - 273.15);
            for (int e = 0;e< 7; e++){
                temperatura = (presion_promedio.get(e)*0.51)/(0.01716*8.3145);
                temperatura = temperatura - 273.15;
                diferencia = Math.pow((temperatura - media),2);
                sumatoria = sumatoria + diferencia;
            }
            desviacion = Math.sqrt((sumatoria/(7-1)));
            media_desviacion_1 = suma_desviacion / 7;
            }
            
            for (int a = 0;a < 12; a++){
                double temperatura = (presion_promedio.get(a)*0.51)/(0.01716*8.3145);
                media = media + (temperatura - 273.15);
                for (int e = 0;e< 12; e++){
                    temperatura = (presion_promedio.get(e)*0.51)/(0.01716*8.3145);
                    temperatura = temperatura - 273.15;
                    diferencia = Math.pow((temperatura - media),2);
                    sumatoria = sumatoria + diferencia;
                }
                desviacion = Math.sqrt((sumatoria/(12-1)));
                media_desviacion_2 = suma_desviacion / 12;
            }
            for (int a = 0;a < 12; a++){
                double temperatura = (presion_promedio.get(a)*0.51)/(0.01716*8.3145);
                media = media + (temperatura - 273.15);
                for (int e = 0;e< 12; e++){
                    temperatura = (presion_promedio.get(e)*0.51)/(0.01716*8.3145);
                    temperatura = temperatura - 273.15;
                    diferencia = Math.pow((temperatura - media),2);
                    sumatoria = sumatoria + diferencia;
                }
                desviacion = Math.sqrt((sumatoria/(12-1)));
                media_desviacion_3 = suma_desviacion / 12;
            }
            for (int a = 0;a < 16; a++){
                double temperatura = (presion_promedio.get(a)*0.51)/(0.01716*8.3145);
                media = media + (temperatura - 273.15);
                for (int e = 0;e< 16; e++){
                    temperatura = (presion_promedio.get(e)*0.51)/(0.01716*8.3145);
                    temperatura = temperatura - 273.15;
                    diferencia = Math.pow((temperatura - media),2);
                    sumatoria = sumatoria + diferencia;
                }
                desviacion = Math.sqrt((sumatoria/(16-1)));
                media_desviacion_4 = suma_desviacion / 16;
            }
            for (int a = 0;a < 5; a++){
                double temperatura = (presion_promedio.get(a)*0.51)/(0.01716*8.3145);
                media = media + (temperatura - 273.15);
                for (int e = 0;e< 5; e++){
                    temperatura = (presion_promedio.get(e)*0.51)/(0.01716*8.3145);
                    temperatura = temperatura - 273.15;
                    diferencia = Math.pow((temperatura - media),2);
                    sumatoria = sumatoria + diferencia;
                }
                desviacion = Math.sqrt((sumatoria/(5-1)));
                media_desviacion_5 = suma_desviacion / 5;
            }
            suma_desviacion_total = (media_desviacion_1 + media_desviacion_2 + media_desviacion_3 + media_desviacion_4 + media_desviacion_5);
            System.out.println("La media de la media de la desviacion estandar a cada listas es " + suma_desviacion_total + " y la desviacion estandar de todo es " + desviacion);
            System.out.println ("Se diferencia porque en la primera se toman rangos por separado donde son superiores o por debajo \n de la media para sacar una desviacion estandar por cada lista que hay para al final calcular la media de \n estas desviaciones y en el segundo se toman en cuenta todos los datos para una unica desviacio estandar, \n por esto es que dan diferentes desviaciones");
    }
}