prod1=float(input("Qual o valor do produto 1? "))
prod2=float(input("Qual o valor do produto 2? "))
prod3=float(input("Qual o valor do produto 3? "))

valores=[prod1,prod2,prod3]
escolha=min(valores)
print("Escolha o produto que custa: {}".format(escolha))

