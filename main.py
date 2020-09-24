# The game "Bulls & Cows"

import random
import time
import sys

start_time = time.time()

# The main function
def main():
    # Random number
    random_num = random_number()
    print(60*"=")
    print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play the Bulls & Cows game.")
    print(60*"=")
    print("Please remember, every digit in the number is unique.\nGood luck!")
    print(60*"=")

    # Number of guesses
    guess = 0

    # Bull = the number and position is correct, Cow = the number is correct, but the position is wrong
    while True:

        # Player's guess
        player_num = list(input("Enter the number:"))
        if len(player_num) != 4:
            print("Remember you are guessing 4 digit number!")
            guess += 1
            continue

        guess += 1

        # Any Bulls or Cows?
        bull = 0
        cow = 0
        for i in player_num:
            if i not in random_num:
                continue
            elif player_num.index(i) == random_num.index(i):
                bull += 1
            elif i in random_num:
                cow += 1

        # Victory
        if random_num == player_num:
            print(f"Correct, you've guessed the right number in {guess} guesses!")
            break

        # How many Bulls and Cows
        print(f'{bull} bulls, {cow} cows')

    # Player's evaluation
    if guess <= 5:
        print("That is amazing!")
    elif guess > 5 and guess <= 10:
        print("That is not bad.")
    elif guess > 10 and guess <= 15:
        print("Wish you better luck next time.")
    elif guess > 15:
        print("You should go back to kindergarden! :D")


# Random number, !every single number must be unique!
def random_number():
    secret_num = []
    end = True

    while end:
        num = str(random.randrange(0, 10))

        if num not in secret_num:
            secret_num.append(num)

        if len(secret_num) == 4:
            end = False

    return secret_num


# Let's play the game!
if __name__ == '__main__':
    sys.exit(main())

elapsed_time = time.time() - start_time
print(f'The game took you {elapsed_time} seconds.')
