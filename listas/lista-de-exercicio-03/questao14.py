nota1=float(input())
nota2=float(input())
conceito=str
media=(nota1+nota2)/2
if(media>=9 and media<=10):
    conceito="A"
elif(media>=7.5 and media<=9):
    conceito="B"
elif(media>=6 and media<=7.5):
    conceito="C"
elif(media>=4 and media<=6):
    conceito="D"
elif(media>=0 and media<=4):
    conceito="E"
    
print("Notas: \n",nota1,"\n",nota2)
print("Média: \n",media)
print("Conceito: \n",conceito)

if(conceito=="A" or conceito=="B" or conceito=="C"):
    print("APROVADO")
elif(conceito=="D" or conceito=="E"):
    print("REPROVADO")
