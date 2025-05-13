if __name__ == '__main__':
	totalestudiantes = int()
	notaaprobacion = float()
	notaestudiante = float()
	aprobados = int()
	porcentajeaprobados = float()
	aprobados = 0
	print("Introduce el número total de estudiantes: ")
	totalestudiantes = int(input())
	print("Introduce la nota de aprobación: ")
	notaaprobacion = float(input())
	for i in range(1,totalestudiantes+1):
		print("Introduce la nota del estudiante ",i,": ")
		notaestudiante = float(input())
		if notaestudiante>=notaaprobacion:
			aprobados = aprobados+1
	porcentajeaprobados = (aprobados/totalestudiantes)*100
	print("El porcentaje de aprobados en el grupo es: ",porcentajeaprobados,"%")
