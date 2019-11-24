def linha(num):
    lista=[]
    while n not in lista:
        for x in range (1,num+1):
            lista.append(x)
            retirada=str(lista).strip("[]").replace(","," ")
            print(retirada)



n=int(input())
numero=linha(n)
