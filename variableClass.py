#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Class that manages a single variable.
'''
class Variable:
    def __init__(self, value, name, type):
        self.value = value
        self.name = name
        self.type = type

    def giveValue(self):
        return self.value

    def giveName(self):
        return self.name

    def giveType(self):
        return self.type
