from abc import ABC, abstractmethod


class Knowledge(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def learn(self):
        pass

class Nothing(Knowledge):
    def play(self):
        print("I don't know anything yet")
        return self.learn()

    def learn(self):
        new_thing = input("What were you thinking of? ")
        print("Yay, I learned something new!")
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

        return Question(new_question, self, Answer(new_answer))

class Question(Knowledge):
    def __init__(self, question, yes, no):
        self.question = question
        self.yes = yes
        self.no = no

    def play(self):
        new_answer1 = input(self.question + " Answer with a Y or N. ")
        if new_answer1 == "Y":
            print("Aren't I smart?")
            return self
        else:
            new_answer2 = input(self.no.answer + "Answer with a Y or N. ")
            if new_answer2 == 'Y':
                print("Aren't I smart?")
                return self
            else:
                self.learn()

    def learn(self):
        new_answer = input("What were you thinking of? ")
        new_question = input("What's a yes/no question I can use to distinguish between %s and %s? " % (self.no.answer,
                                                                                                        new_answer))

        return Question(new_question, self, Answer(new_answer))


if __name__ == "__main__":
    kb = Nothing()
    while True:
        input("Ready to play 20 Qs? Think of something and I'll guess it. Press Enter when ready.")
        kb = kb.play()
