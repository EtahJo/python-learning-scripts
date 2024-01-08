#!/usr/bin/env python3


def sum_of_lists(list1, list2):
    """ (list of numbers, list of numbers)->list
    returns a new list whose values are a sum of the corresponding values of list1 and list2

    precondition: len(list1) == len(list2)

    >>> sum_of_lists([1,2,3],[4,5,6])
    [5,7,9]
    >>> sum_of_lists([4,7,8],[10,11,12])
    [14,18,20]
    """
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list


print(sum_of_lists([1, 2, 3], [4, 5, 6]))
print(sum_of_lists([4, 7, 8], [10, 11, 12]))


def count_matches(str1, str2):
    """ (str,str)->int
    returns the number of times string str1 and str2 have thesame values at corresponding positions

    precondition: len(str1) == len(str2)

    >>> count_matches("ate","ape")
    2
    >>> count_matches("hard","head")
    2
    """
    num_matches = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            num_matches += 1
    return num_matches


print(count_matches("ate", "ape"))
print(count_matches("hard", "head"))
