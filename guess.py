#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This is guess the number program with a random number generator


import random


def main():
    # This function allows the user to try and guess the number

    # Variables
    correct_number = random.randint(1, 10)

    # Input
    user_guess = int(input("Guess the number between 1 & 10 (integer): "))
    print("")

    # process
    if user_guess == correct_number:
        # Output 1
        print("You correctly guessed the number!")
    else:
        # Output 2
        print("Wrong number, better luck next time!")
        print("The correct number is:", (correct_number))


if __name__ == "__main__":
    main()
