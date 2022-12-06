# https://adventofcode.com/2022/day/4
# Day 4 - part 1

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def intersection(rangeA, rangeB):
    if rangeA[0] >= rangeB[0] and rangeA[1] <= rangeB[1]:
        return True
    return False


def solution(source_puzzle):
    """
    In how many assignment pairs does one range fully contain the other?
    """

    sum_pairs = 0
    for line in source_puzzle:

        line = line.strip().split(',')
        range1 = [int(item) for item in line[0].split('-')]
        range2 = [int(item) for item in line[1].split('-')]

        # Check if any of pairs fully contains the other
        if any([intersection(range1, range2), intersection(range2, range1)]):
            sum_pairs += 1

    return sum_pairs


test_file = '04test.txt'
input_file = '04.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 2

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
