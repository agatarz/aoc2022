# https://adventofcode.com/2022/day/1

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def solution(source_puzzle):
    """
    Find the top three Elves carrying the most Calories.
    How many Calories are those Elves carrying in total?

    """
    # Amount of calories which current Elf is carrying
    elf_calories = 0

    # List of all calories carried by Elves
    all_calories = []

    for line in source_puzzle:

        if line:
            # For lines with calorie's definitions
            item_calories = int(line)
            elf_calories += item_calories
        else:
            all_calories.append(elf_calories)
            elf_calories = 0

    # Add calories from the last Elf
    all_calories.append(elf_calories)

    # Total calories for top 3 Elves
    top_calories = sum(sorted(all_calories)[-3:])

    return top_calories


test_file = '01test.txt'
input_file = '01.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 45000

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)
