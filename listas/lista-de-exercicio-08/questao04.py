class Caneta ():
    def  __init__ ( self , cor , marca , numero_ponta , volume_tinta ):
        self .cor = cor
        self .marca = marca
        self .numero_ponta = numero_ponta
        self .volume_tinta = volume_tinta

    def  volume_caneta ( self ):
        print (f'Volume da caneta após escrita {self .volume_tinta}')

    def  escrever ( self , palavra ):
        print (palavra)
        self .volume_tinta -= 1

    def  retornar_marca ( self ):
        return  self .marca
    
    def  encher_caneta ( self ):
        self .volume_tinta =  50
        print (f'Volume da caneta {self .volume_tinta}')

    def imprimir_caracteristicas (self):
        print(f'cor: {self.cor} marca: {self.marca} Nº da ponta: {self.numero_ponta} Volume: {self.volume_tinta}')

caneta = Caneta ( ' azul ' , ' BIC ' , 2 , 50 )
caneta.escrever ( 'Candeias ' )
caneta.volume_caneta ()
caneta.encher_caneta ()
caneta.imprimir_caracteristicas()
