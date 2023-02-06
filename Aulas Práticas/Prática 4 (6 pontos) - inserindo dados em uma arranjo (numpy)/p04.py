# Prática 4 de INF101 - 2021/PER2 - 6 pontos

# Nome: Déric Augusto França de Sales
# Matrícula: 96718
# Data: 25/02/2021

# Descrição:
'''
Este programa recebe várias entradas de números não negativos 
(até que o usuário entre com -1), e faz o cálculo da média de todos os 
números, além de disponibilizar a quantidade de números inseridos.

Observações:
-A função leiaDados() usada para no número máximo de dados que recebe como 
parâmetro ou quando o usuário digita -1.
-A função calculaMedia() calcula a média dos númros dentro de um arranjo
-A função acima() calcula quantos valores do arranjo estão acima do valor m
que recebe como o segundo parâmtro.
'''

import numpy as np


def leiaDados(tam_max):
    print('Entre com uma lista de números não negativos (-1 para terminar):')

    entradas = np.zeros(tam_max, dtype=float)
    num_entradas = 0
    for i in range(len(entradas)):
        entrada = float(input())
        if entrada == -1:
            break
        entradas[i] = entrada
        num_entradas +=1

    dadosDigitados = np.empty(num_entradas, dtype=float)
    for i in range(num_entradas):
        dadosDigitados[i] = entradas[i]

    return dadosDigitados

    
def calculeMedia(dados):
    soma = 0
    for i in range(len(dados)):
        soma += dados[i]

    media = soma/len(dados)
    return media


def acima(dados, m):
    n_acima = 0
    for i in range(len(dados)):
        if dados[i] > m:
            n_acima +=1

    return n_acima


def main():
    dados = leiaDados(20)
    media = calculeMedia(dados)
    n_acima = acima(dados, media)

    print()
    print('A média dos dados é: %0.2f' %media )
    print('Há {} dado(s) acima da média.'.format(n_acima))
    
main()

