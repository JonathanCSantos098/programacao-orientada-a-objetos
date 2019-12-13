class Bola ():
    def __init__ (self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
    
    def trocarCor (self,novaCor):
        self.cor = novaCor

    def mostrarCor (self):
        print(self.cor)

b1 = Bola("vermelha",45,"metal")
b1.trocarCor("rosa")
b1.mostrarCor()