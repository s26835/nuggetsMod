#/usr/bin/env python

'String manipulation'

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

def join(iterable, /):
    "Equivalent to ''.join(iterable); concatenates any number of strings"
    return ''.join(iterable)

def strGen(lines=1, maxchars=79, charset=keychars):
    'Generates a random string'
    allLines = []
    for line in range(lines):
        string = []
        for char in range(randint(1, maxchars)):
            string.append(choice(charset))
        allLines.append(join(string))
    return '\n'.join(allLines)
