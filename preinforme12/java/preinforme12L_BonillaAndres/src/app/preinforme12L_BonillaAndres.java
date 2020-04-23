package app;
import java.util.ArrayList;

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

        double mayor = 0;
        double menor = 0;
        for (int i = 0;i< 52; i++){
            if(i == 0){
                mayor = presion_promedio.get(i);
                menor = presion_promedio.get(i);
            }
            if (presion_promedio.get(i) < menor){
                menor = presion_promedio.get(i);
            }
            if (presion_promedio.get(i) > mayor){
                mayor = presion_promedio.get(i);
            }
        }
        double diferencia = mayor - menor;
        System.out.println("La diferencia del mayor y menor promedio es " + diferencia);
    }
}

