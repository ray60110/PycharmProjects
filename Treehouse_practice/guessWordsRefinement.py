# It is another word game, which is called word guessing.

import random
import os
import sys

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(correctList, wrongList, ans_word):
    clear()

    print("You are mistaken {}/5 times".format(len(wrongList)))
    print('')

    for letter in wrongList:
        print(letter, end=' ')
    print("\n\n")

    for letter in ans_word:
        if letter in correctList:
            print(letter,end=' ')
        else:
            print('_', end=' ')
    print('\n')

def get_guess(correctList, wrongList):
    while True:
        guess= input("please try to guess. \n >" ).lower()
        if len(guess) != 1:
            print("You can only guess one word each time.")
        elif guess in correctList or guess in wrongList:
            print("You have guessed that already")
        elif not guess.isalpha:
            print("You can only guess a letter.")
        else:
            return guess

def play(done=False):
    clear()
    ans_word= random.choice(ans_list)
    correctList=[]
    wrongList=[]

    
    while True:
        draw(correctList, wrongList, ans_word)
        guess= get_guess(correctList, wrongList)

        if guess in ans_word:
            correctList.append(guess)
            found= True
            for letter in ans_word:
                if letter not in correctList:
                    found=False
            if found:
                print("You Beat Me! Congratulation!")
                print("The secret word is {}.".format(ans_word))
                done= True
        if guess not in ans_word:
            wrongList.append(guess)
            if len(wrongList) == 5:
                draw(correctList, wrongList, ans_word)
                print("I am sorry, you are losed!.")
                print("The answer is {}.".format(ans_word))
                done= True
        
        if done:
            playgame= input("Want to play again? (Y/n)").lower()
            if playgame != 'n':
                return play(done=False)
            else:
                sys.exit()
 
def welcome():
    start= input("Please press Enter/Return to start this game or Q to exit.").lower()
    if start != 'q':
        play(done)
    else:
        sys.exit()

    
print("""
Hello! Welcome to Ray's Python Game!
This is a game that make you to guess words of fruits.
the machine will give you a hint of how many word you are trying
to guess. if you are right, it also will show you what position
you guess right.

ok, try it!
""")

ans_list=['pineapple','watermellon','peach','grape','gamania','guava', 'avocado', 'blueberry', 'lychee', 'papaya',
          ' nectarine', 'passionfruit', 'raspberry', 'quince', 'fig', 'coconut', 'apricot']


done=False
while True:
    clear()
    welcome()

