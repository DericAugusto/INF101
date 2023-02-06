# Programador: Gabriel Pereira de Calais
# Matrícula: 93506
# Criado em: 11/05/2021
# Atualizado em: 11/05/2021
# Produz um horário escolar usando uma heurística muito simples baseada
# na estrutura de dados conjunto, utilizando métodos e atributos de classe.
# Os dados de entrada são as disciplinas a serem oferecidas e as matrículas
# dos alunos que farão algumas das disciplinas oferecidas.

import sys

####                                                                        ####
# DECLARE AQUI A CLASSE RegistroEscolar com todos os seus métodos (e atributos)#
####                                                                        ####

class RegistroEscolar:
    def __init__(self, ano, periodo):
        self.ano = ano
        self.periodo = periodo
        
    def set_disciplinas(self, nomearq):
        try:
            arq = open(nomearq, 'r')
            self.disciplinas = []
            linha = arq.readline().rstrip('\n')
            while linha != '' :
                self.disciplinas.append( linha )
                linha = arq.readline().rstrip('\n')
            arq.close()
        except OSError:
            print('***Erro ao ler o arquivo***')

    def set_matriculas(self, nomearq):
        try:
            arq = open(nomearq, 'r')
            self.matriculas = {}
            linha = arq.readline().rstrip('\n')
            while linha != '' :
                termos = linha.split(',')
                v0 = termos[0]
                v1 = termos[1:]
                self.matriculas[v0] = v1
                linha = arq.readline().rstrip('\n')
            arq.close()
        except OSError:
            print('***Erro ao ler o arquivo***')

    def set_horario(self):
        emptySet = set()
        conflito = [emptySet for d in self.disciplinas]    
        for a in self.matriculas.keys():
            for d in range(len(self.disciplinas)):
                if self.disciplinas[d] in self.matriculas[a]:
                    conflito[d] = conflito[d].union(self.matriculas[a])
        restante = set(self.disciplinas)
        self.horario = []
        while restante != emptySet:
            i = 0
            d = self.disciplinas[i]
            while d not in restante:
                i = i + 1
                d = self.disciplinas[i]
            sessao = {d}
            tentativa = restante.difference(conflito[i])
            for s in range(len(self.disciplinas)):
                if self.disciplinas[s] in tentativa:
                    if conflito[s].intersection(sessao) == emptySet:
                        sessao.add(self.disciplinas[s])
            restante = restante.difference(sessao)
            self.horario.append(sessao)


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
    print('\nSessões para o período {:4d}/{:d}:'.format(res.ano,\
          res.periodo))
    for i in range(len(res.horario)):
        print('{:3d}: '.format(i), sorted(res.horario[i]))
    print()


if __name__ == '__main__':
    main()

