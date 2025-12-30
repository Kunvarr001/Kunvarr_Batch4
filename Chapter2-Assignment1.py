#Assignment 1: The below program is to guess the correct number between 1 to 100

import random

def is_valid_guess(user_input):
    return user_input.isdigit() and 1 <= int(user_input) <= 100

def main():
    target_number = random.randint(1, 100)
    is_guessed_correctly = False
    guess_count = 0

    user_guess = input("Guess a number between 1 and 100: ")

    while not is_guessed_correctly:
        if not is_valid_guess(user_guess):
            user_guess = input( "Invalid input. Please enter a number between 1 and 100: ")
            continue
        guess_count += 1
        user_guess = int(user_guess)

        if user_guess < target_number:
            user_guess = input("It's low. Guess again: ")
        elif user_guess > target_number:
            user_guess = input("It's high. Guess again: ")
        else:
            print("You guessed it in", guess_count, "guesses!")
            is_guessed_correctly = True

main()


"""
Mistakes / Issues in the Original C# Code:
    1. Naming Conventions:
        Function name fun() is unclear; it doesnt convey that it validates the input.
        Variable names like n, gn, g, ng are not meaningful and reduce readability.
    2. Logical Issues:
        The function fun() references s, which is undefined inside its scope, potentially causing runtime errors.
    3. Descriptive messages: Error messages such as "I won't count this one …" are not user-friendly.

"""