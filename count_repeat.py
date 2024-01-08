#!/usr/bin/env python3

def count_adjacent_repeats(string):
    """(str)-> int
    returns the number of adjacent repeats for character in string

    >>> count_adjacent_repeats("afffggyeyhhh")
    5
    >>> count_adjacent_repeats("ffyhheeii")
    4

    """
    similar_sum = 0

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            similar_sum += 1
    return similar_sum


print(count_adjacent_repeats("afffggyeyhhh"))
print(count_adjacent_repeats("ffyhheeii"))
