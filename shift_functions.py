#!/usr/bin/env python3

def shift_left(L):
    """ (list)->list
    returns an updated list which is a containing the items in L shifted
    one position to the left and the first element pushed to the last position

    >>> shift_left([1,2,4])
    [2,4,1]
    >>> shift_left([57,58,7,8,20])
    [58,7,8,20,57]

    """
    first_value = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_value

    return L


print(shift_left([1, 2, 4]))
print(shift_left([57, 58, 7, 8, 20]))
