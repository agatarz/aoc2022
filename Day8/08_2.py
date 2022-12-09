# https://adventofcode.com/2022/day/8
# Day 8 - part 2

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

    max_scenic_score = 0

    for h in range(1, grid_height - 1):
        for w in range(1, grid_width - 1):

            tree = grid[h,w]

            # Trees around tree
            top = grid[0:h, w][::-1]
            bottom = grid[h+1:, w]
            left = grid[h, 0:w][::-1]
            right = grid[h, w+1:]
            directions = (top, bottom, left, right)

            tree_scenic_score = 1

            # Count viewing distance for current tree for all directions
            for dir in directions:

                viewing_distance = 0

                for i in dir:
                    if i < tree:
                        viewing_distance += 1
                    elif i >= tree:
                        viewing_distance +=1 
                        break

                tree_scenic_score *= viewing_distance
            
            max_scenic_score = max(max_scenic_score, tree_scenic_score)

    return max_scenic_score


test_file = '08test.txt'
input_file = '08.txt'

# Compare with the test example
assert solution(input_puzzle(test_file)) == 8

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)