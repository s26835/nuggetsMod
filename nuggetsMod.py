#!/usr/bin/env python

'this module introduces a number of micellanous functions'

from math import pi
from os import linesep
from time import sleep

import nuggetsRE as nRE

class Attack(object):
    'Creates a Super Smash Bros. attack; meant to be used for fighters\nFor Final Smash, set attackType (attackName.type) to "Final Smash" (case sensitive)'
    
    def __init__ (self, attackDirection, attackType, description = "This is an attack", name = None, damage = None):
        self.direction = attackDirection
        self.type = attackType
        self.damage = damage
        self.effect = description

    def describe(self):
        pass
        
class Fighter(object):
    'Creates a Super Smash Bros. fighter'
    
    def __init__ (self, name, ID, writeToFile=False, file='modinfo.py'):
        '''Initializes the fighter.\nSet writeToFile to True to append fighter creation code to a file (defaults to logfile.txt)'''
        self.id = "u#{}".format(ID)
        self.name = name
        self.neutralB = Attack('Neutral', 'special')
        self.sideB = Attack('Side', 'special')
        self.upB = Attack('Up', 'special')
        self.downB = Attack('Down', 'special')
        self.finalSmash = Attack('Neutral', "Final Smash")
        self.sideSmash = Attack('Side', 'smash')
        self.upSmash = Attack('Up', 'smash')
        self.downSmash = Attack('Down', 'smash')
        self.neutral = Attack('Neutral', '')
        self.sideTilt = Attack('Side', 'tilt')
        self.upTilt = Attack('Up', 'tilt')
        self.downTilt = Attack('Down', 'tilt')
        self.dash = Attack('Dash', '')
        self.air = Attack('Neutral', 'air')
        self.sideAir = Attack('Side', 'air')
        self.upAir = Attack('Up', 'air')
        self.downAir = Attack('Down', 'air')
        self.flurry = Attack('Flurry', '')
        self.traits = {}
        
        print("{} {} initialized. Prepare to fight!".format(self.id, self.name))
        
        self.saveCode = 'from nuggetsMod import Attack, Fighter %s%s = Fighter("%s", %s)' % (linesep, self.name.lower(), name, ID)
        
        if writeToFile:
            f = open(file, 'a')
            f.write(self.saveCode)
            f.close()
        else:
            print('\nTo save your fighter, copy and paste the following code to a file for safekeeping: \n\n%s' % (self.saveCode))
        print('\nTo save an attribute you set, copy the code into the same file (after declaration)')
        print('\nFighter saved!')

    def __del__(self):
        print("R.I.P. " + self.name)
        del self

    def save(self, file='modinfo.py'):
        f = open(file, 'a')
        f.write(self.saveCode)
        f.close()



def userEnter():
    while True:
        key = input()
        if nRE.match(r'.|\n', key):
            break

def ueprint(value):
    print(value + " \t(Press any character key followed by ENTER to continue)")
    userEnter()

def sprint(value, seconds):
    print(value)
    sleep(seconds)        

def randomNums():
    'Returns a list of a random number of random integers'
    randList=[]
    randList2=[]
    for i in range(randint(1,100)):
        randList.append(randint(1,100))
    for foo in range(randint(1,100)):
        randList2.append(randList[randint(1,100)])
    return randList2

def rpsGame():
    'Plays a randomized rock, paper, scissors game'
    comVic=0; playerVic=0;
    rounds=2;

    while rounds % 2 == 0:
        rounds = int(input("How many rounds? (Must be an odd number.) "))
        print()
    
    for i in range(rounds):
        
        roundNum = i+1
        output = "Tie"
        
        def decide():
                c = str(input("Enter 'rock', 'paper', or 'scissors' (without the quotes): ")); c = c.lower()
                return c
        
        print("Round {}!\n".format(roundNum))

        choice = decide()

        comChoice = int(randint(1,3))
        comChoiceStr=None
        #1: rock
        #2: paper
        #3: scissors
        if comChoice == 1:
            comChoiceStr = 'rock'
        elif comChoice == 2:
            comChoiceStr = 'paper'
        else:
            comChoiceStr = 'scissors'
        
        if (comChoice == 1 and choice == 'paper') \
        or (comChoice == 2 and choice == 'scissors') \
        or (comChoice == 3 and choice == 'rock'):
            output="Victory!"
            playerVic+=1
            
        elif (comChoice == 1 and choice == 'scissors') \
        or (comChoice == 2 and choice == 'rock') \
        or (comChoice == 3 and choice == 'paper'):
            output="Defeat!"
            comVic+=1
            
        else:
            output="Tie."

        print("\nComputer opponent played {}.".format(comChoiceStr), output, "\n")

    if playerVic > comVic:
        print("Player wins!")
    elif comVic > playerVic:
        print("Computer wins!")
    else:
        print("Tie. Play again!")

def counter(start, stop, increment=1):
    'counts from start to stop by the increment'
    for i in range(start, stop+1, increment):
        print(i)


def numChart(decimal=True, binary=True, octal=True, hexadecimal=True, unicode=True):
    'Returns a chart of decimal numbers to other numbers and characters'
    start = int(input("Enter a start value: "))
    stop = int(input("Enter a stop value: "))
    for i in range(start, stop+1):
        print("DECIMAL: {}; BINARY: {}; OCTAL: {}; HEXADECIMAL: {}; UNICODE: {}".format(str(i), bin(i)[2:], oct(i)[2:], hex(i)[2:], chr(i)))

if __name__ == '__main__':
    pass
