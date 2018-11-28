#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
sys.path.insert(0, "/home/camilo/Documentos/Proyectos/university-problems-solvers/Functions")

import introduction
import centerText
import findRootEquations

'''
	Main method of the whole app.
'''
def main():
	options = {"Linear algebra":[[2.1, "Matrix determinant", "findDeterminantMatrix"]], "Calculus":[[1.1, "Find roots of functions", "findRootEquations"]], "Dynamics of mechanical systems":[[3.1, "Undamped systems", ""]], "Mechanics of deformable solids":[[4.1, "Deflection of beams", ""]]}

	introduction.show(options)

	listOfAvailableOptions = []
	# Loop that finds all the available options.
	for key, value in options.iteritems():
		for list in value:
			listOfAvailableOptions.append(list[0])

	# Loop that iteratively  executes the chosen option.
	while True:
		# Variable where the picked option/function is stored.
		pickedFunction = ""

		# Loop that makes sure the chosen option exists.
		while True:
			option = introduction.takeOption()

			if option in listOfAvailableOptions:
				# Loop that finds what option/function the user picked.
				for key, value in options.iteritems():
					for list in value:
						if option == list[0]:
							pickedFunction = list[2]

				break
			else:
				print ('*' + centerText.main('Invalid entry!', 0 ) + '*')

		print ("")

		# Executes the option.
		eval(pickedFunction + ".main()")

print ("")

if __name__ == "__main__":
	""" Executes the app """
	main()
