#Karl Kottman
#CTC389
#Lab 7 - Lab 1&2 Review


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




    




