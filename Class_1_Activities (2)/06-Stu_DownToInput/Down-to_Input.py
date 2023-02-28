my_first_name = input('What is your name?')
neighbors_first_name = input('What is your neighbors first name?')

months_you_coded = int(input('How many months have you coded?'))
months_neighbor_coded = int(input('How many months has your neighbot coded?'))
total_months = months_you_coded + months_neighbor_coded 

print('I am' + my_first_name + ' and my neighbor is ' + neighbors_first_name + '.')
print('Togther we have been coding for ' + str(total_months) + 'months. ')