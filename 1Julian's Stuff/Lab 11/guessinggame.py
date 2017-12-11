'''
Jacob Knecht
Prof. Ordonez
CPTR-215
11/16/17
Guessing Game Lab 11
'''
from abc import ABC


class Knowledge(ABC):
    def play(self):
        pass

    def learn(self):
        pass

class Nothing(Knowledge):
    def play(self):
        print("I don't know anything yet")
        return self.learn()

    def learn(self):
        new_thing = input("What were you thinking of? ")
        return Answer(new_thing)

class Answer(Knowledge):
    def __init__(self, answer):
        self.answer = answer

    def play(self):
        y_or_n = input("Were you thinking of %s (enter only Y or N)? " % self.answer)
        if y_or_n == "Y":
            print("Aren't I smart?")
            return self
        else:
            return self.learn()

    def learn(self):
        new_answer = input("What were you thinking of? ")
        new_question = input("What's a yes/no question I can use to distinguish between %s and %s? " % (self.answer, new_answer))
        connect_Q2A = input("When I ask %s, does it belong to %s? (Answer with Y or N) " % (new_question, new_answer))
        if connect_Q2A == 'Y':
            return Question(new_question, Answer(new_answer), self)
        else:
            return Question(new_question, self, Answer(new_answer))

class Question(Knowledge):
    def __init__(self, question, yes, no):
        self.question = question
        self.yes = yes
        self.no = no

    def play(self):
        new_answer1 = input(self.question + " Answer with a Y or N. ")
        if new_answer1 == "Y":
            return Question(self.question, self.yes.play(), self.no)
        else:
            return Question(self.question, self.yes, self.no.play())



if __name__ == "__main__":
    kb = Nothing()
    while True:
        input("Ready to play 20 Qs? Think of something and I'll guess it. Press Enter when ready.")
        kb = kb.play()
