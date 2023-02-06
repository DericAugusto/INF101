# p08.py
# Nome:
# Matrícula:
# Data: 25/03/2021
# Atualização: 25/03/2021
# (Descreva sucintamente o que o programa faz.)

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



# Implemente aqui a função num_dias_no_mes(m, a).



# Implemente aqui a função adicione_1dia(d, m, a).



# Implemente aqui a função adicione_ndias(n, d, m, a).




main()

