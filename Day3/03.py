# https://adventofcode.com/2022/day/3
# Day 3 - part 1

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def calculate_priority(item):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """

    if str.isupper(item):
        # A - Z: 65 - 90
        return ord(item) - 38
    else:
        # a - z: 97 - 122
        return ord(item) - 96


def solution(source_puzzle):
    """
    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """

    priorities_sum = 0

    for line in source_puzzle:

        # Items in first rucksack's compartment
        first_compartment = line[:len(line) // 2]
        first_items = set(first_compartment)

        # Items in second rucksack's compartment
        second_compartment = line[len(line) // 2:]
        second_items = set(second_compartment)

        # Item type that appears in both compartments
        shared_item = first_items.intersection(second_items)
        shared_item = list(shared_item)[0]

        # Add priority of the item type to the sum
        priorities_sum += calculate_priority(shared_item)

    return priorities_sum


test_file = '03test.txt'
input_file = '03.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 157

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)