public class Empilhamento {

    // Método recursivo para verificar se um número é primo
    public static boolean ehPrimo(int n, int div) {
        if (n <= 1 || (n % 2 == 0 && n != 2)) {
            return false;
        }
        if (div * div > n) {
            return true;
        }
        if (n % div == 0) {
            return false;
        }
        return ehPrimo(n, div + 2);
    }
}
