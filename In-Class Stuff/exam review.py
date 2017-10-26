def numLen(num):
    '''
    >>>numLen()
    :param num:
    :return:
    '''
    if num >= 0:
        return len(str(num))
    else:
        return "Non-negative numbers only please."


def isSomething(x):
    return x != ""

x = isSomething("something")
print(x)
type(x)
