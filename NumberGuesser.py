from random import randint

print("Welcome to the number guesser game. \nGuess the correct number to win.\n")

while input("Do you want to play? (no to quit):").lower() != "no":
    winning_number = randint(0, 10)

    player_number = int(input("Guess a number from 1 to 10:"))
    while player_number != winning_number:
        if player_number < winning_number:
            print("try a larger number")
        else:
            print("try a smaller number")
        player_number = int(input("Guess a number from 1 to 10:")) 
    
    print("You Win!")