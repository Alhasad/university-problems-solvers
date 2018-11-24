#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import giveConsoleWidth

'''
	Shows available options/modes.
'''
def showOptions():
	options = {"Linear algebra":["Matrix determinant"], "Calculus":["Find roots of functions"], "Dynamics of mechanical systems":["Undamped systems"], "Mechanics of deformable solids":["Deflection of beams"]}
	cont = 1

	# Loop para mostrar las opciones.
	for key, value in options.items():
		cont2 = cont + 0.1
		for option in value:
			print( str(cont) + ". " + key + ".")
			print('\t' + str(cont2) + " " + option + ".")
			cont2 += 0.1
		cont += 1

'''
	Shows complete introduction of the program.
'''
def show():
    title = 'University tools and solvers, by Camilo Martínez'
    consoleWidth = giveConsoleWidth.main()

    print ('~' * consoleWidth)
    print (' ' * int(str((consoleWidth - len(title))//2)) + title + ' ' * int(str((consoleWidth - len(title))//2)))
    print ('~' * consoleWidth)
    print ('')
    showOptions()
    print ('')

'''
	Algorithm that takes the option of the user.
'''
def takeOption():
    consoleWidth = giveConsoleWidth.main()

    print ('~' * consoleWidth)
    option = float(input("Option: "))
    return option
