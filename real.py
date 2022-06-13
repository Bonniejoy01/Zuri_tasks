import random
# R, P, S represent rock, paper, scissors.

while True:
    option = ["R", "P", "S"]

    computer = random.choice(option)
    player = None

    while player not in option:
        player = input("Pick a between Rock, Paper, Scissors by entering the intial letter: ").upper()

    if player == computer:
        print("Computer chooses :", computer)
        print("Player chooses :", player)
        print("It is a tie !!!")
    elif player == "R":
        if computer == "P":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Sorry you lose !!")
        if computer == "S":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Hurray you Win !!")
    elif player == "S":
        if computer == "R":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Sorry you lose !!")
        if computer == "P":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Hurray you Win !!")
    elif player == "P":
        if computer == "S":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Sorry you lose !!")
        if computer == "R":
            print("Computer chooses :", computer)
            print("Player chooses :", player)
            print("Hurray you Win !!")
    play_again = input("Will you like to play again?  (yes/no): ").lower()       

    if play_again != "yes":
        break
print("Bye, Thanks for Playing....")
