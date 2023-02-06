# p03.py

# Autor:Déric Augusto França de Sales
# Matrícula: 96718
# Data:  18/02/2021
# Atualização: 18/02/2021

# Este programa contém o princípio de desenvolvimento do jogo Campo Minado. 
# Através dos parâmetros de número de linhas, colunas e bombas, a função principal imprime 2 matrizes coloridas do jogo,
# uma que mostra apenas as bombas, e a outra que mostra as bombas e as indicações de quantas bombas há nas casas adjascentes.

import numpy as np
import random
from termcolor import colored

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
  tabuleiro = np.zeros( (linhas, colunas), dtype=int )
  return tabuleiro

# Coloque sua implementação aqui.
def posicionaBombas(quantidade, tabuleiro, semente=None) :
  while quantidade != 0:
    i,j = sorteiaPosicao(tabuleiro,semente)
    tabuleiro[i][j] = -1
    quantidade += -1

# Coloque sua implementação aqui.
def calculaTabuleiro(tabuleiro) :

  for i in range(len(tabuleiro)) :
    for j in range(len(tabuleiro[0])) :
      
      #Encontrando bombas
      if tabuleiro[i][j] == -1:

        #Preenchendo linha de cima 
        if i != 0:
          if j != 0:  
            tabuleiro[i-1][j-1] += 1 if tabuleiro[i-1][j-1] !=-1 else 0 #Elemento esquerda e em cima

          if j!= len(tabuleiro[0])-1: 
            tabuleiro[i-1][j+1] += 1 if tabuleiro[i-1][j+1] !=-1 else 0  #Elemento direita e em cima
  
          tabuleiro[i-1][j] += 1 if tabuleiro[i-1][j] !=-1 else 0  #Elemento em cima

        #Preenchendo linha de baixo 
        if i != len(tabuleiro)-1:
          if j != 0:  
            tabuleiro[i+1][j-1] += 1 if tabuleiro[i+1][j-1] !=-1 else 0  #Elemento esquerda e em baixo

          if j != len(tabuleiro[0])-1:  
            tabuleiro[i+1][j+1] += 1 if tabuleiro[i+1][j+1] !=-1 else 0  #Elemento direita e em baixo

          tabuleiro[i+1][j] += 1 if tabuleiro[i+1][j] !=-1 else 0  #Elemento em baixo

        #Preenchendo dos lados
        if j != 0:
          tabuleiro[i][j-1] += 1 if tabuleiro[i][j-1] !=-1 else 0  #Elemento da esquerda
      
        if j != len(tabuleiro[0])-1:
          tabuleiro[i][j+1] += 1 if tabuleiro[i][j+1] !=-1 else 0  #Elemento da direita
   
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
