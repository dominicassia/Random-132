# Logan Hicks & Dominic Assia
'''
    * When the program starts up, ask the user if they want to add a new record or if they want to display results. 
    If they display results, load up all data from CSV and plots it in some sensible way. 
    Recommend that logs from practice be plotting in a different color/line then the results from competitions. 
    If they want to add a new record, you have to ask them several questions so you can save all of the appropriate data.
    * User input is going to need to be validated. 
'''
import matplotlib.pylab as plt

# --------- Helper functions ---------

def menu():
    ''' Returns the menu option asked to the user '''

    # When the program starts up, ask the user if they want to add a new record or if they want to display results.
    menu = str(input('Welcome to the track athlete database. Choose an option: [1]- Add a new record [2]- Display results [3]- Exit  '))
    
    # Input validation
    while not menu.isnumeric() or not ( menu == '1' or menu == '2' or menu == '3'):

        menu = str(input('Invalid option. Choose an option: [1]- Add a new record [2]- Display results [3]- Exit  '))

    return menu


def get_name(question):
    ''' Ask for user's name, validate '''

    name = str(input(question))

    while not( name.isalpha() ):
        name = str(input('Invalid. ' + question))

    return name.title()


def generic_input(question):
    ''' Prompts the User a question expecting 1 or 2 as the input '''

    # Initally ask
    ans = str(input(question))

    # Input validation
    while not ans.isnumeric() or not (ans == '1' or ans == '2'):

        ans = str(input('Invalid option. ' + question))

    return ans


def get_date():
    ''' Ask for the date were logging for, validate '''

    date = str(input('What date are you logging? Format: [MM/DD/YYYY]  '))

    # Input validation
    while not ('/' in date and len(date.split('/')) == 3 and len(date.split('/')[0]) == 2 and len(date.split('/')[1]) == 2 and len(date.split('/')[2]) == 4 and date.split('/')[0].isnumeric() and date.split('/')[1].isnumeric() and date.split('/')[2].isnumeric()):
                        
        date = str(input('Invalid format. Format: [MM/DD/YYYY]  '))

    while not( ( int(date.split('/')[0]) >= 1 and int(date.split('/')[0]) <= 12) and (int(date.split('/')[1]) >= 1 and int(date.split('/')[1]) <= 31) and (int(date.split('/')[2]) >= 2000 and int(date.split('/')[2]) <= 2020) ):

        date = str(input('Date out of range / Invalid Format. Range: [01-12/01-31/2000-2020] Format: [MM/DD/YYYY]  '))

    return date


def get_duration():
    ''' Asks for duration, validates '''

    # Ask for the duration of the workout/run
    duration = str(input('Enter the duration of your run/workout. Format [HH:MM:SS]  '))

    # Input validation
    while not (':' in duration and len(duration.split(':')) == 3 and len(duration.split(':')[0]) == 2 and len(duration.split(':')[1]) == 2 and len(duration.split(':')[2]) == 2 and duration.split(':')[0].isnumeric() and duration.split(':')[1].isnumeric() and duration.split(':')[2].isnumeric()):

        duration = str(input('Invalid format. Format: [HH:MM:SS]  '))

    while not ( ( int(duration.split(':')[0]) >= 0 and int(duration.split(':')[0]) <= 59) and (int(duration.split(':')[1]) >= 0 and int(duration.split(':')[1]) <= 59) and (int(duration.split(':')[2]) >= 00 and int(duration.split(':')[2]) <= 59) ):

        duration = str(input('Time out of range / Invalid Format. Range: [00-59:00-59:00-59] Format: [HH:MM:SS]  '))

    # -- Convert to seconds --
    seconds = convert_to_seconds(duration)

    return str(seconds)


def convert_to_seconds(duration):
    ''' Takes a formated duration and returns it in seconds '''

    seconds = 0

    duration = duration.split(':')

    seconds += int(duration[0]) * 3600

    seconds += int(duration[1]) * 60

    seconds += int(duration[2])

    return seconds


def get_unit(question):
    ''' Asks the user how many units of something they did, validates '''

    ans = str(input(question))

    # Input validation
    while not( ans.isnumeric() ):

        ans = str(input('Invalid. ' + question))

    return ans


def validate_athlete(name, view, runners, track):
    ''' Validates whether a name is a track athlete or runner '''
    
    # -- Check if the name is a team member --

    while name not in runners.keys() and name not in track.keys():

        print('{} is not in the database'.format(name))
        name = get_name('Please enter a team member\'s name to view:  ')

    # -- Check if the team member is a runner/track athlete, compare to view variable --

    if view == '1' and name not in runners.keys() and name in track.keys():

        print('{} is not a runner, they\'re a track athlete'.format(name))
        print('Displaying {} as a track athlete.'.format(name))

        view = '2'

    if view == '2' and name not in track.keys() and name in runners.keys():

        print('{} is not a track athlete, they\'re a runner'.format(name))
        print('Displaying {} as a track athlete.'.format(name))

        view = '1'

    return name, view


def sort_practice_competition(name, lst):
    ''' Sorts competition and practice data '''       

    # -- initalize lists --
    c_duration = []
    c_unit = []
    c_date = []

    p_duration = []
    p_unit = []
    p_date = []

    # -- Iterate through all data enteries for that person --
    for i in range(len(lst[name])):

        # -- Separate between practice and competitions for graph --
        if lst[name][i][1] == '1':

            p_unit.append(int(lst[name][i][3]))     # duration
            p_duration.append(int(lst[name][i][5])) # unit
            p_date.append(lst[name][i][2])          # date

        # -- Separate between practice and competitions for graph --
        if lst[name][i][1] == '2':

            c_unit.append(int(lst[name][i][3]))     # duration
            c_duration.append(int(lst[name][i][5])) # unit
            c_date.append(lst[name][i][2])          # date

    return c_duration, c_unit, c_date, p_duration, p_unit, p_date


def sort(duration, unit, date):
    ''' Sorts the duration in ascending order '''

    d = []
    u = []
    dt = []

    # -- Get the min value in duration & find its index to swap unit --
    for i in range(len(duration)):

        min_val = min(duration)
        idx = duration.index(min_val)

        # -- Append to d & u --

        d.append(min_val)
        u.append(unit[idx])
        dt.append(date[idx])

        # -- Remove the min val and correlating unit --

        duration.remove(min_val)
        unit.remove(unit[idx])
        date.remove(date[idx])

    return d, u, dt


def plot(name, view, comp_duration, comp_unit, comp_date, prac_duration, prac_unit, prac_date):
    ''' Plots competition/practice miles vs time '''

    # -- Set title and labels --

    plt.title('{}\'s Stats'.format(name))

    if view == '1':
        plt.ylabel('Miles')

    if view == '2':
        plt.ylabel('Reps')
    
    plt.xlabel('Seconds')
    plt.grid()

    # -- Annotate --
    for i in range(len(comp_date)):
        plt.annotate( comp_date[i], (comp_unit[i], comp_duration[i]) )

    for j in range(len(prac_date)):
        plt.annotate( prac_date[j], (prac_unit[j], prac_duration[j]) )

    # -- Plot --
    plt.scatter(prac_unit, prac_duration, color='Orange', label='Practice')
    plt.scatter(comp_unit, comp_duration, color='Blue', label='Competitions')
    
    plt.legend()

    print('Plot is being displayed.')
    plt.show()


# --------- Main functions ---------

def record():
    ''' Ask user several questions, save all of the appropriate data '''

    # Add all the data to a list to write to the file at the end
    data = []

    # Open the CSV file in append mode
    with open('data.csv', 'a') as file_write:
        
        # -- User's name --
        name = get_name('Enter your name first name:  ')
        data.append(name)

        # -- Competition or practice --

        type = generic_input('Are you recording a practice or competition? [1]-Practice [2]-Competition  ')
        data.append(type)

        # -- Date --

        date = get_date()
        data.append(date)

        # -- Duration -- 

        duration = get_duration()
        data.append(duration)

        # -- Athlete type -- 

        athlete = generic_input('What type of athlete are you? Choose an option: [1]-Runner [2]-Sprinter/Field Event  ')
        data.append(athlete)

        # -- Distance runners can log their miles / Sprinters and Field event Athletes can log workouts --

        if athlete == '1':
            
            # Runner

            distance = get_unit('How many miles did you run?  ')
            data.append(distance)

        if athlete == '2':
            
            # Track athlete
            repetitions = get_unit('How many repetitions did you do?  ')
            data.append(repetitions)

        # -- Format for CSV --

        write_data = ','.join(data)

        # -- Write the data to the file --

        file_write.write(write_data)
        file_write.write('\n')

        print('Data recorded.')


def display():
    ''' Load up all data from CSV and plot it in some sensible way. '''
    
    # Read format: [NAME, 1:PRACTICE/2:COMP, DATE, DURATION, 1:RUNNER/2:TRACK, IF 1:MILES/IF 2:REPS ]

    # RUNNERS/TRACK format: { NAME: [[data_set1], [data_set2],..], NAME: [..],..}

    runners = {}
    track = {}

    # --------------------

    # Open the CSV file to read
    with open('data.csv', 'r') as file_read:

        # -- Iterate over each line and place data in a list --
        for line in file_read:

            # -- Split over the commas --
            data = line.split(',')

            # -- Remove the \n --
            if '\n' in data[-1]:
                data[-1] = data[-1][:-1]

            # -- Sort between runners and track athletes --
            if data[4] == '1':
                
                # Check if the name is already a key
                if data[0] not in runners.keys():

                    # Create the member's list
                    runners[ data[0] ] = []

                # Add the data
                runners[ data[0] ].append(data)

            if data[4] == '2':

                # Check if the name is already a key
                if data[0] not in track.keys():

                    # Create the member's list
                    track[ data[0] ] = []

                # Add the data
                track[ data[0] ].append(data)

        # -- View track or runner --
        view = generic_input('Would you like to view runner or track stats? [1]-Runner [2]-Track  ')

        # -- Get name --
        name = get_name('Please enter a team member\'s name to view:  ')

        # -- Validate athlete type --
        name, view = validate_athlete(name, view, runners, track)

        if view == '1':
            c_duration, c_unit, c_date, p_duration, p_unit, p_date = sort_practice_competition(name, runners)

            # -- Sort the data --
            comp_duration, comp_unit, comp_date = sort(c_duration, c_unit, c_date)
            prac_duration, prac_unit, prac_date = sort(p_duration, p_unit, p_date)

        else:
            c_duration, c_unit, c_date, p_duration, p_unit, p_date = sort_practice_competition(name, track)

            # -- Sort the data --
            comp_duration, comp_unit, comp_date = sort(c_duration, c_unit, c_date)
            prac_duration, prac_unit, prac_date = sort(p_duration, p_unit, p_date)

        # -- Plot --

        plot(name, view, comp_duration, comp_unit, comp_date, prac_duration, prac_unit, prac_date)


# --------- Main ---------

def main():
    ''' Database for Track Athletes.
        - Distance runners can log their miles
        - Sprinters and Field event Athletes can log workouts.

        Log for competition results. 
        Computes and displays trends and personal best achievements. 
        Save info to a CSV file.
    '''

    # Gets the user's option
    m = menu()

    # Add a new record
    if m == '1':
        record()

    # Display results
    if m == '2':
        display()

    # Quit
    if m == '3':
        exit()

    # Restart the program
    print('')
    main()


if __name__ == "__main__":
    main()