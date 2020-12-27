# CmpSc132 || Lab 2 || Omer Canca & Dominic Assia

import re

def resetPassword():

    # Ask user to enter a new password
    password = input('Enter your new password: \n')

    # Confirm the password
    second_password = input('Confirm your new password: \n')
   
    return password, second_password

def verification():

    password, second_password = resetPassword()

    # Continue if passwords match. Break if they do not

    if password != second_password:
        print('Your passwords do not match. Please try again')
        verification()

    return password

def requirements(password):

    # Confirm that password meets the desired restrictions

    if len(password) < 8 or len(password) > 16:
        print('Your password must be between 8 and 16 characters.')
        resetPassword()

    elif not re.search('[_@$!^*&~`]', password):
        print('Your password must contain a special character.')
        resetPassword()
        
    elif not re.search('[A-Z]', password):
        print('Your password must contain an uppercase character.')
        resetPassword()

    elif not re.search('[a-z]', password):
        [print('Your password must contain a lowercase character.')]
        resetPassword()

    else:
        print('Your password is valid and has been changed.')

    return password

def main(i):

    print('This program will help the user create a new password')

    # Ask the user to input the password
    old_password = input('Enter your current password: \n')

    while i != 0:

        if old_password != 'Basketball!':

            print('The password is incorrect.\n')
            i -= 1
            main(i)

        else:
            print('The password is correct')

            password = verification()

            finalPassword = requirements(password)

            print('your new password is:', finalPassword)

            exit()

    if i == 0:

        print('There has been too many attempts. The account is locked')
        exit()

# Initialize attemps

main(3)