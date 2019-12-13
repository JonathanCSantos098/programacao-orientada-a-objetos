class Computador():
    def __init__ (self, marca, modelo, componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor

    def mostrarMarca (self):
        print(self.marca)

    def adicionarComponentes (self,novoComp):
        self.componentes.append(novoComp)
 
    def mostrarComponentes (self):
        print(self.componentes)
    
    def mostrar_anos_uso (self):
        if (self.anos_uso < 6):
            print(self.anos_uso)
        elif (self.anos_uso >= 6):
            print("Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...")

    def envelhecer (self):
        self.anos_uso += 1
        
comp = Computador ("Lenovo","Ideapad 145s", ['monitor','mouse','teclado','cabo de força'], 5, "cinza fosco")
comp.mostrarMarca()
comp.mostrar_anos_uso()
comp.adicionarComponentes('SSD')
comp.mostrarComponentes()