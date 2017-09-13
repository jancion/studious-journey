'''
Write a function called isStrictlyIncreasing that determines whether
a list of values is strictly increasing or not.
While this should function should work for lists of numbers,
it should also work for homogeneous lists of any type that
can be compared using the == and < operators.

The file you submit shouldn't do any input or output
(unless it's guarded by if __name__ == "__main__":). Don't forget to write your own doctests!

'''

def isStrictlyIncreasing(value_list):
    temp_list = [0]
    for x in len(value_list):
        for i in value_list:
            if i in temp_list:
                continue
            elif i > temp_list[-1]
                temp_list.append(i)
    return temp_list

values = [1, 4, 2, 5, 6, 7, 8, ]


print(isStrictlyIncreasing(values))





if __name__ == '__main__':
    import doctest
    doctest.testmod()