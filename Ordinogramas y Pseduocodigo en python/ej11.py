if __name__ == '__main__':
	numero1 = float()
	numero2 = float()
	numero3 = float()
	menor = float()
	medio = float()
	mayor = float()
	print("Introduce el primer número: ")
	numero1 = float(input())
	print("Introduce el segundo número: ")
	numero2 = float(input())
	print("Introduce el tercer número: ")
	numero3 = float(input())
	# Comparamos y ordenamos
	if numero1<numero2 and numero1<numero3:
		menor = numero1
		if numero2<numero3:
			medio = numero2
			mayor = numero3
		else:
			medio = numero3
			mayor = numero2
	else:
		if numero2<numero1 and numero2<numero3:
			menor = numero2
			if numero1<numero3:
				medio = numero1
				mayor = numero3
			else:
				medio = numero3
				mayor = numero1
		else:
			menor = numero3
			if numero1<numero2:
				medio = numero1
				mayor = numero2
			else:
				medio = numero2
				mayor = numero1
	print("Los números ordenados de menor a mayor son: ",menor,", ",medio,", ",mayor)
