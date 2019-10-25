salario=float(input("Informe o slário: "))

if(salario<=280):
    aumento=(salario*20)/100
    novo_salario=salario+aumento
    print("Salário: ",salario)
    print("Percentual de aumento foi de 20%")
    print("Aumento de R$ ",aumento)
    print("Novo Salaŕio: ",novo_salario)
elif(salario>280 and salario<700):
    aumento=(salario*15)/100
    novo_salario=salario+aumento
    print("Salário: ",salario)
    print("Percentual de aumento foi de 15%")
    print("Aumento de R$ ",aumento)
    print("Novo Salaŕio: ",novo_salario)
elif(salario>700 and salario<1500):
    aumento=(salario*10)/100
    novo_salario=salario+aumento
    print("Salário: ",salario)
    print("Percentual de aumento foi de 10%")
    print("Aumento de R$ ",aumento)
    print("Novo Salaŕio: ",novo_salario)
elif(salario>1500):
    aumento=(salario*5)/100
    novo_salario=salario+aumento
    print("Salário: ",salario)
    print("Percentual de aumento foi de 5%")
    print("Aumento de R$ ",aumento)
    print("Novo Salaŕio: ",novo_salario)
