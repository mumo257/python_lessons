# Guess a number and ask the user to guess that number
# import the random module
import random

# let the program guess the secret number
secret_number = random.randint(1, 100)

# keep track of how many times the user has guessed
attempt = 0

# create a loop to allow the user to guess multiple times
while True:
    # get the user input/guess
    guess = int(input("Enter the number in your mind: "))

    # allow user to play multiple times
    attempt += 1

    # check the number
    if guess < secret_number:
        print("Oops! The number you guessed is too low, try again")
    elif guess > secret_number:
         print("Oops! The number you guessed is too high, try again")
    else:
        print("Congratulations! The number {} is accurate, and you have guessed {} times".format(guess, attempt))
        break



