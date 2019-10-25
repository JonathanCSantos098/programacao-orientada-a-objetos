quant_peso=float(input("Infomre o peso: "))
if (quant_peso>50):
    excesso=quant_peso-50
    multa=excesso*4
    print("Excesso de peso foi de {:.2f} Kg e multa de R${:.2f}".format(excesso,multa))
else:
    print("Esta dentro do limite!")

