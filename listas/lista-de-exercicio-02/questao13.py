def peso(a,b):
    if (a=="homem"):
        peso_ideal=(72.7*b)-58
        print(peso_ideal)
    elif (a=="mulher"):
        peso_ideal=(62.1*b)-44.7
        print(peso_ideal)
a=str(input("Informe o sexo: "))
b=float(input("Infora a altura: "))

peso (a,b)
