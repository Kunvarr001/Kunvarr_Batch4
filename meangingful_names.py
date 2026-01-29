
# ASSIGNMENT 1 : ROLL THE DICE

import random

def roll_dice(sides):
    rolled_number = random.randint(1, sides)
    return rolled_number

def main():
    number_of_sides = 6
    keep_rolling = True

    while keep_rolling:
        user_input = input("Ready to roll? Enter Q to Quit: ")
        
        if user_input.lower() != "q":
            result = roll_dice(number_of_sides)
            print("You have rolled a", result)
        else:
            keep_rolling = False

main()


# ASSIGNMENT 2 : GUESS THE NUMBER (1 to 100)

import random

def is_valid_guess(user_input):
    if user_input.isdigit() and 1 <= int(user_input) <= 100:
        return True
    else:
        return False

def main():
    secret_number = random.randint(1, 100)
    number_found = False
    guess = input("Guess a number between 1 and 100: ")
    guess_count = 0

    while not number_found:
        if not is_valid_guess(guess):
            guess = input("I won't count this one. Please enter a number between 1 and 100: ")
            continue
        else:
            guess_count += 1
            guess = int(guess)

        if guess < secret_number:
            guess = input("Too low. Guess again: ")
        elif guess > secret_number:
            guess = input("Too high. Guess again: ")
        else:
            print("You guessed it in", guess_count, "guesses!")
            number_found = True


main()

# ASSIGNMENT 3 : ARMSTRONG NUMBER CHECK
def calculate_armstrong_sum(number):
    digit_count = len(str(number))
    armstrong_sum = 0
    remaining_number = number

    while remaining_number > 0:
        digit = remaining_number % 10
        armstrong_sum += digit ** digit_count
        remaining_number //= 10

    return armstrong_sum

user_number = int(input("Enter a number to check for Armstrong: "))

if user_number == calculate_armstrong_sum(user_number):
    print(f"{user_number} is an Armstrong Number.")
else:
    print(f"{user_number} is NOT an Armstrong Number.")