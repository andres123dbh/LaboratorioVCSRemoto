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
        System.out.println(nueva_lista);
    }    
}


