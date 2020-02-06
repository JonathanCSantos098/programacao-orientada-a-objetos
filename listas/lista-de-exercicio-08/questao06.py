class Retangulo():
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor_lado (self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_valor_lado (self):
        return self.base and self.altura
    
    def calcular_area (self):
        return self.base * self.altura

    def calcular_perimetro (self):
        return self.base * 2 + self.altura * 2
        


bas = float (input("Informe um valor: "))
alt = float (input("Informe outro valor: "))
ret = Retangulo(bas,alt)
ret.calcular_area()
ret.calcular_perimetro()
ret.mudar_valor_lado(4, 5)
ret.calcular_area()
ret.calcular_perimetro()