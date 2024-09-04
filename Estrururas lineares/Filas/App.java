/**
 * App
 */
public class App {

    public static void main(String[] args) {
        Minhafila mp = new Minhafila();
        for(int i=0; i<10; i++){
            mp.push(i);
            System.out.println("Inserindo o valor "+i+" na fila");
        }

        System.out.println("\n-=-=-=-==-=-=-=-\n");
        while (!mp.isEmpty()) {
            System.out.println("Removendo o valor "+ mp.pop()+" da fila");
        }
            
    }
}
