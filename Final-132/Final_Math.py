# Dominic Assia & Omer Canca
'''
    Final Math Module
    ~~~~~

    Functions:

    calcMathOperations()
    calcPythagThm()
    calcQuadForm()
'''

import cmath
from Final_Main import main as fmain

def calcMathOperations(s, r):

    # Print results
    print('\n')
    print(s, '+', r, '=', s + r)
    print(s, '-', r, '=', s - r)
    print(s, '*', r, '=', s * r)
    print(s, '/', r, '=', s / r)

def calcPythagThm(a, b):

    #Calculate and print the answer
    c = cmath.sqrt((a**2) + (b**2))
    print('\nc:', c)

def calcQuadForm(a, b, c):

    h = (b**2) - (4 * a * c)

    # Create a value for the denominator
    e = (2 * a)

    # Check to see if negative values exist under the radical
    if h <= 0:
        print('\nError. The first solution is undefined. There is a negative in the radical.')

    # Check to see if there are zeros in the denominator
    if e == 0:
        print('\nError. The first solution is undefined. There is a 0 in the denominator')

    # Create a value for the discriminant
    d = cmath.sqrt(h)

    # Use quadratic formula to have program calculate answers
    # Use an addition formula and a subtraction formula
    solution_1 = (-b + d) / (e)
    solution_2 = (-b - d) / (e)

    # If there are no errors, solve the equation

    # Print the solutions for the user
    print('\nThe first solution is ', solution_1)
    print('\nThe second solution is ', solution_2)