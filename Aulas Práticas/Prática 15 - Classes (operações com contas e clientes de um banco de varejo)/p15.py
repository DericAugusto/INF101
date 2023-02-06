# Nome: Déric Augusto França de Sales
# Matrícula: 96718
# Data: 20/05/2021

# Descrição do programa:
'''
O programa abaixo exemplifica operações de um banco de varejo, usando a
definição de classes em sua estrutura. Há duas classes sendo utilizadas,
uma para representar os clientes do banco e outra para representar as 
contas correntes dos clientes. Na função main() temos um exemplo de 
operações que podem ser realizadas.
'''

class Cliente():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta():
    def __init__(self, clientes, numero, saldo=0.00):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0.0
        self.operacoes = []

        self.deposito(saldo)

    def resumo(self):
        aux = ''
        for cliente in self.clientes:
            aux = aux + cliente.nome + ', '
        
        print('\nCc nº {:s} de {}\n'\
            '\tSaldo: {:10.2f}'.format(self.numero, aux ,self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(('SAQUE', valor))
        else:
            print('Cc nº {} com saldo insuficiente; SAQUE NÃO REALIZADO'.\
            format(self.numero))

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(('DEPÓSITO', valor))
    
    def extrato(self):
        print("\n\nExtrato da CC nº {:s}\n".format(self.numero))
        for op in self.operacoes:
            print("{:10s} {:10.2f}".format(op[0], op[1]))
        print("\n SALDO {:10.2f}".format(self.saldo))


def main():
    cliente1 = Cliente("João Silva", "3234-7890")
    cliente2 = Cliente("Maria Silva", "3234-7890")
    cliente3 = Cliente("José Vargas", "2567-0987")

    conta1 = Conta([cliente1, cliente2], "76534", 1000.00)
    conta2 = Conta([cliente3], "80297", 500.00)

    conta1.saque(50.00)
    conta2.deposito(300.00)
    conta1.saque(190.00)
    conta2.deposito(95.15)
    conta2.saque(256.71)

    conta1.resumo()
    conta2.resumo()

    conta1.extrato()
    conta2.extrato()

main()