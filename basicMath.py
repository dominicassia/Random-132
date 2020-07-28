# Cmpsc 132 || Lab 3: Working with Functions || Omer Canca & Dominic Assia

import math     # Basic operations
import cmath    # Import cmath in order to insert square root function

# Define basic math function.
def basicMath():

    # Ask the user to enter two real numbers
    s = float(input('Enter a real number to perform basic math calculations. '))
    r = float(input('Enter a second real number to perform basic math calculations. '))

    # Print results
    print(s, '+', r, ':', s + r)
    print(s, '-', r, ':', s - r)
    print(s, '*', r, ':', s * r)
    print(s, '/', r, ':', s / r)

# Define pythagorean thereom function
def pythagThereom():

    # Ask the user for two values 
    a = float(input('Enter a real number to perform the pythagorean thereom. '))
    b = float(input('Enter a second real number to perform the pythagorean thereom. '))

    #Calculate and print the answer
    c = (a**2 + b**2)
    print('c:', c)

# Define quad. formula function
def quadFormula():
    
    # ask the user for inputs of a, b, and c values
    a = float(input('What is the value for a? '))
    b = float(input('What is the value for b? '))
    c = float(input('What is the value for c? '))

    h = (b**2) - (4 * a * c)

    # Create a value for the denominator
    e = (2 * a)

    # Check to see if negative values exist under the radical
    if h <= 0:
        print('Error. The first solution is undefined. There is a negative in the radical.')


        return lst

    # Check to see if there are zeros in the denominator
    if e == 0:
        print('Error. The first solution is undefined. There is a 0 in the denominator')
        quadFormula()

    # Create a value for the discriminant
    d = cmath.sqrt(h)

    # Use quadratic formula to have program calculate answers
    # Use an addition formula and a subtraction formula
    solution_1 = (-b + d) / (e)
    solution_2 = (-b - d) / (e)

    # If there are no errors, solve the equation

    # Print the solutions for the user
    print('The first solution is ', solution_1)
    print('The second solution is ', solution_2)

def main():

    print('This program will perform basic math, the pythagorean thereom, and the quadratic formula based on input by the user.')

    basicMath()
    pythagThereom()
    quadFormula()

# Call main function to call 3 math type functions

main()

'''
Notes:

    main() has to go at the end of the file (always) as none of the functions you were calling 'exist' yet
    call functions with () not (): 
    watch indentation when defining a function, always tab in to write in the function ( basicMath() )
    no need to call functions within your code / between functions! that is what main() is for
    importing cmath within a function doesn't seem to be an issue, but it is standard to do it at the beginning of a file unless specified
    make sure you initialize your input to somthing other than a str to do calculations. I chose float(input('')) but you can make it an int if needed

'''