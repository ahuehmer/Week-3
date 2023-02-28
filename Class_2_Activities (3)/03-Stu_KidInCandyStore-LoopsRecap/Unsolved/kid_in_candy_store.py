# The list of candies to print to the screen
candy_list = [
    "Snickers", 
    "Kit Kat", 
    "Sour Patch Kids", 
    "Juicy Fruit", 
    "Swedish Fish", 
    "Skittles", 
    "Hershey Bar", 
    "Starbursts", 
    "M&Ms"
    ]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options with index numbers
for candy in candy_list:
    print(f'[{candy_list.index(candy)}] {candy}')

#take input of candy selection
print('Which candy would you like to select?')
for x in range(allowance):
    candy_selection = input('Input the candy you would like to select.')

    #add candy to candy cart
    candy_cart.append(candy_list[int(candy_selection)])

print('This is your selection:')
for candy in candy_cart:
    print(candy)