class Caneta ():
    def __init__ (self,cor, marca, numero_ponta, volume_tinta):
        self.cor = cor
        self.marca = marca
        self.numero_ponta = numero_ponta
        self.volume_tinta = volume_tinta

    def volume_caneta (self):
        print (self.volume_tinta)

    def escrever (self,palavra):
        print(palavra)
        self.volume_tinta -= 1

    def retornar_marca (self):
        return self.marca
    
    def encher_caneta (self):
        self.volume_tinta = 50
        print(self.volume_tinta)

    #def imprimir_caracteristicas (self):

caneta = Caneta('azul','BIC', 2, 50)
caneta.escrever('Candeias')
caneta.volume_caneta()
caneta.encher_caneta()