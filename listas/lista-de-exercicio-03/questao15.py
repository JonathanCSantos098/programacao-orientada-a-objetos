a = float(input("Entre com a medida do lado 1 do triangulo: "))
b = float(input("Entre com a medida do lado 2 do triangulo: "))
c = float(input("Entre com a medida do lado 3 do triangulo: "))

if a>=b+c or b>=c+a or c>=a+b :
	print("Triangulo inexistente.")
elif a==b and b==c :
	print("Triangulo equilatero.")
elif a==b or b==c or c==a :
	print("Triangulo isosceles.")
else:
	print("Triangulo escaleno.")

