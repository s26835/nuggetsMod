#!/usr/bin/env python

'This module introduces a number of mathematical functions'

import numbers as _num
import statistics as stat
import fraction
from math import pi
from random import randint

def calcGrade(percentageGrade):
    'Takes a percentage grade and converts it to letter; returns result'
    
    #percentageGrade defines grade to be converted
    
    percent = float(percentageGrade)
    grade = None
    
    if percent < 60:
        grade = 'F'
    elif percent < 70:
        grade = 'D'
    elif percent < 80:
        grade = 'C'
    elif percent < 90:
        grade = 'B'
    else:
        grade = 'A'

    return(grade)

def centDiv(cents):
    'Divides a number of cents into as little U.S. coins as possible'

    numCents = int(cents)
    
    if numCents >= 100:
        raise ValueError('centDiv() expected cents to be < 100; got %s' % (cents))
    else:
        #calculates quarters
        quarters = str(numCents // 25)
        remainder = numCents % 25

        #calculates dimes
        dimes = str(remainder // 10)
        remainder %= 10

        #calculates nickels
        nickels = str(remainder // 5)
        remainder %= 5

        #calculates pennies
        pennies = str(remainder)
        remainder = 0 #for consistency
        
        print(quarters + " quarters, " + dimes + " dimes, " + nickels + " nickels, and " + pennies + " pennies.")
        
#These are from excersises learning Python        
def circleArea(radius):
    area = math.pi * (radius**2)
    return(area)

def isdivisible(dividend, divisor, /): #get rid of / parameter if your Python version is earlier than 3.8
    'finds if dividend is divisible by divisor'
    if dividend % divisor == 0:
        return(True)
    else:
        return(False)

def f2c(farenheit):
    'converts farenheit to celsius'
    celsius = (farenheit - 32) * (5/9)
    return celsius
    
def c2f(celsius):
    'converts celsius to farenheit'
    farenheit = (celsius / (5/9)) + 32
    return farenheit

'''def minToHours(minutes):
    'converts minutes to hours and minutes'
    return dict(('hours', 'minutes'), divmod(minutes, 60))'''

#Statistical functions

def qdict(*data):
    return dict(zip(['q1', 'q2', 'q3'], stat.quantiles(data)))

def iqr(*data):
    "Interquartile range"
    
    if len(data) == 1 and isinstance(data[0], (list, tuple)):
        data = data[0]
    q = stat.quantiles(data)
    return q[2] - q[0]

#This function is currently being prototyped
def _iavg(*data: _num.Number) -> float:
    """
    Intuitive AVeraGe
    Returns the best average for the data set
    Use fraction.Fraction instances for ratios
    Ignores mode; nobody likes it
    
    >>> iavg(3, 4, 5)
    4
    >>> from fractions import Fraction as F
    >>> iavg(F(60, 20), F(200, 50), F(5, 1))
    Fraction(180, 47)
    """
    
    if len(data) == 1 and isinstance(data[0], (list, tuple)):
        data = data[0]
    
    target = 1.5 * iqr(*data)
    q = qdict(*data)
    for item in data:
        if item < q['q1'] - target or item > q['q3'] + target:
            return stat.median(data)
        elif isinstance(item, fraction.Fraction):
            return stat.harmonic_mean(data)
    else:
        return stat.fmean(data)
