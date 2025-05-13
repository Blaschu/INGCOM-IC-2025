if __name__ == '__main__':
	print("Seleccionar tipo de operacion")
	print("1)Suma, 2)Resta, 3)Producto, 4)Division, 5)Salir")
	opcion = input()
	if opcion==1:
		print("Seleccionaste Sumar")
		print("introduce valores a sumar")
		num1 = float(input())
		num2 = float(input())
		res = num1+num2
		print("el resultado de la suma es: ",res)
	else:
		print("Seleccionar tipo de operacion")
		opcion = float(input())
	if opcion==2:
		print("Seleccionaste Restar")
		print("introduce valores a Restar")
		num1 = float(input())
		num2 = float(input())
		res = num1-num2
		print("el resultado de la resta es: ",res)
	else:
		print("Seleccionar tipo de operacion")
		opcion = float(input())
	if opcion==3:
		print("Seleccionaste Producto")
		print("introduce valores a multiplicar")
		num1 = float(input())
		num2 = float(input())
		res = num1*num2
		print("el resultado de la nmultiplicacion es: ",res)
	else:
		print("Seleccionar tipo de operacion")
		opcion = float(input())
	if opcion==4:
		print("Seleccionaste Dividir")
		print("introduce valores a dividir")
		num1 = float(input())
		num2 = float(input())
		res = num1/num2
		print("el resultado de la division es: ",res)
	else:
		print("Seleccionar tipo de operacion")
		opcion = float(input())
	if opcion==5:
		print("Seleccionaste Salir")
		print("introduce valores a sumar")
	else:
		print("Seleccionar tipo de operacion")
		opcion = float(input())

