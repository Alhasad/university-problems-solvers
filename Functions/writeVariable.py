#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Writes a given Variable-type object to a file.
'''
from variableClass import Variable
import fileinput

def alreadyHaveVariables():
    """ Tests if a 'Variables' file already exists and has variables stored """
    file = open("Variables", "r")
    line = file.readline()
    file.close()
    print(line)
    if line == "" or line == "checked":
        return False
    else:
        return True

def uncheckVariablesFile():
    """ Changes the first line of a file to 'unchecked' """
    try:
        with open("Variables") as file:
            lines = file.readlines()

        lines[0] = "unchecked\n" # Replace.

        with open("Variables", "w") as file:
            file.writelines(lines)

    except FileNotFoundError:
        return -1

def main( newVariable ):
    """ Main method """
    answer = "y"
    if alreadyHaveVariables():
        # Loop that ensures the entries are valid.
        while True:
            print("There are already variables stored from a previous session.")
            answer = raw_input("Do you want to start a new variables set? [y/n] ")
            if answer == "y" or answer == "n":
                break
            else:
                print("Invalid entry!")

    # A file from a previous session will have a 'unchecked' in the first line.
    # If the user wants a new set of variables, this will delete the existing file and open a new one.
    # If the user wants to use the existing set of variables, this will change the 'unchecked' to 'checked'.
    if answer == "y":
        file = open("Variables", "w")
        file.write("checked\n")
    else:
        with open("Variables") as file:
            lines = file.readlines()

        lines[0] = "checked\n" # Replace.

        with open("Variables", "w") as file:
            file.writelines(lines)

        file.open("Variables", "a")

    file.write( str(newVariable.giveName()) + "\n" )
    file.write( str(newVariable.giveValue()) + "\n" )
    file.write( str(newVariable.giveType()) + "\n" )
    file.write("*\n")
    file.close()
