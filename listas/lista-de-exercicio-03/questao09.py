num1=float(input())
num2=float(input())
num3=float(input())

if (num1>num2>num3):
    print("{:.0f} {:.0f} {:.0f}".format(num1,num2,num3))
elif (num1>num3>num2):
    print("{:.0f} {:.0f} {:.0f}".format(num1,num3,num2))
elif (num2>num1>num3):
    print("{:.0f} {:.0f} {:.0f}".format(num2,num1,num3))
elif (num2>num3>num1):
    print("{:.0f} {:.0f} {:.0f}".format(num2,num3,num1))
elif (num3>num1>num2):
    print("{:.0f} {:.0f} {:.0f}".format(num3,num1,num2))
elif (num3>num2>num1):
    print("{:.0f} {:.0f} {:.0f}".format(num3,num2,num1))
