# Initial variable to track shopping status
user_choice = 'yes'

# List to track pie purchases
pie_cart = [] 

# Pie List
list_of_pies = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee', 'Black Bun', 
                'Blueberry', 'Buko', 'Burek',  'Tamale', 'Steak']

# Display initial message
print('Welcome to the House of Pies! Here is our menu:') 

#while statement to apply to all the following: 
while user_choice == 'yes':

    #display list of pies
    print('----------------------------------------------------')
    for pies in list_of_pies:
        print(f'[{list_of_pies.index(pies)}] {pies}')

    # Get index of the pie from the selected number
    order = int(input('Select the number of the pie you would like?'))

    # Add pie to the pie list by finding the matching index and adding one to its value
    pie_cart.append(list_of_pies[order])

    # Inform the customer of the pie purchase
    print(f'Great! We will have the {list_of_pies[order]} ready for you!')

    # Provide exit option
    user_choice = input('Would you like to continue shopping? yes or no')

# Once the pie list is complete
print('You purchased a total of ' +str(len(pie_cart)) + ' pies.')

# Count instances of each pie


# Loop through the full pie list


    # Gather the count of each pie in the pie list and print them alongside the pies