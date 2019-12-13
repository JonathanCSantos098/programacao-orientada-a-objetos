class Quadrado():
    def __init__ (self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado (self,novoValor):
        self.tamanho_lado = novoValor

    def retornar_valor_dado (self):
        return self.tamanho_lado


    def calcular_area (self):
        area=self.tamanho_lado * self.tamanho_lado

lado = Quadrado(10)
lado.calcular_area()