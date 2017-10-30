from random import shuffle
class SetCard:
    '''Creates the cards and class'''
    NUMBERS = (1, 2, 3)
    COLORS = tuple('RGP')
    SHAPES = tuple('DST')
    FILLS = tuple('FES')

    def __init__(self, number, color, shape, fill):
        # number in (1, 2, 3)
        # color in "RGP"
        # shape in "DOS"
        # fill in (0, 1, 2) (Filled, Empty, Striped)
        self.number = number
        self.color = color
        self.shape = shape
        self.fill = fill


    def find_third_card(self, card2):
        global card3
        card3 = ''
        number = '123'
        color = "RGP"
        shape = "TCS"
        fill = '012'
        if self.number == card2.number:
            card3 += str(self.number)
        else:
            number = number.replace(str(self.number), '')
            number = number.replace(str(card2.number), '')
            card3 += number
        if self.color == card2.color:
            card3 += self.color
        else:
            color = color.replace(self.color, "")
            color = color.replace(card2.color, '')
            card3 += color
        if self.shape == card2.shape:
            card3 += self.shape
        else:
            shape = shape.replace(self.shape, '')
            shape = shape.replace(card2.shape, '')
            card3 += shape
        if self.fill == card2.fill:
            card3 += str(self.fill)
        else:
            fill = fill.replace(str(self.fill), '')
            fill = fill.replace(str(card2.fill), '')
            card3 += fill
        return SetCard(card3[0], card3[1], card3[2], card3[3])


    def makes_set_with(self, card2, card3):
        return all_same_or_different(self.number, card2.number, card3.number) and \
               all_same_or_different(self.color, card2.color, card3.color) and \
               all_same_or_different(self.shape, card2.shape, card3.shape) and \
               all_same_or_different(self.fill, card2.fill, card3.fill)

    def __str__(self):
        return "%s%s%s%s" % (self.number, self.color, self.shape, self.fill)

    def __repr__(self):
        return "SetCard(%s, '%s', '%s', %s)" % (self.number, self.color, self.shape, self.fill)
    def draw(self):
        import turtle
        card = turtle.Turtle()
        card.speed(0)
        card.hideturtle()
        #check color
        if self.color == 'R':
            card.color('Red')
        if self.color == 'G':
            card.color('Green')
        if self.color == 'P':
            card.color('Pink')

        for x in range(int(self.number)):

            #draw shape
            if self.shape == 'S':
                if self.fill == '0':
                    card.begin_fill()
                card.down()
                card.forward(50)
                card.right(90)  # Rotate clockwise by 90 degrees
                card.forward(50)
                card.right(90)
                card.forward(50)
                card.right(90)
                card.forward(50)
                card.right(90)
                if self.fill == '2':
                    card.forward(10)
                    for x in range(2):
                        card.right(90)
                        card.forward(50)
                        card.left(90)
                        card.forward(10)
                        card.left(90)
                        card.forward(50)
                        card.right(90)
                        card.forward(10)
                    card.up()
                    card.forward(50)
                card.up()
                if self.fill == '0':
                    card.end_fill()
                    card.forward(100)

            if self.shape == 'C':
                if self.fill == '0':
                    card.begin_fill()
                card.down()
                for x in range(60):
                    card.forward(4)
                    card.right(6)
                if self.fill == '2':
                    for x in range(15):
                        card.forward(4)
                        card.right(6)
                    card.right(90)
                    card.forward(76)
                    card.left(90)
                    card.up()
                    card.forward(10)
                    card.left(90)
                    card.forward(1)
                    card.down()
                    card.forward(74)
                    card.up()
                    card.right(90)
                    card.forward(10)
                    card.right(90)
                    card.forward(4)
                    card.down()
                    card.forward(68)
                    card.left(90)
                    card.up()
                    card.forward(10)
                    card.left(90)
                    card.forward(9)
                    card.down()
                    card.forward(54)
                    card.up()
                    card.forward(11)
                    card.left(90)
                    card.forward(40)
                    card.left(90)
                    card.forward(2)
                    card.down()
                    card.forward(74)
                    card.up()
                    card.right(90)
                    card.forward(10)
                    card.right(90)
                    card.forward(6)
                    card.down()
                    card.forward(62)
                    card.left(90)
                    card.up()
                    card.forward(10)
                    card.left(90)
                    card.forward(12)
                    card.down()
                    card.forward(42)
                    card.up()
                    card.right(90)
                    card.forward(6)
                    card.right(90)
                card.up()
                card.forward(125)
                if self.fill == '0':
                    card.end_fill()
            if self.shape == 'T':
                if self.fill == '0':
                    card.begin_fill()
                card.down()
                card.right(120)
                card.forward(50)
                card.right(120)
                card.forward(50)
                card.right(120)
                card.forward(50)

                if self.fill == '2':
                    card.right(120)
                    card.forward(40)
                    card.right(120)
                    card.forward(40)
                    card.right(120)
                    card.forward(10)
                    card.right(60)
                    card.forward(30)
                    card.left(120)
                    card.forward(10)
                    card.left(60)
                    card.forward(20)
                    card.right(120)
                    card.forward(10)
                    card.right(60)
                    card.forward(10)
                    card.left(120)
                    card.forward(10)
                    card.right(60)
                    card.up()
                    card.forward(75)

                card.up()
                if self.fill == '0':
                    card.end_fill()
                    card.forward(75)
        turtle.done()





def all_same_or_different(thing1, thing2, thing3):
    return (thing1 == thing2 and thing2 == thing3) or \
           (thing1 != thing2 and thing2 != thing3 and thing3 != thing1)

def setDeck():
    deck = []
    for number in ('1', '2', '3'):
        for color in "RGP":
            for shape in "TCS":
                for fill in ('0', '1', '2'):
                    deck += [SetCard(number, color, shape, fill)]
    return deck
deck = setDeck()
shuffle(deck)
card1 = deck[0]
card2 = deck[1]
card3 = card1.find_third_card(card2)
card3.draw()