#!usr/bin/env python

'Helpful string functions and variables'

from random import randint, choice

lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specials = '`~!@#$%^&*()-_=+[]{}|\\;:"\'<>?/.,'
alphas = uppers + lowers
alphanums = alphas + digits
keychars = alphanums + specials
whitespace = ' \n\r\t\f\v'
asciis = ''.join([chr(char) for char in range(256)])

def split(string, char='', /):
    "Equivalent to list(string) if char == '';\nElse string.split(char)"
    return list(string) if char == '' else string.split(char)

def join(iterable, joiner='', /):
    "Equivalent to joiner.join(iterable); concatenates any number of iterables\nMeant for strings"
    return joiner.join(iterable)

def strGen(lines=1, maxchars=79, charset=keychars):
    'Generates a random string'
    allLines = []
    for line in range(lines):
        string = []
        for char in range(randint(1, maxchars)):
            string.append(choice(charset))
        allLines.append(join(string))
    return '\n'.join(allLines)
