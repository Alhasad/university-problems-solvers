#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Muestra la matriz.
'''
def main(matriz):
	numeroMayorDigitos = 0
	i = 0

	# Obtiene el número mayor de dígitos.
	for fila in matriz:
		while i < len(fila):
			correccionNegativa = 0

			# Corrección del número de dígitos en caso que el valor iterado sea negativo.
			if fila[i] < 0:
				correccionNgativa = 1

			# Número de digitos del valor iterado.
			digitos = len(str(abs(fila[i] + correccionNegativa)))

			# Comprueba que en realidad sea el mayor.
			if digitos > numeroMayorDigitos:
				numeroMayorDigitos = digitos

			i += 1

			print ("")

	# Muestra la matriz.
	for fila in matriz:
		print ('%s' % (' '.join('%0*s' % (numeroMayorDigitos, i) for i in fila)))
