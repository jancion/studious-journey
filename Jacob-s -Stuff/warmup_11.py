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

    def max(self):
        if self.data > self.rest.max():
            return self.data
        else:
            return self.rest.max()

    def min(self):
        if self.data < self.rest.min():
            return self.data
        else:
            self.rest.min()

    def __len__(self):
        return 1 + len(self.rest)

    def __contains__(self, item):
        return item == self.data or item in self.rest


if __name__ == "__main__":
    list2 = Node(3, Node(5, Empty()))
    list4 = Node(1, Node(2, list2))
    print(10 in list2)  # list2.__contains__(10)
    print(5 in list2)  # list2.__contains__(5)
    print(list4.min())
    print(list2 + list4)