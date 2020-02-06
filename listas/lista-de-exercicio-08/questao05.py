class Pokemon():
    def __init__ (self, nome, tipo, descricao, ataques, nivel, poder_luta, brilhante):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante

    def mostrar_ataques (self):
        print(self.ataques)

    def subir_nivel (self):
        self.nivel += 1
        self.poder_luta += 100

    def mostrar_poder_luta (self):
        print(self.poder_luta)

    def e_brilhante (self):
        print (self.brilhante)

    def adicionar_ataque (self,atk):
        self.ataques.append(atk)

    def mostrarNome (self):
        print(self.nome)


poke = Pokemon ("Entei","Fogo","Cão Lendário dificilmente de ser encrontrado",[],1,1,True)
poke.mostrarNome()
poke.mostrar_poder_luta()
poke.adicionar_ataque('bola de fogo')
poke.mostrar_ataques()