# Cmpsc 132 || Lab 4 || Omer Canca & Dominic Assia

# Create the global tuple
presidents_tuple = ('Washington', 'Adams', 'Jefferson', 'Monroe', 'Adams', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Mckinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump')

def checkGuess(guess):

    # Loop through all presidents in the tuple

    for i in range(len(presidents_tuple)):

        x = 0

        # Check tuple value against guess

        if presidents_tuple[i].upper() == guess:

            # The guess matches a value in the tuple

            x = 0 
            break

        else:

            x += 1

    if x == 0:
        print('Your guess was correct')
        return True

    else:
        print('Your guess was incorrect')
        return False

def main():

    # Create dynamic list

    lst = []

    # Wrong guesses var

    wrongGuesses = 0
    rightGuesses = 0

    # Explain the game

    print('The objective of this game is to guess all presidents by last name before running out of guesses.')

    # Create an amount of chances

    chances = int(input('Enter the amount of wrong guesses you would like before you lose the game. Between 1 and 8.\n'))
    
    # Loop through amount of chances

    for i in range(chances):

        # Convert guess to uppercase

        guess = str(input('Enter the name of a president\n')).upper()

        inTuple = checkGuess(guess)

        # Compare the contents of lst to the guess

        inList = False

        for j in range(len(lst)):

            # Check list value to guess

            if lst[j].upper() == guess:

                # This guess has already been made

                inList = True

            else:

                # This guess has not been made

                inList = False

        # -----

        if inTuple == True and inList == False:

            rightGuesses += 1

            lst.append(guess)

            print('You have not guessed', len(presidents_tuple)-len(lst), 'president\n')

            print('Percentage of names guessed correctly:', round( (rightGuesses/(rightGuesses + wrongGuesses))*100 , 4 ), '%\n' ) 

            indexNums = []

            for k in range(len(lst)):

                for l in range(len(presidents_tuple)):

                    if lst[k].upper() == presidents_tuple[l].upper():

                        indexNums.append(l)

            print(indexNums)

            lowest = 100

            for m in range(len(indexNums)):

                if indexNums[m] < lowest:

                    lowest = indexNums[m]

            print('Index of earliest president not guessed:', lowest-1, '\n') 

        elif inTuple == False:

            wrongGuesses += 1

            print(guess.lower(), 'is not a president\n')

            print('Wrong guesses :', wrongGuesses, '\n')

# call main

main()