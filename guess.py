import random

random_number = random.randint(1, 11)

#guess = input("Guess a number!: ")

#guess = int(guess)

while True:
    guess = input("Guess a number!: ")
    guess = int(guess)
    if guess > random_number:
        print("Sorry too high, please try again!: ")
    elif guess < random_number:
        print("Sorry too low, please try again: ")
    else:
        print("You win!!")
        play_again = input("Do you want to play again? (y/n)")
        play_again.islower()
        if play_again == "y":
            random_number == random.randint(1, 11)
            guess = None
        else:
            print("Thanks for playing")
            break
