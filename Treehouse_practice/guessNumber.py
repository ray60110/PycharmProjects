# here is a game be able to do:
# limit the number of guesses
# catch when someone guesses a non-integer
# print too low or too high message for bad guesses
# let people play again


import random


ans= random.randint(1,100)

def game():
        print("""
    Welcome to this competition.
    your job is to guess a number that matches our pre-selected one.
    you are able to guess a number from 0 to 100 for 5 times.

    GOOD LUCK!
    """)
        guess_times=[]
        while len(guess_times)<6:
            try:
                first_guess=input("> ")
                guess=int(first_guess)
            except ValueError:
                print("{} you just put is not an integer, please try again.".format(first_guess))

            else:
                guess_times.append(guess)
                
                if guess== ans:
                    print("Congrat!, you beat me! The answer is {}".format(ans))
                    break
                elif guess> ans:
                    print("Your guess is too high, guess lower than {}".format(guess))
                elif guess< ans:
                    print("Your guess is too low, guess higher than {}".format(guess))

        else:
            print("Oops! you didn't get it. My number is {} ".format(ans))
        play_again=input("Do you want to play again? (Y/n)")
        if play_again.lower() != "n":
            game()
        else:
            print("BYE!")
game()
 
