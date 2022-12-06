# https://adventofcode.com/2022/day/3
# Day 3 - part 2

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
    Find the item type that corresponds to the badges of each three-Elf group.
    What is the sum of the priorities of those item types?
    """

    priorities_sum = 0

    for i in range(0, len(source_puzzle), 3):

        # items for the group's rucksacks
        rucksack1 = set(source_puzzle[i])
        rucksack2 = set(source_puzzle[i + 1])
        rucksack3 = set(source_puzzle[i + 2])

        # item type that appears in all three rucksacks
        badge = set.intersection(rucksack1, rucksack2, rucksack3)
        badge = list(badge)[0]

        priorities_sum += calculate_priority(badge)

    return priorities_sum


test_file = '03test.txt'
input_file = '03.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 70

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
