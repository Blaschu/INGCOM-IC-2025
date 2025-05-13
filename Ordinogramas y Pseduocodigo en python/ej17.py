if __name__ == '__main__':
	# 17.	Leer un número y contar sus dígitos
	numero = int()
	contador = int()
	print("Introduce un número:")
	numero = int(input())
	if numero<0:
		numero = abs(numero)
	contador = 0
	while numero>=1:
		numero = int(numero/10)
		contador = contador+1
	print("El número de dígitos es: ",contador)