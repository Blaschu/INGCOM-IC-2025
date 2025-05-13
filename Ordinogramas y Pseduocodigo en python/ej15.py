if __name__ == '__main__':
	# Declaración de variables
	suma = float()
	promedio = float()
	contador = int()
	cantidad = int()
	# Inicialización de variables
	suma = 0
	contador = 0
	# Solicitar la cantidad de números a ingresar
	print("Ingrese la cantidad de números:")
	cantidad = int(input())
	# Bucle para ingresar los números y calcular la suma
	while contador<cantidad:
		numero = float()
		print("Ingrese un número:")
		numero = float(input())
		suma = suma+numero
		contador = contador+1
	# Calcular el promedio
	promedio = suma/cantidad
	# Mostrar el resultado
	print("El promedio es:",promedio)