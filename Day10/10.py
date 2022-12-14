# https://adventofcode.com/2022/day/10
# Day 10 - part 1

def input_puzzle(source_file):
     """ Get input files as list of lines. """

     with open(source_file) as file:
         puzzle = [line.rstrip() for line in file.readlines()]
         return puzzle


def cycles_x_register(input_puzzles):
    """ Return list with X register values for each cycle. """

    # The last X register value
    x = 1

    # X values for each cycle -> X_values[n] for n cycle
    x_values = [0, 1]
    
    for line in input_puzzles:        

        if line.startswith('addx'):
            
            # X register in signal
            add_x = int(line.split(' ')[-1])
            
            x_values.append(x)
            x += add_x

        # for noop signal: x doesnt change    
        x_values.append(x)

    return x_values


def solution(input_puzzles):
    """ 
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    What is the sum of these six signal strengths?
    """
    # X_register[n] value for n cycle
    x_registers = cycles_x_register(input_puzzles)
    
    # Get (cycle, x) during the 20th, 60th, 100th, 140th, 180th, and 220th cycles 
    chosen_cycles = [(n, x_registers[n]) for n in range(len(x_registers)) if n%40 == 20]

    # Total signal strength
    answer = sum(map(lambda x: x[0]*x[1], chosen_cycles))
          
    return answer
    
test_file = '10test.txt'
input_file = '10.txt'

# Compare with the test example
assert solution(input_puzzle(test_file)) == 13140

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)