public class FatorialRecursivo {

    // Método recursivo para calcular o fatorial
    public static int fatorial(int n) {
        // Caso base: fatorial de 0 ou 1 é 1
        if (n == 0 || n == 1) {
            return 1;
        }
        // Caso recursivo: n * fatorial de (n-1) - CAda chamada recursiva é feita em seu contexto e consome muita melhora
        return n * fatorial(n - 1);                // A recursão eu salvo o que eu estou fazendo um registro
    }

    public static void main(String[] args) {
        int numero = 5; // Altere este valor para testar com outros números
        int resultado = fatorial(numero);
        System.out.println("O fatorial de " + numero + " é: " + resultado);
    }
}
