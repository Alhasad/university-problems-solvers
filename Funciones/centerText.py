#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import giveConsoleWidth

'''
	Centers the string, with an offset option.
'''
def main(text, offset):
    consoleWidth = giveConsoleWidth.main()
    return (' ' * int(str((consoleWidth - len(cadena))//2)) + cadena + ' ' * int(str((consoleWidth - len(cadena))//2)))
