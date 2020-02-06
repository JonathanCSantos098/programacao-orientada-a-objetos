class Macaco ():
    def __init__ (self, nome, bucho=[]):
        self.nome = nome
        self.bucho = []
    
    def comer (self,alimentos):
        self.bucho.append(alimentos)
        return self.bucho
    
    def ver_bucho (self):
        return print (self.bucho)

    def digerir (self):
        self.bucho.remove(self.bucho[0])
        return self.bucho

mac1 = Macaco ("Zé")
mac1.comer("banana")
mac1.comer("abacaxi")
mac1.comer("lixia")
mac1.digerir()
mac1.ver_bucho()

mac2 = Macaco ("Zé")
mac2.comer("cogumelo")
mac2.comer("cenoura")
mac2.comer(mac1)
mac2.digerir()
mac2.ver_bucho()