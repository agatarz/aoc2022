# https://adventofcode.com/2022/day/8
# Day 8 - part 1

import numpy as np

def input_puzzle(source_file):
     """ Get input files as list of lines. """

     with open(source_file) as file:
         puzzle = [line.rstrip() for line in file.readlines()]
         return puzzle
     

def solution(input_puzzles):

    """ How many trees are visible from outside the grid?"""

    # Read the grid
    grid = np.array([list(line) for line in input_puzzles])
    grid = grid.astype(int)
    grid_height, grid_width = grid.shape

    visible_trees = 2 * (grid_width + grid_height - 2)


    for h in range(1, grid_height - 1):
        for w in range(1, grid_width - 1):

            tree = grid[h][w]

            top = grid[0:h, w]
            bottom = grid[h+1:, w]
            left = grid[h, 0:w]
            right = grid[h, w+1:]

            top_cond = all(tree > top)
            bottom_cond = all(tree > bottom)
            left_cond = all(tree > left)
            right_cond = all(tree > right)

            condition = any([top_cond, bottom_cond, left_cond, right_cond])

            if condition:
                visible_trees += 1

    return visible_trees


test_file = '08test.txt'
input_file = '08.txt'

# Compare with the test example
assert solution(input_puzzle(test_file)) == 21

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)