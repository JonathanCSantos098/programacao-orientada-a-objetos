class Tamagotchi ():
    def __init__ (self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print ("Novo Nome: ", self.nome)

    def retornar_fome (self):
        return print ("Fome: ",self.fome)

    def retornar_saude (self):
        return print ("Saude: ", self.saude)

    def retornar_idade (self):
        return print ("Idade: ", self.idade)

    def comer (self):
        self.fome += 1
        if self.fome == 20:
            print ("Barriga cheia")

    def tomar_injecao (self):
        self.saude += 1
        if self.saude == 20:
            print ("Saudavel")

    def envelhecer (self):
        self.saude -= 1
        self.idade += 1
        if self.saude == 0:
            print ("morreu")

    
bicho = Tamagotchi ("Rex", 10, 10, 0)
bicho.alterar_nome("Ativimquibal")
bicho.retornar_fome()
bicho.retornar_saude()
bicho.retornar_idade()
bicho.comer()
bicho.tomar_injecao()
bicho.envelhecer()
