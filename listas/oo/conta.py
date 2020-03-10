import datetime #importando a biblioteca de hora

class Cliente: #criando classe cliente
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print("Data de abertura da conta: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)

class Conta(Historico):
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print ("Inicializando uma conta")
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
        if (self.saldo <= 0):
            print("Saldo insuficiente")
        else:
            return self.saldo

    def extrato(self):
        print("Conta: {} \n Saldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))
    
    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia de {} para conta {}".format(valor, destino.numero))
            return True
            