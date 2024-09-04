# Criando a lista com valores aleatórios
import random

# Gerando estrutura linear desordenada
class EstruturaLinear:
    def __init__(self):
        self.elementos = []

    def receber_elementos(self):
        while True:
            elemento = input("Digite um valor para adicionar à lista (ou 'sair' para finalizar): ")
            if elemento.lower() == 'sair':
                break
            try:
                # Convertendo o valor para inteiro antes de adicionar à lista
                self.elementos.append(int(elemento))
            except ValueError:
                print("Por favor, digite um número válido ou 'sair' para finalizar.")
    
    def criar_lista_aleatoria(self):
        lista_aleatoria = self.elementos[:]
        random.shuffle(lista_aleatoria)
        return lista_aleatoria
    
    def bubsort(self, lista_aleatoria):
        size = len(lista_aleatoria)
        cont = 0
        
        for i in range(size -1): # Para cada item na lista:
            swap = False
            for j in range (size -1): # Compare com os itens
                cont += 1
                if lista_aleatoria[j] > lista_aleatoria[j + 1]:
                    lista_aleatoria[j], lista_aleatoria[j + 1] = lista_aleatoria[j + 1], lista_aleatoria[j]
                    swap = True
            if not swap:
                break

        return lista_aleatoria, cont

            




# Exemplo de uso da classe
estrutura = EstruturaLinear()
estrutura.receber_elementos()

# Criar uma lista embaralhada a partir dos elementos recebidos
lista_aleatoria = estrutura.criar_lista_aleatoria()
print("Lista embaralhada:", lista_aleatoria)

# Ordenar a lista usando Bubble Sort
lista_ordenada = estrutura.bubsort(lista_aleatoria)
print("Lista ordenada:", lista_ordenada)


# contabilizar o numero de operações necessárias

lista_ordenada, operacoes = estrutura.bubsort(lista_aleatoria)
print(f"Número total de operações: {operacoes}")

# ordenar e classificar o número de operações

# Chama o método bubsort

# Faça uma busca sequencial no vetor ordenado
# contabilize o npumero de operações
# Faça uma busca binária e contabilize o número de operações também
# Exemplo 
    

