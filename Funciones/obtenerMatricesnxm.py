#!usr/bin/python
# -*- encoding: utf-8 -*-

'''
Obtiene las dimensiones de las matrices.
'''
def obtenerDimensiones():
	# Se obtiene el número de matrices a ingresar.
	numMatrices = int(raw_input("Número de matrices = "))
	dimensionMatrices = []

	print ("")

	# Loop que ingresa la dimensión de cada matriz a multiplicar.
	i = 0
	while i < numMatrices:
		# try-except en caso que algún valor ingresado sea inválido o erróneo.
		try:
			# Se obtiene la dimensión de cada matriz a ingresar en orden y de tipo "string".
			str_dimension = raw_input("Dimensión de la matriz " + str(i + 1) + " (ejemplo: 3x3): ")

			# Condición en caso que no se haya ingresado una "x".
			if "x" in str_dimension:

				# Se convierten los datos en tipo "int" luego de haber divido la cadena de acuerdo a la "x" que separa los números.
				dimension = [int(x) for x in str_dimension.split("x")]

				# Se añade la lista creada de números a la lista madre de dimensiones.
				dimensionMatrices.append(dimension)
				i += 1
		except:
			print ("Dimensión inválida.")

			return dimensionMatrices

'''
Obtiene las matrices.
'''
def main():
	# Se obtienen las dimensiones de las matrices a ingresar.
	dimensiones = obtenerDimensiones()

	print ("")

	# Loop que itera por las filas de cada matriz a ingresar de acuerdo a su dimensión previamente dada.
	i = 0
	matrices = []
	while i < len(dimensiones):
		print ("Matriz " + str(i + 1) + ":")
		print ("")

		# Loop que itera por las columnas de cada matriz a ingresar de acuerdo a su dimensión previamente dada.
		j = 0
		matrizActual = []
		while j < dimensiones[i][0]:
			str_Fila = raw_input("-> Fila " + str(j + 1) + ": ")

			# Condición, en caso que el número de valores ingresados no coincida con la dimensión previamente dada.
			if dimensiones[i][1] != len(str_Fila.split(" ")):
				print ("El número de valores ingresados no coincide con la dimensión de la matriz " + str(i + 1) + ".")
			else:

				# Se convierten los datos de tipo "string" en "int".
				fila = [float(x) for x in str_Fila.split(" ")]

				# Se añade la fila a la matriz actual por la cual se itera.
				matrizActual.append(fila)
				j += 1

				# Se añade la matriz previamente creada a la lista de matrices ingresadas.
				matrices.append(matrizActual)
				i += 1
			print ("")

	return matrices
