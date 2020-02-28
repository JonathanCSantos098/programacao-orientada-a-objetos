from datetime import datetime #importação da biblioteca datetime

class Pessoa: #criando a classe pessoa
    def __init__(self, nome, idade): #definindo seus atributos
        self.nome = nome
        self.idade = idade

    def __str__(self): #criando o str(processo de impressão)
        print (f'- {self.nome} / {self.idade} anos')

class Vendedor(Pessoa): #criando a classe vendedor
    def __init__(self, nome, idade, salario): #definindo seus atributos
        self.nome = nome
        self.idade = idade
        self.salario = salario

class Cliente(Pessoa): #criando a classe cliente
    def __init__(self, nome, idade, **kwargs): #definindo seus atributos
        self.nome = nome
        self.idade = idade
        self.compras = []
        self.data = datetime.today()

    def registrar_compra(self, compra): #criando o metodo que adiciona as compras em uma lista vazia
        return self.compras.append(compra)

    def get_data_ultima_compra(self): #criando o metodo que retorna a data da ultima compra
        print (self.data)

    def total_compras(self): #criando o metodo que retorna o total de compras realizadas
        print(self.compras)
        return print(len(self.compras), "Compras Realizadas")

class Compra: #criando a classe compra
    def __init__(self, vendedor, data, valor): #definindo seus atributos
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

        
#testando as classes e seus metodos

pessoa1 = Pessoa("Jonathan", 19) #criando uma pessoa
funcionario = Vendedor(pessoa1.nome, pessoa1.idade, 1500) #criando um vendedor que recebe os atributos da primeira pessoa
pessoa1.__str__() #imprimindo seus dados

pessoa2 = Pessoa("José", 46) #criando uma segunda pessoa
cliente = Cliente(pessoa2.nome, pessoa2.idade) #criando um cliente que recebe os atributos da segunda pessoa
cliente.__str__() #imprimindo seus dados

compra = Compra(pessoa1,"",10.0) #criando uma compra
cliente.registrar_compra("Arroz")
cliente.registrar_compra("Carne Moída")
cliente.total_compras() #retornando o total de compras realizadas

cliente.get_data_ultima_compra() #retornando a hora da última compra