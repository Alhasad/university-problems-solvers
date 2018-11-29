#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Shows complete introduction of the program.
'''
import giveConsoleWidth

def show(options):
	""" Shows the available options of the program """
	title = "University tools and solvers, by Camilo Martínez"
	consoleWidth = giveConsoleWidth.main()

	print ('~' * consoleWidth)
	print (' ' * int(str((consoleWidth - len(title))//2)) + title + ' ' * int(str((consoleWidth - len(title))//2)))
	print ('~' * consoleWidth)
	print ('')
	cont = 1

	for key, value in options.iteritems():
		print( str(cont) + ". " + key + ".")
		for list in value:
			print('\t' + str(list[0]) + ". " + list[1] + ".")

		cont += 1

	print ("")

def takeOption():
	""" Algorithm that takes the option of the user """
	consoleWidth = giveConsoleWidth.main()

	print ('~' * consoleWidth)
	option = float(input("Option: "))
	return option
