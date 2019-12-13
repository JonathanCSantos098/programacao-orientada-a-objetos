Por padrão, o atributo ataques é uma lista vazia. Com o método adicionar_ataque você deve ser
capaz de adicionar um novo ataque à lista ataques. O método subir_nivel incrementa o atributo nível e o poder_luta.
O atributo e_brilhante deve ser um boolean que vai indicar se o Pokémon é brilhante ou não.
class Pokemon():
    def __init__ (self, nome, tipo, descricao, ataques, nivel, poder_luta):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        #self.brilhante = brilhante

    def mostrar_ataques (self):
        print(self.ataques)

    def subir_nivel (self):
        self.nivel += 1
        self.poder_luta += 100

    def mostrar_poder_luta (self):
        print(self.poder_luta)

    #def e_brilhante (self):

    def adicionar_ataque (self,atk):
        self.ataques.append(atk)

    def mostrarNome (self):
        print(self.nome)


poke = Pokemon ("Entei","Fogo","Cão Lendário dificilmente de ser encrontrado",[],1,1)
poke.mostrarNome()
poke.mostrar_poder_luta()
poke.adicionar_ataque('bola de fogo')
poke.mostrar_ataques()