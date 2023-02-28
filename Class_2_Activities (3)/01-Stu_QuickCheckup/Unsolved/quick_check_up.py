# Print Hello User!
print('Hello user!')

# Take in User Input
user_input = input('What is your name?')

# Respond Back with User Input
print(f'Hello {user_input}!')

# Take in the User Favorite Number
user_number = int(input('What is your favorite number?'))

# Respond Back with a statement based on your favorite number
if user_number < 8:
    print('Your favorite number is less than my favorite number.')
elif user_number > 8:
    print('Your favorite number is greater than my favorite number.')
elif user_number == 8:
    print('Your favorite number is my favorite number too.')