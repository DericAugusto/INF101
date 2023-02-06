# p03.py
# Autor:
# Matrícula:
# Data:
# Atualização:
# (Escreva aqui um breve comentário sobre o que o programa faz.)

import numpy as np
import random
from termcolor import colored

def imprimeTabuleiroSimples(tabuleiro) :
  # print sem argumentos imprime uma linha vazia
  print()
  
  # Funcao len de um array 2D pega o número de linhas, exemplo len(arr)
  # Funcao len da primeira posição de um array 2D pega o número de colunas,
  # exemplo len(arr[0])
  for i in range(len(tabuleiro)) :
    print('| ', end='')
    for j in range(len(tabuleiro[0])) :
      print('{:2d}'.format(tabuleiro[i][j]), end=' ')
    print('|')

  # print sem argumentos imprime uma linha vazia
  print()


def imprimeTabuleiro ( tabuleiro ) :

  # print sem argumentos imprime uma linha vazia
  print()
  
  # Funcao len de um array 2D pega o número de linhas, exemplo len(arr)
  # Funcao len da primeira posição de um array 2D pega o número de colunas,
  # exemplo len(arr[0])
  for i in range(len(tabuleiro)) :
    for j in range(len(tabuleiro[0])) :
      if tabuleiro[i][j] == -1 :
        print(colored('B','red'), end=' ')
      elif tabuleiro[i][j] == 0 :
        print(colored('█','grey'), end=' ')
      else :
        print(colored(tabuleiro[i][j],'cyan'), end=' ')
    print()

  # print sem argumentos imprime uma linha vazia
  print()


def sorteiaPosicao(tabuleiro, semente=None) :
  if semente is not None:
    random.seed(semente)
  while True :
    i = random.randint(0, len(tabuleiro) - 1)
    j = random.randint(0, len(tabuleiro[0]) - 1)
    if tabuleiro[i][j] != -1 :
      break
  return i, j


# Inicializa com zeros um tabuleiro de tamanho definido.
# Coloque sua implementação aqui.
def inicializaTabuleiro(linhas, colunas=-1) :



# Coloque sua implementação aqui.
def posicionaBombas(quantidade, tabuleiro, semente=None) :



# Coloque sua implementação aqui.
def calculaTabuleiro(tabuleiro) :

        

def main(numero_linhas, numero_colunas, numero_bombas) :
  tabuleiro = inicializaTabuleiro( numero_linhas, numero_colunas )
  posicionaBombas(numero_bombas, tabuleiro, 111)
  imprimeTabuleiro(tabuleiro)
  calculaTabuleiro(tabuleiro)
  imprimeTabuleiro(tabuleiro)


numero_linhas = 8
numero_colunas = 8
numero_bombas = 10

main(numero_linhas, numero_colunas, numero_bombas)
