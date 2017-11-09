# Ba-Linked-List.py
# Jacob Knecht & CPTR-215
# 2017-11-06 first draft

"""A List is either:
- Empty (contains nothing), or
- a Node that contains a number and a List"""


class List:
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
    def __init__(self):
        pass

    def __repr__(self):
        return "Empty()"

    def __str__(self):
        return "END"

    def sum(self):
        return 0

    def __add__(self, other):
        if type(other) == int:
            return Node(other, Empty())
        else:
            return other

    def __len__(self):
        return 0

    def __contains__(self, item):
        return False

    def max(self):
        return float("-inf")

    def min(self):
        return float("inf")

    def __sub__(self, other):
        return self

    def all_even(self):
        return True

    def all_odd(self):
        return True


class Node(List):
    def __init__(self, number, rest_of_list):
        self.data = number
        self.rest = rest_of_list

    def __repr__(self):
        return "Node(%s, %r)" % (self.data, self.rest)

    def __str__(self):
        return "%s, %s" % (self.data, self.rest)

    def sum(self):
        return self.data + self.rest.sum()

    def __add__(self, other):
        return Node(self.data, self.rest + other)

    def __sub__(self, other):
        if other == self.data:
            return self.rest
        else:
            return Node(self.data, self.rest - other)

    def max(self):
        if self.data > self.rest.max():
            return self.data
        else:
            return self.rest.max()

    def min(self):
        if self.data < self.rest.min():
            return self.data
        else:
            return self.rest.min()

    def __len__(self):
        return 1 + len(self.rest)

    def __contains__(self, item):
        return item == self.data or item in self.rest

    def all_even(self):
        if self.data % 2 == 0:
            return self.rest.all_even()
        else:
            return False

    def all_odd(self):
        if self.data % 2 != 0:
            return self.rest.all_odd()
        else:
            return False

if __name__ == "__main__":
    list2 = Node(1, Node(4, Empty()))
    list4 = Node(5, Node(9, list2))
    list2 = Node(1, Node(4, list4))
    print(10 in list2)  # list2.__contains__(10)
    print(5 in list2)  # list2.__contains__(5)
    print(list4.min())
    print(list2 + list4)
    print(list4 - 5)
    print(list2.all_even())