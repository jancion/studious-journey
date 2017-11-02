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
        GCD = self.compute_GCD()
        self.numer = self.numer // GCD
        self.denom = self.denom // GCD

    def compute_GCD(self):
        '''
        Give two numbers, returns GCD

        :return:
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
        >>> Fraction(5, 7)
        Fraction(5, 7)
        '''
        if self.denom < 0:
            self.denom, self.numer = -self.denom, -self.numer

    def __repr__(self):
        """Returns a string that, when evaluated, creates an identical object."""
        return "Fraction(%d, %d)" % (self.numer, self.denom)

    def __str__(self):
        return "%d/%d" % (self.numer, self.denom)

    def __add__(self, other):
        return Fraction(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Fraction(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Fraction(self.numer * other.denom, self.denom * other.numer)

    def __eq__(self, other):
        return self.numer / self.denom == other.numer / other.denom

    def __ne__(self, other):
        return self.numer / self.denom != other.numer / other.denom

    def __gt__(self, other):
        return self.numer / self.denom > other.numer / other.denom

    def __lt__(self, other):
        return self.numer / self.denom < other.numer / other.denom

    def __ge__(self, other):
        return self.numer / self.denom >= other.numer / other.denom

    def __le__(self, other):
        return self.numer / self.denom <= other.numer / other.denom




if __name__ == "__main__":
    import doctest

    doctest.testmod()
    fracZero = Fraction()
    fracOne = Fraction(1)
    fracHalf = Fraction(1, 2)
    fracTwoThirds = Fraction("2/3")
    # frac45hundredths = Fraction(0.45)
    print("%s + %s = %s" % (fracHalf, fracTwoThirds, fracHalf + fracTwoThirds))
    # print("%s - %s = %s" % (fracHalf, fracTwoThirds, fracHalf - fracTwoThirds))
    # print("%s * %s = %s" % (fracHalf, fracTwoThirds, fracHalf * fracTwoThirds))
    # print("%s / %s = %s" % (fracHalf, fracTwoThirds, fracHalf / fracTwoThirds))
    if fracTwoThirds * Fraction(3) == Fraction(2):
        print("Exact results achieved")
    else:
        print("You might as well use floats")