def somaimposto(taxaimposto,custo):
    percentagem=taxaimposto/100
    custo_total=custo+(percentagem*custo)
    return custo_total
    
imposto=int(input("Porcentagem: "))
custo_produto=float(input("Custo do produto: "))
print(somaimposto(imposto,custo_produto))
