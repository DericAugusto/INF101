# p13.py
# Programador:
# Matrícula:
# Data de criação:
# Data de atualização:
# Produz um horário escolar usando uma heurística muito simples baseada
# na estrutura de dados conjunto. Os dados de entrada são as dsiciplinas
# a ser oferecidas e as matrículas dos alunos que farão algumas das
# disciplinas oferecidas.

import sys

def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDisc = 'disciplinas.txt'
    nomeArqMatric = 'matriculas.txt'
    if len(sys.argv) > 1:
        nomeArqDisc = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatric = sys.argv[2]
    
    discs = leia_arq_disciplinas(nomeArqDisc)
    matrics = leia_arq_matriculas(nomeArqMatric)

    hor = faz_horario_escolar(discs, matrics)
    # Imprime as sessões não conflitantes do horário.
    print('\nSessões:')
    for i in range(len(hor)):
        print('{:3d}: '.format(i), sorted(hor[i]))


# Lê uma disciplina por linha do arquivo cujo nome externo é 'nomearq'.
# Retorna a lista de disciplinas lidas.
####                                                                 ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: leia_arq_disciplinas(nomearq) #
####                                                                 ####




# Lê, por linha, o nome de um aluno e as disciplinas em que ele se matriculou.
# Os dados em cada linha são separados por uma vírgula. O nome externo do
# arquivo é passado como parâmetro. Retorna um dicionário em que a chave é o
# nome de um aluno e o valor associado é o conjunto de disciplinas em que o
# aluno se matriculou.
####                                                                 ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: leia_arq_matriculas(nomearq)  #
####                                                                 ####




####                                                                    ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: faz_horario_escolar(disciplinas, #
#                                                             matriculas)  #
####                                                                    ####


    

if __name__ == '__main__':
    main()
