'''
Julian Ancion
Prof. Ordonez
Guessing Game
'''
"""A List is either:
- Empty (contains nothing), or
- a Node that contains a number and a List"""


class List:
    '''
    List section created by Prof. Ordonez
    '''
    def __init__(self):
        print("Don't call us, we won't call you!")

    def sum(self):
        return "Don't call us, we won't call you!"

    def __len__(self):
        return "Don't call us, we won't call you!"

    def __contains__(self, item):
        return "Don't call us, we won't call you!"

    def __add__(self, other):
        return "Don't call us, we won't call you!"

    def max(self):
        return "Don't call us, we won't call you!"

    def min(self):
        return "Don't call us, we won't call you!"

    def __sub__(self, other):
        return "Don't call us, we won't call you!"

    def all_even(self):
        return "Don't call us, we won't call you!"

    def all_odd(self):
        return "Don't call us, we won't call you!"





class Empty(List):
    '''
    for dealing with the empty nodes at the end of linked-lists.
    '''
    def __init__(self):
        pass

    def __repr__(self):
        return "Empty()"

    def __str__(self):
        return "End"

    def sum(self):
        return 0

    def __add__(self, second):
        if type(second) == int:
            return Node(second, Empty())
        else:
            return second

    def __len__(self):
        return 0

    def __contains__(self, item):
        return False

    def max(self):
        return float("-Inf")

    def min(self):
        return float("Inf")

    def __sub__(self, other):
        return self

    def all_even(self):
        return True

    def all_odd(self):
        return True


class Node(List):
    def __init__(self, data, rest_of_list):
        self.data = data
        self.rest = rest_of_list

    def __repr__(self):
        return "Node(%s, %r)" % (self.data, self.rest)

    def __str__(self):
        return "%s, %s" % (self.data, self.rest)

    def sum(self):
        return self.data + self.rest.sum()

    def __add__(self, other):
        '''Returns a new list with other appended to the end of self
        >>> Empty() + Empty()
        Empty()
        >>> Node(1, Node(2, Empty())) + Empty()
        Node(1, Node(2, Empty()))
        >>> Node(1, Node(2, Empty())) + Node(3, Empty())
        Node(1, Node(2, Node(3, Empty())))
        >>> Node(1, Node(2, Empty())) + 5
        Node(1, Node(2, Node(5, Empty())))
        >>> Empty() + 3
        Node(3, Empty())
        >>> Empty() + Node(3, Node(5, Empty()))
        Node(3, Node(5, Empty()))
        '''
        return Node(self.data, self.rest + other)

    def __sub__(self, other):
        if other == self.data:
            return self.rest
        else:
            return Node(self.data, self.rest - other)

    def max(self):
        '''
        Returns the lowest value of a linked-list.
        :return: The highest number in a linked-list.
        >>> Node(1, Node(2, Empty())).max()
        2
        >>> Node(4, Node(2, Empty())).max()
        4
        '''
        if self.data > self.rest.max():
            return self.data
        else:
            return self.rest.max()

    def min(self):
        '''
        Returns the lowest value of a linked-list.
        :return:
        >>> Node(1, Node(2, Empty())).min()
        1
        >>> Node(4, Node(2, Empty())).min()
        2
        '''
        if self.data < self.rest.min():
            return self.data
        else:
            return self.rest.min()

    def __len__(self):
        '''

        :return:
        >>> Node(4, Node(2, Empty())).__len__()
        2
        >>> Node(4, Node(2, Node(3, Empty()))).__len__()
        3
        '''
        return 1 + len(self.rest)

    def __contains__(self, item):
        '''

        :param item:
        :return:
        '''
        return item == self.data or item in self.rest

    def all_even(self):
        '''
        Checks to see if a list contains all even numbers.
        :return: True if all even, False if not all even.
        >>> Node(2, Node(4, Empty())).all_even()
        True
        >>> Node(1, Node(4, Empty())).all_even()
        False
        '''
        if self.data % 2 == 0:
            return self.rest.all_even()
        else:
            return False

    def all_odd(self):
        '''
        Checks to see if a list contains all odd data points.
        :return: true if all odd, false if not all odd.
        >>> Node(1, Node(3, Empty())).all_odd()
        True
        >>> Node(1, Node(4, Empty())).all_odd()
        False
        '''
        if self.data % 2 != 0:
            return self.rest.all_odd()
        else:
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    list2 = Node(1, Node(4, Empty()))
    list4 = Node(5, Node(9, list2))
    list2 = Node(1, Node(4, list4))
    print(10 in list2)  # list2.__contains__(10)
    print(5 in list2)  # list2.__contains__(5)
    print(list4.min())
    print(list2 + list4)
    print(list4 - 5)
    print(list2.all_even())