package app;

public class preinforme11L_BonillaAndres {
    public static void main(String[] args) throws Exception {
        final String nombre_videojuegos[] = {"Final Fantasy VII Remake","Persona 5: Royal","Call of Duty: Modern Warfare 2 Campaign Remastered","Resident Evil 3","Nioh 2","Days Gone","Death Stranding","Call of Duty: Modern Warfare","Star Wars Jedi: Fallen Order","Call of Duty: Warzone","Dragon Ball Z Kakarot","One Piece: Pirate Warriors 4","Paper Beast","Control","PES 2020","Granblue Fantasy: Versus","DOOM Eternal","FIFA 20","NBA 2K20","A Plague Tale: Innocence","Remnant: From the Ashes","Ghost Recon: Breakpoint","Dreams","Borderlands 3","GreedFall"};

        ejemplo();
    }

    public static void ejemplo(){
        double videojuegos[][]={{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25},
        {9,9.5,8.5,8,7.5,7.5,9,9,9,8.5,8,7,7,8,8.5,7.5,9,8.5,8.5,9,8.5,6.5,9,9,8},
        {60,60,20,60,60,40,60,60,60,0,78,60,30,60,60,60,60,60,60,50,40,60,40,60,50}};
        for(int i=0;i<24;i++){
            System.out.println(videojuegos[1][i]);
        }

    }
}