def byte (num):
    result = num / 1024 / 1024
    return result

def porcent (mega_byte, soma):
    result = (100 * mega_byte) / 2581.56
    return result

def main (arq):
    soma = 0
    leitura = []
    num_usuario = 1
    
    with open (arq) as dados:

        with open ('relatorio.txt', 'w') as write:

            print ('ACME Inc.        Uso do espaço em disco pelos usuários', file = write)
            print ('--------------------------------------------------------', file = write)
            print ('{:<3}   {:<10}   {:<17}     {:<9}'.format('Nr.', 'Usuário', 'Espaço utilizado', '% do uso'), file = write)

            for linha in dados:
                linha = linha.strip('  ').split()
                mega = byte(int(linha[1]))
                leitura.append(mega)
                print('{:<3}   {:<10}    {:>10.2f} MB      {:>9.2f}%'.format(num_usuario, linha[0], mega, porcent (mega, soma)), file =  write)
                num_usuario += 1
                soma += mega

            print (' ', file = write)
            print ('Espaço total ocupado: {:.2f} MB'.format(soma), file = write)  
            print ('Espaço médio ocupado: {:.2f} MB'.format(soma/num_usuario), file = write)

main ('usuarios.txt')