# p08.py
# Nome: Déric Augusto França de Sales
# Matrícula: 96718
# Data: 25/03/2021
# Atualização: 25/03/2021
# O programa soma dias à uma data informada pelo usuário e retorna o resultado.
#Para isso, recebe primeiro a data, depois a quantidade de dias que serão somadas 
#e após informar o resultado, pergunta se o usuário quer realizar a operação mais uma vez.

def main():
    while True:
        linha = input('\nEntre com uma data (dd mm aaaa):\n')
        n = int(input('Quantos dias a ser adicionados (valor positivo)? '))
        dia, mes, ano = tuple(map(int, linha.split(' ')))
        dian, mesn, anon = adicione_ndias(n, dia, mes, ano)
        print('A data com {} dias adicionados é {:02d}/{:02d}/{:4d}.'
              .format(n, dian, mesn, anon))
        resp = input('Deseja continuar (s/n)? ')
        if resp == 'n' or resp == 'N': break


# Implemente aqui a função bissexto(a).
def bissexto(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

# Implemente aqui a função num_dias_no_mes(m, a).
def num_dias_no_mes(m, a):
    return (29 if bissexto(a) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m-2]

    #               1              2              3   4   5   6   7   8   9   10  11  12
    #numDiasMes = [31, 29 if bissexto(a) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #return numDiasMes[m-1]


# Implemente aqui a função adicione_1dia(d, m, a).
def adicione_1dia(d, m, a):

    # se for o últmo dia do mês
    if d == num_dias_no_mes(m,a):
        d=1
        # se for o último dia do ano
        if m == 12:
            m=1
            a = a+1
        else:
            m = m+1
    else:
        d = d+1
    
    return d,m,a


# Implemente aqui a função adicione_ndias(n, d, m, a).
def adicione_ndias(n, d, m, a):
    tupla = adicione_1dia(d, m, a)
    n-=1
    while n!=0:
        d, m, a = tupla
        tupla = adicione_1dia(d, m, a)
        n -= 1
    return tupla


main()