user_input = 'y'

previous_variable = 0

while user_input == 'y':
    user_variable = int(input('How many numbers should be displayed?'))

    for answer in range(previous_variable, previous_variable + user_variable):
        print(answer)

    previous_variable = user_variable + previous_variable
        
    user_input = input('Would you like to continue? y or n')

