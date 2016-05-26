# It is another word game, which is called word guessing.

import random

print("""
Hello, This is a game that make you to guess words of fruits.
the machine will give you a hint of how many word you are trying
to guess. if you are right, it also will show you what position
you guess right.

ok, try it!
""")

ans_list=['pineapple','watermellon','peach','grape','gamania','guava']

def game():
    ans_word= random.choice(ans_list)
    correctList=[]
    wrongList=[]
    
    while len(wrongList)<5 and len(correctList) != len(list(ans_word)):
        for word in ans_word:
            if word in correctList:
                print(word, end='')
            elif word not in correctList:
                print('_',end='')
        print("")
        print("{}/5 to failed".format(len(wrongList)))
        print("")


        guess= input("please try to guess. \n >" ).lower()
        if len(guess) != 1:
            print("You can only guess one word each time.")
            continue
        elif guess in correctList or guess in wrongList:
            print("You have guessed that already")
            continue
        elif not guess.isalpha:
            print("You can only guess a letter.")
            continue

        if guess in ans_word:
            correctList.append(guess)
            if len(correctList)==len(ans_word):
                print("Congrat! You win!")
                return start
        else:
            wrongList.append(guess)
    else:
        print("Sorry, You lose. Answer is {}".format(ans_word))
        return start
                  
            
    
start=input("Are you ready (Y/n)?").lower()
if start !='n':
    game()
