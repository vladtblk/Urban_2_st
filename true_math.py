from math import inf
def divide (first, second):
    result = 0
    if second != 0:
        result = first / second
    else:
        result = inf
    return result
