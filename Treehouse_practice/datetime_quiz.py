import random
import datetime

from datetime_question import Addon
from datetime_question import Multiplied


class Quiz:
    question= []
    answerlist= []
    summary=[]


    def __init__(self):
        while len(self.question)<11:
            num1, mark, num2= random.randint(1,10), random.choice(['+', '*']), random.randint(1,10)
            self.text= '{}{}{}'.format(num1, mark, num2)
            self.question.append(self.text)
            if mark =='*':
                self.answer= num1*num2
                self.answerlist.append(self.answer)
            else:
                self.answer=num1+num2
                self.answerlist.append(self.answer)

        # to gernate 10 random questions with number from 1 to 10
        # add these numbers into self.question


    def take_quiz(self):



        # log the start time
        # ask all of the question
        # log if they got the question right
        # log the end time
        # show a total summary

    def ask(self, Question):


        # capture the answer

        # check the answer
        # log the end time
        # if the answer is right, send back True
        # otherwise, send back false
        # send back elapse time.

    def summary(self):
        # To print out how many question you have submit and correct.
        print('You have {} out of {} right!'.format(self.totalcorrect(), len(self.summary)))
        print('It seems to took you {} to finish them.'.format())
