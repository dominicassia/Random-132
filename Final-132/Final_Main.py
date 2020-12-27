# Dominic Assia & Omer Canca
'''
    CMPSC 132 | Final Project | Dominic Assia & Omer Canca

    Final Project
    ~~~~~
    This is the final lab of this Summer class.
    This assignments combines several labs, we worked on, into 1 python program.
    Pay attention to all of the details.  Use the python file names that I mention below.
'''

# Import modules

import Final_Math as math
import Final_Stats as stats
import Final_NewPassword as password

def main():

    # Menu of programs
    print('\nChose an option to select from the list below:\n\t1 - Math Operations\n\t2 - Pythagreon Theorem\n\t3 - Quadratic Formula\n\t4 - Baseball Statistics\n\t5 - New Password\n\t6 - Exit')

    temp = input('> ')

    try:
        temp = int(temp)

    except ValueError or TypeError:

        # Display Error, Restart
        print('\n** Input must be an integer **')
        main()

    if int(temp) > 6 or int(temp) <= 0:

        # Display Error, Restart
        print('\n** The selection is not an option **')
        main()

    if temp == 1:

        print('\n\t---------\tMath Operations')

        # Take input
        s = float(input('\nEnter a real number to perform basic math calculations. '))
        r = float(input('\nEnter a second real number to perform basic math calculations. '))

        # Call function
        math.calcMathOperations(s, r)

        # Restart
        print('\n\t---------')
        main()

    elif temp == 2:

        print('\n\t---------\tPythagreon Theorem')

        # Take input
        a = float(input('\nEnter a real number to perform the pythagorean thereom. '))
        b = float(input('\nEnter a second real number to perform the pythagorean thereom. '))

        # Call function
        math.calcPythagThm(a, b)

        # Restart
        print('\n\t---------')
        main()

    elif temp == 3:

        print('\n\t---------\tQuadratic Formula')
        print('\nThis program will produce two answers using the quadratic formula based off of user inputs')

        # Take input
        a = float(input('\nWhat is the value for a? '))
        b = float(input('\nWhat is the value for b? '))
        c = float(input('\nWhat is the value for c? '))

        # Call function
        math.calcQuadForm(a, b, c)

        # Restart
        print('\n\t---------')
        main()

# Call main
if __name__ == "__main__":

    main()