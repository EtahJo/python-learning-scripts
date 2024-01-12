#! /usr/bin/env python3


def get_colors():
    """
    (str)=>[]
    returns a list of colors depending on the users input
    """
    list_of_colors = []
    prompt = "Add to list of colors : "
    color = input(prompt)
    while color != '':
        list_of_colors.append(color)
        color = input(prompt)
    return list_of_colors


print(get_colors())
