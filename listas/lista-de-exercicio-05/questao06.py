def conversao_hora(horas,minutos):
    
    if (horas > 11):
        tempo=horas-12
        return tempo

horas=int(input())
minutos=int(input())
atribui=conversao_hora(horas,minutos)

def horario(atribui,horas):
    if (horas <= 11 ):
        print ("{}:{} A.M".format(horas,minutos))
    else:
        print ("{}:{} P.M".format(atribui,minutos))

atribuicao=horario(atribui,horas)


while True:
    continuar=str(input("Deseja continuar? (S/N)"))
    if continuar in "Nn":
        break
    horas=int(input())
    minutos=int(input())
    x=conversao_hora(horas,minutos)
    y=horario(x,minutos)
    