#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Main method of the whole app.
'''
import sys
from os import system, name
sys.path.insert(0, "/home/camilo/Documentos/Proyectos/university-problems-solvers/Functions")

import introduction
import centerText
import findRootEquations
import findDeterminantMatrix
import multiplyMatrices
import writeVariable

def clear():
	""" Clear function to make the app more user friendly """
	if name == 'nt':
		_ = system('cls') # For windows.
	else:
		_ = system('clear') # For mac and linux (here, os.name is 'posix').

def main():
	""" Main method """

	options = {"Linear algebra":
	[[2.1, "Matrix determinant", "findDeterminantMatrix"],
	 [2.2, "Multiply matrices", "multiplyMatrices"]],
	"Calculus":
	[[1.1, "Find roots of functions", "findRootEquations"]],
	"Dynamics of mechanical systems":
	[[3.1, "Undamped systems", ""]],
	"Mechanics of deformable solids":
	[[4.1, "Deflection of beams", ""]],
	"Aditional options":
	[[5.1, "Quit", "exit"]]}

	listOfAvailableOptions = []
	# Loop that finds all the available options.
	for value in options.itervalues():
		for list in value:
			listOfAvailableOptions.append(list[0])

	# Loop that iteratively  executes the chosen option.
	while True:
		introduction.show(options)

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

		# Checks if the picked option is actually 'quit'.
		if pickedFunction == "exit":
			tmp = writeVariable.uncheckVariablesFile()
			sys.exit()

		# Executes the option.
		eval(pickedFunction + ".main()")

		print ("")
		tmp = raw_input("Press any key to continue...")
		clear()

print ("")

if __name__ == "__main__":
	""" Executes the app """
	main()
