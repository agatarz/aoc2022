# https://adventofcode.com/2022/day/10
# Day 10 - part 2

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
    Render the image given by your program.
    """

    # X_register[n] value for n cycle
    x_registers = cycles_x_register(input_puzzles)

    # Position of pixel which is currently being drawn on the screen
    pixel_position = 0
    
    # CRT row on the screen
    crt = ""

    for cycle_nr in range(1, len(x_registers)):

        # X register for cycle_nr
        x = x_registers[cycle_nr]

        # Sprite position
        sprite_x = [x - 1, x, x + 1]

        # Determine whether the sprite is visible
        if len(set(sprite_x).intersection(set([pixel_position]))):
            crt += '#'
        else:
            crt += '.'

        pixel_position += 1

        # End of CRT row 
        if cycle_nr % 40 == 0:
            print(crt)
            crt = ''
            pixel_position = 0
           
    return None
    

test_file = '10test.txt'
input_file = '10.txt'

solution(input_puzzle(input_file))
