
import random
import math

# Take inputs for range and check if its a valid input (integer)

flag = True      # We're  only using flag so that we can end the loop after checking if the input is valid and print the same
while flag:      # We can just make the process smaller and use 'int' like in line 32
    lower = input("\nType in the lower bound: ")
    upper = input("Type in the upper bound: ")

    if lower.isdigit() and upper.isdigit():
        print("\nLet's Play!")
        lower = int(lower)
        upper = int(upper)
        flag =  False # To end the while loop
    else:
        print ("\nInvalid Input! Try Again!")

# generate a random number between the lower and upper bound
secret = random.randint(lower,upper) 


# Initialize the number of guesses and define the variable to be used for guessing
count = 0
guess = None


# Take input for guess; we can take lower and upper bound inputs as well with int

while guess != secret:  # while is required so that line 41 isn't repeated every time
    guess = int(input("\nGuess a number between " + str(lower) + " and " + str(upper) + ": "))

    # Checking if the guess is right or wrong
    if guess == secret:
        print("\nYayyy! You got it right!")
    else:
        print("\nWrong answer, guess again.")
        count += 1

print("\nIt took you", count,"guesses.\n")