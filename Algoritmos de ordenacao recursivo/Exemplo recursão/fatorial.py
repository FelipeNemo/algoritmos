def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * fatorial de (n-1)
    return n * fatorial(n - 1)

# Exemplo de uso
numero = 5  # Altere este valor para testar com outros números
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
