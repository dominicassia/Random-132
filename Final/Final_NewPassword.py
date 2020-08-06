'''
    Final New Password Module
    ~~~~~

    Functions:

    createNewPassword()
'''

import re

def createNewPassword():

    # Establish old password as constant in the beginning
    old_password = ('Basketball.')
    x = old_password

        # Confirm that password meets the desired restrictions
    
    def not_main():

        # Ask user to enter a new password
        password = input('Enter your new password: ')

        # Confirm the password
        second_password = input('Confirm your new password: ')

        # Continue if passwords match. Break if they do not
        if password == second_password:
            print('Your passwords match. ')

            if len(password)<8 or len(password)>16:
                print('Your password must be between 8 and 16 characters.')

            if not re.search(password, '!$*.'):
                print('Your password must contain a special character.')

            if not re.search('[A-Z]', password):
                print('Your password must contain an uppercase character.')

            if not re.search('[a-z]', password):
                print('Your password must contain a lowercase character.')
        
            else:
                print('Your password is valid and has been changed.')

        while password != second_password:
            print('Your passwords do not match. Please try again')
            break

    print('This program will help the user create a new password')

    # Ask the user to input the password
    old_password1 = input('Enter your current password ')


    if old_password1 != x:
        print('The password is incorrect.')
        old_password1 = input('Enter your current password ')

        if old_password1 != x:
            print('The password is incorrect.')
            old_password1 = input('Enter your current password ')

        else:
            print('The password is correct')
            not_main()

            if old_password1 != x:
                print('The password is incorrect.')
                old_password1 = input('Enter your current password ')

            else:
                print('The password is correct')
                not_main()


                if old_password1 != x:
                    print('The password is incorrect. The program is locked now because of too many attempts')

                else:
                    print('The password is correct')
                    not_main()
    
    else:
        print('The password is correct')
        not_main()
