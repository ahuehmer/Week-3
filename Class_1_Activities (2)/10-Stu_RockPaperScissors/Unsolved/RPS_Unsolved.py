# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors?")

#Print computer choices
if computer_choice == 'r':
    comp_full = ('rock')
elif computer_choice == 'p':
    comp_full = ('paper')
else: 
    comp_full = ('scissors')

print(f'Computer chooses {comp_full}')

# Run Conditionals
if computer_choice == 'r' and user_choice == 'p':
    print('You win!')
elif computer_choice == 'r' and user_choice == 's':
    print('Better luck next time!')
elif computer_choice == 'p' and user_choice == 'r':
    print('Better luck next time!')
elif computer_choice == 'p' and user_choice == 's':
    print('You win!')
elif computer_choice == 's' and user_choice == 'p':
    print('Better luck next time!')
elif computer_choice == 's' and user_choice == 'r':
    print('You win!')   
elif computer_choice == user_choice:
    print('Its a tie!') 
else: 
    print('Please enter either r, p, or s.')
