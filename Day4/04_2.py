# https://adventofcode.com/2022/day/4
# Day 4 - part 2

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def intersection(rangeA, rangeB):
    set1 = set(range(rangeA[0], rangeA[1] + 1))
    set2 = set(range(rangeB[0], rangeB[1] + 1))

    if len(set.intersection(set1, set2)):
        return True
    return False


def solution(source_puzzle):
    """
    In how many assignment pairs do the ranges overlap?
    """

    sum_pairs = 0
    for line in source_puzzle:

        line = line.strip().split(',')
        range1 = [int(item) for item in line[0].split('-')]
        range2 = [int(item) for item in line[1].split('-')]

        # Check if any of pairs do the range overlap
        sum_pairs += intersection(range1, range2)

    return sum_pairs


test_file = '04test.txt'
input_file = '04.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 4

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
