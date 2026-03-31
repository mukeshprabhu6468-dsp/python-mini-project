#NUMBER GUESSING

import random as r
print("Welcome to the Number Guessing Game")
number = r.randint(1,100)
attempts = 0
guess = 0
while guess != number:
    guess = int(input("Enter your guess (1-100):"))
    attempts += 1
    if guess < number:
        print("Number is Lower! Try again.")
    elif guess > number:
        print("Number is Higher! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        print("Total attempts:", attempts)


