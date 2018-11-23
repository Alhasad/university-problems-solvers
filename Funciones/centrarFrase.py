#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import darAnchoDeConsola

'''
	Centra la cadena de texto dada por parámetro, con opción de offset.
'''
def main(cadena, offset):
    anchoDeConsola = darAnchoDeConsola.main()
    return (' ' * int(str((anchoDeConsola - len(cadena))//2)) + cadena + ' ' * int(str((anchoDeConsola - len(cadena))//2)))
