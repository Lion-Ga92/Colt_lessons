from random import randint

turns = 0
player_wins = 0
comp_wins = 0
winning_score = 3

while player_wins < winning_score and comp_wins < winning_score:
    print(f"player score: {player_wins} computer score: {comp_wins}")
    print("...ready... \n")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")
    player_1 = input("Player 1 make choice: ").lower()
    if player_1 == "quit" or player_1 == "q":
        break

    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    elif rand_num == 2:
        computer = "scissor"
    print(f"Computer plays {computer}")
    print("\n")

    if player_1 == computer:
        print("We have a tie")

    elif player_1 == "paper":
        if computer == "rock":
            print("player one wins")
            player_wins += 1
        else:
            print("Computer wins")
            comp_wins += 1


    elif player_1 == "rock":
        if computer == "scissor":
            print("Player one wins")
            player_wins += 1
        else:
            print("Computer wins")
            comp_wins += 1

    elif player_1 == "scissor":
        if computer== "paper":
            print("Player one wins")
            player_wins += 1
        else:
            print("Computer wins")
            comp_wins

    else:
        print("Enter valid value 'rock', 'paper', 'scissor'")


if player_wins > comp_wins:
    print("Congrats you won!!")
elif player_wins == comp_wins:
    print("it is a tie")
else:
    print("Oh no, computer won!")
