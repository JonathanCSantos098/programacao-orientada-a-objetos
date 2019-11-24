def extensao_mes(dia,mes,ano):
    meses=(0,"Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
    dia=int(dia)
    mes=int(mes)
    ano=int(ano)
    if mes <=12 and mes >=1:
        print ("{} de {} de {}".format(dia,meses[mes],ano))
    else:
        print("NULL")

day,month,year=input().split("/")
extensao_mes(day,month,year)