from utils import *


# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    dictionary = dict(zip(boxes, grid))
    for key, value in dictionary.items():
        if value == '.':
            dictionary[key] = '123456789'
    return dictionary


def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def eliminate2(values):
    solved_boxes = [key for key in values.keys() if len(values[key]) == 1]
    for box in solved_boxes:
        solved_value = values[box]
        peer = peers[box]
        for peer_key in peer:
            values[peer_key] = values[peer_key].replace(solved_value, '')
    return values


def only_choice(values):
    for unit in unitlist:
        counter = {}
        for key in unit:
            value = values[key]

            if len(value) != 1: # doesn't work here! wrong
                for digit in value:
                    if digit in counter:
                        counter[digit] += 1
                    else:
                        counter[digit] = 1
    return values


def only_choice2(values):
    for unit in unitlist:

        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit

    return values

# def only(values):
#     for unit in unitlist:
#         for i in '123456789':
#             box_container = [box for box in unit if i in values[box]]
#
#             if len(box_container) == 1:
#                 values[box_container[0]] = i
#     return values

if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

    dictionary1 = grid_values(grid)
    dictionary1 = eliminate(dictionary1)
    dictionary1 = only_choice(dictionary1)
    print(dictionary1)
    # print('--')
    # dictionary2 = grid_values(grid)
    # dictionary2 = eliminate2(dictionary2)
    # dictionary2 = only_choice2(dictionary2)
    # print(dictionary2)

