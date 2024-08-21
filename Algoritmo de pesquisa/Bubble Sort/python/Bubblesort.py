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
            self.elementos.append(elemento)
    
    def criar_lista_aleatoria(self):
        lista_aleatoria = self.elementos[:]
        random.shuffle(lista_aleatoria)
        return lista_aleatoria
    
# Busca sequencial em vetor desordenado
    def bubblesort(self, lista_aleatoria):
        n = len(lista_aleatoria)
        
        for i in range(n):
            # Flag para verificar se houve troca
            trocou = False
            
            for j in range(0, n-i-1):
                if lista_aleatoria[j] > lista_aleatoria[j+1]:
                    # Troca os elementos se eles estiverem fora de ordem
                    lista_aleatoria[j], lista_aleatoria[j+1] = lista_aleatoria[j+1], lista_aleatoria[j]
                    trocou = True
            
            # Se não houve troca, a lista já está ordenada
            if not trocou:
                break

        return lista_aleatoria


# contabilizar o numero de operações necessárias
# ordenar e classificar o número de operações
# Faça uma busca sequencial no vetor ordenado
# contabilize o npumero de operações
# Faça uma busca binária e contabilize o número de operações também
# Exemplo 
    
estrutura = EstruturaLinear()
estrutura.receber_elementos()
lista_aleatoria = estrutura.criar_lista_aleatoria()

lista_sequencial = estrutura.bubblesort()


print("Lista aleatória:", lista_aleatoria)
print("Lista ordenada ", lista_sequencial)
