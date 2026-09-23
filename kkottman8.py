#Karl Kottman
#CTC 389
#Lab 8



def psychedelia():
    print("You've entered the psychedelic room where you find a turntable and the following three records:")

    print("1. 'Odessey and Oracle' by The Zombies")
    print("2. 'Magical Mystery Tour' by The Beatles")
    print("3. 'Are You Experienced' by Jimi Hendrix")

    psychalbum = int(input("Enter the number of the album you choose to play:"))

    if (psychalbum == 1):
        print("You're getting lost in the sound of The Zombies and can't get enought, especially of these three tracks:")

        print("1. 'Time of the Season'")
        print("2. 'Hung up on a Dream'")
        print("3. 'Maybe After He's Gone'")

        psychsong1 = int(input("Enter the number of the song you want to listen to on repeat:"))

        if (psychsong1 == 2):
            print("You've reached a dream-like state. Do you want to:")

            print("1. ...keep dreaming?")
            print("2. ...listen to more music?")
            print("3. ...wake up?")

            whatnext = int(input("Enter the number of your choice:"))

            if (whatnext == 2):
                print("Great! What song will you listen to next?")

                print("1. 'The End' by The Doors")
                print("2. 'In-A-Gadda-Da-Vida' by Iron Butterfly")
                print("3. 'Shangri-la' by The Kinks")

                finalsong = int(input("Enter the number of your song choice:"))

                if (finalsong == 1):
                    print("This song is too long! Sadly, you can't finish your musical odyssey,", name,".")

                elif (finalsong == 2):
                    print("This song is too long! Sadly, you can't finish your musical odyssey,", name,".")

                else:
                    print("Congratulations! You've reached Shangri-la and completed your musical odyessey! Enjoy your newfound enlightenment!")
            

            elif (whatnext == 1):
                print("You slept too long! Sadly, your musical odyessy is over,", name,".")

            else:
                print("You've awakened from your psychedelic experience and are ready for something new.")
                musical_odyssey()

        


        else:
            print("Listening to too much of The Zombies has turned you into a Zombie! Now you can't stop listening! Sadly, your musical odyssey has come to a premature end,", name,".")

        

    elif (psychalbum == 2):
        print("You love the mystery tour! Which song will you repeat?")

        print("1. 'I Am the Walrus'")
        print("2. 'Blue Jay Way'")
        print("3. 'Strawberry Fields Forever'")

        psychsong2 = int(input("Enter the number of the song you want to repeat:"))

        if (psychsong2 == 1):
            print("You've turned into a walrus! Sadly, you can't finish your musical odyssey like this,", name,"!")
        
        else:
            print("Excellent choice! But now it's time to try listening to something different.")
            punk()

    elif (psychalbum == 3):
        print("You're experienced now! Which song do you want to hear again?")

        print("1. 'Purple Haze'")
        print("2. 'Hey Joe'")
        print("3. 'The Wind Cries Mary'")

        psychsong3 = int(input("Enter the number of the song you want to repeat:"))

        if (psychsong3 == 1):
            print("You got lost in the haze and have to start over.")
        else:
            print("Excellent choice! But now it's time to try listening to something different.")
            newwave()


def punk():
    print("You've entered a disheveled room with a turntable and the following three records:")

    print("1. 'Operation Ivy' by Operation Ivy")
    print("2. 'Legacy of Brutality' by Misfits")
    print("3. 'Bedtime for Democracy' by Dead Kennedys")

def newwave():
    print("You've entered a neon room with a turntable and the following three records:")

    print("1. 'Low-Life' by New Order")
    print("2. 'Kiss Me, Kiss Me, Kiss Me' by the Cure")
    print("3. 'I Just Can't Stop It' by the Beat")

            
def musical_odyssey():
    print("Before you are three doors named as follows:")

    print("1. Psychedelia")
    print("2. Punk")
    print("3. New Wave")

    choice1 = int(input("What number door will you enter?:"))

    if (choice1 == 1):
        psychedelia()



name = input("Welcome to the Land of Rock! What is your name?:")

print("Hello,", name,"! You are about to embark on a musical odyssey. To fully complete this experience, you must choose the right path forward. But there is only one path that will take you all the way, so choose wisely.")

while True:
    answer = input("Whether it's your first time or you're coming back for more, are you ready to embark on a musical odyssey?:")
    if (answer == "yes"):
        musical_odyssey()

    else:
        break



