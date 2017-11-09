'''
Jacob Knecht
Prof. Ordonez
CPTR-215
11/02/17
WarmUp 10
'''
class Fraction:
    def __init__(self, *args):
        if len(args) == 0:
            self.numer, self.denom = 0, 1
        elif type(args[0]) == str:
            self.numer, self.denom = [int(piece) for piece in args[0].split("/")]
        elif len(args) == 1 and type(args[0]) == int:
            self.numer, self.denom = args[0], 1
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            self.numer, self.denom = args
        else:
            print("Get better at writing, scrub")
        self.normalize_sign()
        self.__simplify()

    def __simplify(self):
        '''

        >>> Fraction(-3,-6)
        Fraction(1, 2)
        >>> Fraction("-7/49")
        Fraction(-1, 7)
        >>> Fraction(5, 7)
        Fraction(5, 7)
        '''
        GCD = self.__compute_GCD()
        self.numer = self.numer // GCD
        self.denom = self.denom // GCD

    def __compute_GCD(self):
        '''
        Code came from https://www.programiz.com/python-programming/examples/hcf
        It is the Euclidean algorithm
        >>> Fraction(-3,-6)
        Fraction(1, 2)
        >>> Fraction("-7/49")
        Fraction(-1, 7)
        >>> Fraction(5, 7)
        Fraction(5, 7)

        '''
        x = self.numer
        y = self.denom
        while(y):
            x,y = y, x%y
        return x

    def normalize_sign(self):
        '''
        >>> Fraction(-3,-6)
        Fraction(1, 2)
        >>> Fraction("-7/49")
        Fraction(-1, 7)
        >>> Fraction(5, -7)
        Fraction(-5, 7)
        >>> Fraction(-2, -3)
        Fraction(2, 3)
        '''
        if self.denom < 0:
            self.denom, self.numer = -self.denom, -self.numer

    def __repr__(self):
        '''
        >>> Fraction(-3,-6)
        Fraction(1, 2)
        >>> Fraction("-7/49")
        Fraction(-1, 7)
        >>> Fraction(5, -7)
        Fraction(-5, 7)
        >>> Fraction(-2, -3)
        Fraction(2, 3)
        '''
        return "Fraction(%d, %d)" % (self.numer, self.denom)

    def __str__(self):
        '''
        >>> print(Fraction(1,2))
        1/2
        >>> print(Fraction(-5, 7))
        -5/7
        '''
        return "%d/%d" % (self.numer, self.denom)

    def __add__(self, other):
        '''

        >>> Fraction(1,2) + Fraction(-5, 7)
        Fraction(-3, 14)
        >>> Fraction(-8,-12) + Fraction(6, -3)
        Fraction(-4, 3)
        '''
        return Fraction(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        '''
        >>> Fraction(1,2) - Fraction(-5, 7)
        Fraction(17, 14)
        >>> Fraction(-8,-12) - Fraction(6, -3)
        Fraction(8, 3)
        '''
        return Fraction(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        '''
        >>> Fraction(1,2) * Fraction(-5, 7)
        Fraction(-5, 14)
        >>> Fraction(-8,-12) * Fraction(6, -3)
        Fraction(-4, 3)
        '''
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        '''
        >>> Fraction(1,2) / Fraction(-5, 7)
        Fraction(-7, 10)
        >>> Fraction(-8,-12) / Fraction(6, -3)
        Fraction(-1, 3)
        '''
        return Fraction(self.numer * other.denom, self.denom * other.numer)

    def __eq__(self, other):
        '''
        >>> Fraction(1,2) == Fraction(1, 2)
        True
        >>> Fraction(-8,-12) == Fraction(6, -3)
        False
        '''
        return str(self) == str(other)

    def __ne__(self, other):
        '''
        >>> Fraction(1,2) != Fraction(1, 2)
        False
        >>> Fraction(-8,-12) != Fraction(6, -3)
        True
        '''
        return str(self) != str(other)

    def __gt__(self, other):
        '''
        >>> Fraction(1,2) > Fraction(1, 2)
        False
        >>> Fraction(-8,-12) > Fraction(6, -3)
        True
        '''
        newSelf, newOther = self.common_denom(other)
        return newSelf > newOther

    def __lt__(self, other):
        '''
        >>> Fraction(1,2) < Fraction(1, 2)
        False
        >>> Fraction(-8,-12) < Fraction(6, -3)
        False
        '''
        return not self > other and not self == other

    def __ge__(self, other):
        '''
        >>> Fraction(1,2) >= Fraction(1, 2)
        True
        >>> Fraction(-8,-12) >= Fraction(6, -3)
        True
        '''
        newSelf, newOther = self.common_denom(other)
        return newSelf >= newOther

    def __le__(self, other):
        '''
        >>> Fraction(1,2) <= Fraction(1, 2)
        True
        >>> Fraction(-8,-12) <= Fraction(6, -3)
        False
        '''
        newSelf, newOther = self.common_denom(other)
        return newSelf <= newOther

    def common_denom(self, other):
        newSelfNumer = self.numer * other.denom
        newOtherNumer = other.numer * self.denom

        return newSelfNumer, newOtherNumer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
