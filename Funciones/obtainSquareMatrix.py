#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
    Obtains a matrix given by the user.
'''
def main():
    # try-except in case an entered value is invalid.
    try:
        n = int(raw_input("Dimension (example: 2 -> Gives a 2x2 matrix) = "))
        print ("")
        print ("Matrix " + str(n) + "x" + str(n) + ":")

        # Loop that creates the rows of the matrix as a list.
        i = 0
        matrix = []

        while i < n:
            str_presentRow = []

            str_row = raw_input("-> row " + str(i + 1) + ": ")

            str_presentRow = str_row.split(" ")

            presentRow = [float(x) for x in str_presentRow]

            if len(presentRow) == n:
                matrix.append(presentRow)
                i += 1
            else:
                print ("The number of given values is different from the matrix dimension!")

            return matriz
    except:
        print ("")
        print ("Invalid entry!")
