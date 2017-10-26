'''
Julian Ancion
Prof. Ordonez
CPTR-215-A
10/19/2017
SetCards.py
'''
import turtle

class SetCard:
    '''Creates the card class objects'''
    def __init__(self, number, color, shape, fill):
        self.number = number
        self.color = color
        self.shape = shape
        self.fill = fill

    def drawcard(self):
        '''
        draws card using turtle graphics
        :return:
        '''
        colordict= {
            'R':'Red',
            'B':'Blue',
            'G':'Green'
        }
        smart = turtle.Turtle()
        smart.speed(0)
        smart.hideturtle()
        for i in range(int(self.number)):

            if self.shape == 'S':
                if self.fill == 'F':
                    smart.begin_fill()
                smart.down()
                smart.color(colordict[self.color])
                for i in range(4):
                    smart.forward(50)
                    smart.right(90)

                if self.fill == 'S':
                    smart.forward(10)
                    for i in range(2):
                        smart.right(90)
                        smart.forward(50)
                        smart.left(90)
                        smart.forward(10)
                        smart.left(90)
                        smart.forward(50)
                        smart.right(90)
                        smart.forward(10)
                    smart.up()
                    smart.forward(50)
                smart.up()
                if self.fill == 'F':
                    smart.end_fill()
                    smart.forward(100)

            if self.shape == 'T':
                if self.fill == 'F':
                    smart.begin_fill()
                smart.down()
                smart.color(colordict[self.color])
                for i in range(3):
                    smart.right(120)
                    smart.forward(50)

                if self.fill == 'S':
                    smart.right(120)
                    smart.forward(40)
                    smart.right(120)
                    smart.forward(40)
                    smart.right(120)
                    smart.forward(10)
                    smart.right(60)
                    smart.forward(30)
                    smart.left(120)
                    smart.forward(10)
                    smart.left(60)
                    smart.forward(20)
                    smart.right(120)
                    smart.forward(10)
                    smart.right(60)
                    smart.forward(10)
                    smart.left(120)
                    smart.forward(10)
                    smart.right(60)
                    smart.up()
                    smart.forward(75)

                smart.up()
                if self.fill == 'F':
                    smart.end_fill()
                    smart.forward(75)

            if self.shape == 'C':
                if self.fill == 'F':
                    smart.begin_fill()
                smart.down()
                smart.color(colordict[self.color])
                for i in range(60):
                    smart.forward(4)
                    smart.right(6)

                if self.fill == 'S':
                    for i in range(15):
                        smart.forward(4)
                        smart.right(6)
                    smart.right(90)
                    smart.forward(76)
                    smart.left(90)
                    smart.up()
                    smart.forward(10)
                    smart.left(90)
                    smart.forward(1)
                    smart.down()
                    smart.forward(74)
                    smart.up()
                    smart.right(90)
                    smart.forward(10)
                    smart.right(90)
                    smart.forward(4)
                    smart.down()
                    smart.forward(68)
                    smart.left(90)
                    smart.up()
                    smart.forward(10)
                    smart.left(90)
                    smart.forward(9)
                    smart.down()
                    smart.forward(54)
                    smart.up()
                    smart.forward(11)
                    smart.left(90)
                    smart.forward(40)
                    smart.left(90)
                    smart.forward(2)
                    smart.down()
                    smart.forward(74)
                    smart.up()
                    smart.right(90)
                    smart.forward(10)
                    smart.right(90)
                    smart.forward(6)
                    smart.down()
                    smart.forward(62)
                    smart.left(90)
                    smart.up()
                    smart.forward(10)
                    smart.left(90)
                    smart.forward(12)
                    smart.down()
                    smart.forward(42)
                    smart.up()
                    smart.right(90)
                    smart.forward(6)
                    smart.right(90)
                smart.up()
                smart.forward(125)

                if self.fill == 'F':
                    smart.end_fill()


        turtle.done()
    def find_third_card(self, card2):
        '''
        Checks the self card againts a second card to determine the third card and then outputs the third card into the SetCard method
        :param card2:
        :return:
        '''
        num = '123'
        color = 'RGB'
        shape = 'SCT'
        fill = 'FES'


        c1_num = self.number
        c1_color = self.color
        c1_shape = self.shape
        c1_fill = self.fill
        c2_num = card2.number
        c2_color = card2.color
        c2_shape = card2.shape
        c2_fill = card2.fill

        for i in num:
            if c1_num == c2_num:
                num = c1_num
            elif i == c1_num or i == c2_num:
                num = num.replace(i, '')
        for i in color:
            if c1_color == c2_color:
                color = c1_color
            elif i == c1_color or i == c2_color:
                color = color.replace(i, '')
        for i in shape:
            if c1_shape == c2_shape:
                shape == c2_shape
            elif i == c1_shape or i == c2_shape:
                shape = shape.replace(i, '')
        for i in fill:
            if c1_fill == c2_fill:
                fill = c1_fill
            elif i == c1_fill or i == c2_fill:
                fill = fill.replace(i, '')
        #print('SetCard(' + num + ',', + shape + ',', + )
        return SetCard(num, color, shape, fill)




    def makes_set_with(self, card2, card3):
        '''
        checks if the three cards are a set.
        :param card2:
        :param card3:
        :return:
        '''
        return all_same_or_different(self.number, card2.number, card3.number) and \
               all_same_or_different(self.color, card2.color, card3.color) and \
               all_same_or_different(self.shape, card2.shape, card3.shape) and \
               all_same_or_different(self.fill, card2.fill, card3.fill)

    def __str__(self):
        return "%s%s%s%s" % (self.number, self.color, self.shape, self.fill)

    def __repr__(self):
        return "SetCard(%s, '%s', '%s', %s)" % (self.number, self.color, self.shape, self.fill)


def all_same_or_different(thing1, thing2, thing3):
    return (thing1 == thing2 and thing2 == thing3) or \
           (thing1 != thing2 and thing2 != thing3 and thing3 != thing1)


card1 = SetCard('3', 'G', 'C', 'S')
card2 = SetCard('3', 'R', 'T', 'F')
card3 = SetCard('3', 'B', 'S', 'E')



deck = []
for number in (1, 2, 3):
    for color in "RGP":
        for shape in "DOS":
            for fill in (0, 1, 2):
                deck += [SetCard(number, color, shape, fill)]
card4 = card1.find_third_card(card3)
if card1.makes_set_with(card2, card3):
    print("That's a set!")
else:
    print("Not a set!")

print(card4)
card4.drawcard()
