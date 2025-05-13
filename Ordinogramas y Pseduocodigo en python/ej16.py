
if __name__ == '__main__':
	# Declaración de variables
	numero1 = int()
	numero2 = int()
	# Solicitar los números al usuario
	print("Ingrese el primer número:")
	numero1 = int(input())
	print("Ingrese el segundo número:")
	numero2 = int(input())
	# Verificar divisibilidad
	if numero2!=0:
		if numero1%numero2==0:
			print(numero1," es divisible por ",numero2)
		else:
			print(numero1," no es divisible por ",numero2)
	else:
		print("El segundo número no puede ser cero.")

