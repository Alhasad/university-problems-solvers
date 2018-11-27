#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("E:/Aplicaciones/Proyectos/University-problems-solvers/Funciones"))

import introduction
import centerText
import findRootEquations

'''
	Main method of the whole app.
'''
def main():
	options = {"Linear algebra":
	[[1.1, "Matrix determinant", "findDeterminantMatrix"]],
	"Calculus":
	[[2.1, "Find roots of functions", "findRootEquations"]],
	"Dynamics of mechanical systems":
	[[3.1, "Undamped systems", ""]],
	"Mechanics of deformable solids":
	[[4.1, "Deflection of beams", ""]]}

	introduction.show(options)

	# Loop that iteratively  executes the chosen option.
	while True:
		# Loop that makes sure the chosen option exists.
		while True:
			option = introduction.takeOption()

			if option == 1.1:
				break
			else:
				print ('*' + centerText.main('Invalid entry!', 0 ) + '*')

		print ("")

		# Condiciones para la ejecución de las optiones.
		if option == 1.1:
			findRootEquations.main()
		elif option == 100:
			exit()

print ("")

if __name__ == "__main__":
	""" Executes the app """
	main()
