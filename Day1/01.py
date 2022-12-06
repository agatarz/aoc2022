# https://adventofcode.com/2022/day/1

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def solution(source_puzzle):
    """
    Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?
    """

    # Amount of calories which current Elf is carrying
    elf_calories = 0

    # Found number of maximum calories carried by counted Elves
    max_calories = 0

    for line in source_puzzle:

        if line:
            # For lines with calorie's definitions
            item_calories = int(line)
            elf_calories += item_calories
        else:
            max_calories = max(elf_calories, max_calories)
            elf_calories = 0

    # Checking for the last Elf
    max_calories = max(elf_calories, max_calories)

    return max_calories


test_file = '01test.txt'
input_file = '01.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 24000

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
