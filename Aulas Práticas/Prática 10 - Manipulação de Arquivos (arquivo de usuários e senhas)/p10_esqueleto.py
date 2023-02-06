# p10.py
# Programador:
# Matrícula:
# Criado em: 15/04/2021
# Atualizado em: 15/04/2021
# (escreva aqui um breve comentário sobre o que o programa faz)

arqNome = 'passwords.txt' # nome externo do arquivo de senhas (em texto claro)

def main():
    print('Início do processamento do arquivo de senhas \'{}\'.'.
          format(arqNome))
    login_name = input('\nLogin name: ')
    while len(login_name) > 0:
        senha = input('Password: ')
        encSenha = pesquise(login_name)
        if encSenha != '\0':
            print('O usuário \'{}\' '.format(login_name), end='')
            if not autenticado(senha, encSenha):
                print('NÃO ', end='')
            print('foi autenticado pelo sistema.')
        else:
            print('O usuário \'{}\' não existe. Está sendo criado...'.
                  format(login_name))
            insira(login_name, senha)
        login_name = input('\nLogin name: ')
    print('\nFim do processamento do arquivo de senhas.')


def autenticado(s, es):
    return s == es


# A função pesquise retorna a senha em texto claro associada a nome.
# Se nome não for encontrado no arquivo de senhas, ela retorna o
# caractere nulo.
###                                                               ###
# IMPLEMENTE AQUI A SUA FUNÇÃO pesquise(nome).                      #
###                                                               ###






# Insere, no final do arquivo texto de senhas, o par login, senha.
def insira(nome, senha):
    try:
        arq = open(arqNome, 'a')
        arq.write('{}\t{}\n'.format(nome, senha))
        arq.close()
    except OSError:
        print('***Erro: o arquivo \'{}\' não existe.'.format(arqNome))


if __name__ == '__main__':
    main()
