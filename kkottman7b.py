#Karl Kottman
#CTC389
#Lab 7 - Lab 3&4 Review


def guessing_game():
    print("I'm thinking of a number between 1 and 10 inclusive. Can you guess it?")
    x = 0
    while (x != 6):
        x = int(input("Enter your guess:"))
        if (x == 6):
            print("You got it! The number is 6!")
        elif (x >= 4) and (x <= 8):
            print("So close! Guess again:")
        else:
            if (x < 4):
                print("Sorry, the number was 6. Your number was too low. You lost.")
            else:
                print("Sorry, the number was 6. Your number was too high. You lost.")
            break



while True:
    answer = input("Would you like to play a guessing game?:")
    if (answer == "yes"):
        guessing_game()

    else:
        break



    




