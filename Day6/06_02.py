# https://adventofcode.com/2022/day/6
# Day 6 - part 2

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle[0]


def solution(source_puzzle):
    """ How many characters need to be processed before the first start-of-message marker is detected? """

    i = 0

    while True:
        # current four-letter word
        marker = source_puzzle[i:i + 14]

        # the number of unique chars in the current string
        unique_chars = len(set(marker))

        # for all unique chars marker is found
        if unique_chars == 14:
            return i + 14

        if i == len(source_puzzle) - 14:
            return 0

        i += 1


def test_solution():
    test_puzzles = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
                    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
                    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
                    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)]

    for puzzle, ans in test_puzzles:
        assert solution(puzzle) == ans
    return True


input_file = '06.txt'

# Compare with the test example
test_solution()

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
