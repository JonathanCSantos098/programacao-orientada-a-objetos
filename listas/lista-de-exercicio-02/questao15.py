valor_hora=float(input("Informe o valor da hora: "))
horas_mes=int(input("Informe a quantidade de horas trabalhadas: "))

salario=valor_hora*horas_mes

imposto=(salario*11)/100
inss=(salario*8)/100
sindicato=(salario*5)/100

desconto=imposto+inss+sindicato
salario_liquido=salario-desconto

print(salario,"\n",imposto,"\n",inss,"\n",sindicato,"\n",salario_liquido)
