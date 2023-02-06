# Prática 4 de INF101 - 2021/PER2 - 2 pontos

# Nome: Déric Augusto França de Sales
# Matrícula: 96718
# Data: 04/03/2021

# Descrição:
'''
    No programa são definidas duas listas que são ordenadas e impressas, fazendo uso das funções minimo() e ordena().
'''


def minimo( L, indice_inicial ):
    '''
        Esta função lê uma lista a partir de um dado índice e retorna o índice do menor elemento lido.
    '''
    i_minimo = indice_inicial
    valor = L[indice_inicial]
    for i in range(indice_inicial + 1,  len(L)):
        if L[i] < valor:
            i_minimo = i
            valor = L[i]
    
    return i_minimo


def ordena(L):
    '''
        Esta função ordena uma lista fazendo uso da função minimo().
    '''
    for elemento in range(len(L)-1):

        #Identificando o indice do menor elemento
        i = minimo(L , elemento)

        #Trocando os valores de posição
        menor_valor = L[i]
        L[i] = L[elemento]
        L[elemento] = menor_valor


def main():
    L1 = [36,18,43,9,18,25,14]
    L2 = [43,36,25,18,18,14,9]

    ordena(L1)
    ordena(L2)

    print("Listas ordenadas:")
    print(L1)
    print(L2)


main()