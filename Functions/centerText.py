#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Centers the string, with an offset option.
'''
import giveConsoleWidth

def main(text, offset):
	""" Main method """
	consoleWidth = giveConsoleWidth.main()
	return (' ' * int(str((consoleWidth - len(cadena))//2)) + cadena + ' ' * int(str((consoleWidth - len(cadena))//2)))
