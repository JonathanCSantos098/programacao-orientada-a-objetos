class Pessoa():
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer (self):
        self.idade += 1
        return print (self.idade)

    def engordar (self, aumento):
        self.peso += aumento
        return print (self.peso)

    def emagrecer (self,perda):
        self.peso -= perda
        return print (self.peso)
    
    def crescer (self):
        if self.idade < 21:
            self.altura += 0.5
            return print (self.altura)
        else:
            return print (self.altura)

pes = Pessoa ("Carlos", 34, 70.6, 180)
pes.envelhecer()
pes.engordar(0.7)
pes.emagrecer(1.8)
pes.crescer