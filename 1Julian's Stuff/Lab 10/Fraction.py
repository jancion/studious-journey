'''
Julian Ancion
Prof. Ordonez
CPTR-215
11/02/17
'''
class Fraction:
    def __init__(self, *args):
        '''
        Initializes the class and determines the input
        :param args: the numerator and the denomerators
        >>> Fraction(1)
        Fraction(1, 1)

        >>> test = Fraction('-1/2')
        >>> print(test)
        -1/2
        '''
        if len(args) == 0:
            self.numer, self.denom = 0, 1

        elif type(args[0]) == str:
            self.numer, self.denom = [int(piece) for piece in args[0].split("/")]

        elif len(args) == 1 and type(args[0]) == int:
            self.numer, self.denom = args[0], 1

        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            self.numer, self.denom = args

        elif len(args) == 1 and type(args[0]) == float:
            self.numer = args[0] * 100
            self.denom = 100

        else:
            print('Please enter in one of the following formats')
            print('Fraction(.45')
            print('Fraction(1, 2)')
            print('Fraction(1/2')

        self.__simplify()


    def __gcd(self):
        '''
        Uses the Euclidean Algorithm
        determines greatest common denominator
        :param a: numerator
        :param b: denominator
        :return: simplified fraction
        >>> Fraction(2, 4)
        Fraction(1, 2)
        >>> Fraction(6, 12)
        Fraction(1, 2)
        '''
        b = self.denom
        a = self.numer
        while b:
            a, b = b, a % b
        return a

    def __simplify(self):
        '''
        Simplifies fractions
        :return: simplified fraction
        >>> test = Fraction('2/4')
        >>> print(test)
        1/2
        >>> test = Fraction('3/9')
        >>> print(test)
        1/3
        '''

        denom = self.denom
        numer = self.numer
        if denom == 0:
            return "0"
        common_divisor = self.__gcd()
        reduced_numer = numer / common_divisor
        reduced_denom = denom / common_divisor

        if self.numer == self.denom:
            self.numer = 1
            self.denom = 1
        elif reduced_denom == 1:
            return reduced_numer, denom
        elif common_divisor == 1:
            self.numer, self.denom = numer, denom
        else:
            self.numer, self.denom = reduced_numer, reduced_denom

    def __repr__(self):
        '''
        Returns a string that, when evaluated, creates an identical object.
        :return: the properly formatted string
        >>> Fraction('1/2')
        Fraction(1, 2)
        >>> Fraction('-1/2')
        Fraction(-1, 2)
        '''
        if self.numer < 0 and self.denom > 0:
            return "Fraction(%d, %d)" % (self.numer, self.denom)
        elif self.numer < 0 and self.denom < 0:
            return "Fraction(%d, %d)" % (-self.numer, -self.denom)
        else:
            return "Fraction(%d, %d)" % (self.numer, self.denom)

    def __str__(self):
        '''
        Used when called into a string setting such as print
        :return: simple formatted string containing the fraction
        >>> print(Fraction(1, 2))
        1/2
        >>> print(Fraction(-1, 2))
        -1/2
        '''
        return "%d/%d" % (self.numer, self.denom)

    def __add__(self, other):
        '''
        adds two fractions together
        :param other: the second fraction
        :return: combined fractions
        >>> Fraction('1/2') + Fraction('2/3')
        Fraction(7, 6)
        >>> Fraction(1, 2) + Fraction(1, 2)
        Fraction(1, 1)
        '''
        return Fraction(self.numer * other.denom + self.denom * other.numer, \
                        self.denom * other.denom)

    def __sub__(self, other):
        '''
        subtracts two seperate fractions
        :param other: the second fraction
        :return: a reduced fraction
        >>> Fraction(1,2) - Fraction(1,2)
        Fraction(0, 2)
        >>> Fraction(3,4) - Fraction(1,2)
        Fraction(1, 4)
        '''
        if self.denom == other.denom:
            return Fraction(self.numer - other.numer, self.denom)
        else:
            numer1 = self.numer * other.denom
            denom1 = self.denom * other.denom
            numer2 = other.numer * self.denom

            return Fraction(numer1 - numer2, denom1)

    def __mul__(self, other):
        '''
        multiplies two seperate fractions
        :param other: the second fraction
        :return: the product of the two fractions
        >>> Fraction(1, 2) * 2
        Fraction(1, 1)
        >>> Fraction(1, 2) * Fraction(1, 2)
        Fraction(1, 4)
        '''
        if type(other) == Fraction:
            return Fraction(self.numer * other.numer, \
                        self.denom * other.denom)
        else:
            return Fraction(self.numer * other, self.denom)

    def __eq__(self, other):
        '''
        compares two seperate fractions
        :param other:
        :return:
        >>> Fraction(1, 2) == Fraction('1/2')
        True
        >>> Fraction(1) == Fraction(1, 2)
        False
        '''
        numer1 = self.numer
        numer2 = other.numer
        denom1 = self.denom
        denom2 = other.denom
        if numer1 == numer2 and denom1 == denom2:
            return True
        else:
            return False

    def __truediv__(self, other):
        '''
        returns a divided fraction
        :param other: second fraction
        :return: divided fraction
        >>> Fraction(1, 2) / Fraction('1/2')
        Fraction(1, 1)
        >>> Fraction(1, 2) / Fraction(3, 4)
        Fraction(2, 3)
        '''
        numer2 = other.numer
        denom2 = other.denom
        return Fraction(self.numer * denom2, self.denom * numer2)

    def __ne__(self, other):
        '''
        Determines if two fractions are not equal
        :param other: second fraction
        :return: True or False
        >>> Fraction(1,2) != Fraction(2,3)
        True
        >>> Fraction(1,2) != Fraction(1,2)
        False
        '''
        one = False
        two = False
        if self.numer == other.numer:
            one = True
        if self.denom == other.denom:
            two = True
        if one == True and two == True:
            return False
        else:
            return True

    def __lt__(self, other):
        '''
        Checks if fraction is less than other fraction
        :param other: second fraction
        :return: True or false
        >>> Fraction(1, 2) < Fraction(1, 3)
        False
        >>> Fraction(1, 3) < Fraction(1, 2)
        True
        '''
        numer1 = self.numer * other.denom
        numer2 = other.numer * self.denom

        return numer1 < numer2

    def __le__(self, other):
        '''
        Determines if one fraction is less than or equal a second fraction
        :param other: second fraction
        :return: True or false
        >>> Fraction(1, 3) <= Fraction(1, 3)
        True
        >>> Fraction(1, 2) <= Fraction(1, 4)
        False
        '''
        numer1 = self.numer * other.denom
        numer2 = other.numer * self.denom

        return numer1 <= numer2

    def __gt__(self, other):
        '''
        Determines if one fraction is greater than a second fraction
        :param other: Second Fraction
        :return: True or False
        >>> Fraction(1, 2) > Fraction(1, 3)
        True
        >>> Fraction(1, 3) > Fraction(1, 2)
        False
        '''
        numer1 = self.numer * other.denom
        numer2 = other.numer * self.denom

        return numer1 > numer2

    def __ge__(self, other):
        '''
        Determines if one fraction is greater than or equal to a second fraction
        :param other: Second Fraction
        :return: True or False
        >>> Fraction(1, 2) >= Fraction(1, 2)
        True
        >>> Fraction(1, 3) >= Fraction(1, 2)
        False
        '''
        numer1 = self.numer * other.denom
        numer2 = other.numer * self.denom

        return numer1 >= numer2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    fracZero = Fraction()
    fracOne = Fraction(1)
    fracHalf = Fraction(1, 2)
    fracTwoThirds = Fraction("1/3")
    fracThreeSixths = Fraction(3, 6)
    frac45hundredths = Fraction(0.45)
    print("%s + %s = %s" % (fracHalf, fracTwoThirds, fracHalf + fracTwoThirds))
    print("%s - %s = %s" % (fracHalf, fracTwoThirds, fracHalf - fracTwoThirds))
    print("%s * %s = %s" % (fracHalf, fracTwoThirds, fracHalf * fracTwoThirds))
    print("%s / %s = %s" % (fracHalf, fracTwoThirds, fracHalf / fracTwoThirds))
    if Fraction(2) == Fraction(2):
        print("Exact results achieved")
    else:
        print("You might as well use floats")
    print(fracThreeSixths)
    print(frac45hundredths)
    print(fracOne != frac45hundredths)
    print(fracOne == fracOne)
    print(fracOne)
    print(fracOne < fracHalf)
