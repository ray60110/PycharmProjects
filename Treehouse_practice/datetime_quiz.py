import random
import datetime

from datetime_question import Addon, Multiplied

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
        starttime= datetime.datetime.now()
        counts=0

        for i in range(10):
            print(self.question[i])
            student= input('\n Please submit your answer. >>>')
            if input is int():
                if student == self.answerlist[i]:
                    print('True')
                    self.summary.append(1)
                else:
                    print('False')
                    self.summary.append(0)
            else:
                print('Illegal answer, False')
                self.summary.append(0)
        endtime= datetime.datetime.now()

        for a in self.summary:
            counts+=a
        print('Your score: ')

        # log the start time
        # ask all of the question
        # log if they got the question right
        # log the end time
        # show a total summary

    def ask(self):
        pass
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer is right, send back True
        # otherwise, send back false
        # send back elapse time.

    def summary(self):
        print('You have {} out of {} right!'.format())
