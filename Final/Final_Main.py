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
    print('\nChose an option to select from the list below:\n\t1 - Math Operations\n\t2 - Pythagreon Theorem\n\t3 - Quadratic Formula\n\t4 - Baseball Statistics\n\t5 - New Password')

    try:
        temp = int(input('> '))


        if temp > 5 or temp <= 0:

            # Display Error, Restart
            print('\n** The selection is not an option **')
            main()

    except TypeError or ValueError:

        # Display Error, Restart
        print('\n** Input must be an integer **')
        main()




# Call main

if __name__ == "__main__":

    main()