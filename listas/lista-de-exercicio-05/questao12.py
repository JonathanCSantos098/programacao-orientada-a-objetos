import random
def mistura(palavra):
    embaralha=list(palavra)
    random.shuffle(embaralha)
    embaralha="".join(embaralha)

    embaralha="".join(random.sample(palavra,len(palavra)))
    print (embaralha)

y=str(input())
x=mistura(y)