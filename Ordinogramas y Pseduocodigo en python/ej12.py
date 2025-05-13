if __name__ == '__main__':
	fibonacci = int()
	numero1 = int()
	numero2 = int()
	contador = int()
	numero1 = 0
	numero2 = 1
	print("Los primeros 10 números de la serie Fibonacci son: ")
	print(numero1)
	print(numero2)
	for contador in range(3,11):
		fibonacci = numero1+numero2
		print(fibonacci)
		numero1 = numero2
		numero2 = fibonacci

