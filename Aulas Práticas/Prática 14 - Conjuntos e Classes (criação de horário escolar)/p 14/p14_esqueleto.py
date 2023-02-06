# p14.py
# Programador: 
# Matrícula: 
# Criado em: 
# Atualizado em: 
# (Escreva aqui uma breve descrição sobre o que o programa faz.)

import sys

####                                                                        ####
# DECLARE AQUI A CLASSE RegistroEscolar com todos os seus métodos (e atributos)#
####                                                                        ####






def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDiscs = 'disciplinas.txt'
    nomeArqMatrics = 'matriculas.txt'
    if len(sys.argv) > 1:
        nomeArqDiscs = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatrics = sys.argv[2]
    
    # Cria uma instância da classe RegistroEscolar.
    res = RegistroEscolar(2020, 2)
    
    # Estabelece as disciplinas do período instanciado.
    res.set_disciplinas(nomeArqDiscs)
    
    # Estabelece as matrículas do período instanciado.
    res.set_matriculas(nomeArqMatrics)
    
    # Estabelece as sessões para o horário do período instanciado.
    res.set_horario()
    
    # Imprime as sessões possíveis para o horário do período instanciado.
    print('\nSessões para o período {:4d}/{:d}:'.format(res.periodo[0],\
          res.periodo[1]))
    for i in range(len(res.horario)):
        print('{:3d}: '.format(i), sorted(res.horario[i]))
    print()


if __name__ == '__main__':
    main()

