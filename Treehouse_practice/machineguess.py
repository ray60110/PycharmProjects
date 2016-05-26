# This is the version 2 of the number game.
# We make computer to guess what the number is in our mind.

import random

guessed_item=[]
    
def game():
    a=0
    b=100
    while len(guessed_item)<5:

        guess= random.randint(a,b)
        print("I guess: "+ str(guess))
        confirm=input("Am I right? Human. (y/n)")

        if confirm.lower() =="y":
            print("HaHa! You are beaten by me, Human.")
            break
        else:
            guessed_item.append(guess)
        
        hint= input("Should I guess Higher or Lower? (H/L)")
        if hint.lower()=="h":
            a=guess
        elif hint.lower()=='l':
            b=guess
        else:
            print("Please provide the appropriate hint!")
            continue
    else:
        print("Congrat! you beat me! \n")
        replay=input("Do you want to play again? (Y/n)")
        if replay.lower() !='n':
            game()
        else:
            print("BYE")

print("""
Hello chalenger, you are stepping in a competition
that between you and the computer in front of you.
You have bear a number in your mind before the
machine start to guess. The number should be 0-100

Good Luck!
""")

ready= input("Have you had your number in mind? Y/n \n")
if ready.lower() != 'n':
    game()
else:
    quit()
