public class Main {
    public static void main(String[] args) {
        int numero = 15; // Altere este valor para testar outros números
        if (numero == 2 || (numero > 2 && Empilhamento.ehPrimo(numero, 3))) {
            System.out.println(numero + " é primo");
        } else {
            System.err.println(numero + " não é primo");
        }
    }
}
