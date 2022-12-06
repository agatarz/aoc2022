# https://adventofcode.com/2022/day/5
# Day 5 - part 1

def input_puzzle(source_file):
    """ Get input files as list of lines. """

    with open(source_file) as file:
        puzzle = [line.rstrip() for line in file.readlines()]
        return puzzle


def stack_unmarked(item):
    """ Check if crate which can be added to the Stack is unmarked. """
    if item == [' ']:
        return True
    return False


def decode_movement(input_line):
    """
    Get from input line:
    - number of crates to move,
    - stack from which is moved,
    - stack to which crate is moved.
    """
    input_line = input_line.split()
    crates_to_move = int(input_line[1])
    from_stack = int(input_line[3])
    to_stack = int(input_line[5])
    return crates_to_move, from_stack, to_stack


class Stack:
    """ Stack is made of marked crates. """
    def __init__(self):
        self.stack = []

    def add_top(self, items):
        """ Insert item or items at the top of the Stack. """

        assert type(items) == list
        self.stack.extend(items)

    def add_bottom(self, items):
        """ Insert items at the bottom of the Stack. """

        assert type(items) == list
        self.stack = items + self.stack

    def pop(self, number=1):
        """ Removes and returns items at the top of the Stack."""
        top = self.stack[-number:]
        assert type(top) == list
        self.stack = self.stack[:-number]
        return top

    def peek(self):
        """ Returns the item at the top of the Stack without removing it."""
        return self.stack[-1:]

    def elements(self):
        """ Return list of all items in the Stack"""
        return self.stack


def get_stack(stacks_list, stack_number):
    """ Return object of current Stack. """

    if stack_number < len(stacks_list):
        # If Stack with number 'stack_number' exist, return it
        current_stack = stacks_list[stack_number]
    else:
        # If Stack with number 'stack_number' wasn't created yet, do it and save in list of stacks
        current_stack = Stack()
        stacks_list.append(current_stack)

        print('Stack with number %d is created.' % stack_number)

    return current_stack


def solution(source_puzzle):
    """ After the rearrangement procedure completes, what crate ends up on top of each stack?"""

    # list with Stacks, counted from 1'st position of the list
    stacks = [0, ]

    for line in source_puzzle:
        if '[' in line:
            # get schema of crates in stacks

            for position in range(1, len(line), 4):

                # get Crates ID from current input line
                stack_id = int((position - 1) / 4 + 1)
                crate_id = [line[position]]

                # Stack object for selected stack_id
                selected_stack = get_stack(stacks, stack_id)

                # Check if Crate isn't unmarked then add it to the Stack
                if not stack_unmarked(crate_id):
                    selected_stack.add_bottom(crate_id)

        if 'move' in line:
            # get how many crates you need to move and from which to which stack
            moves_number, id_stack_start, id_stack_stop = decode_movement(line)

            for i in range(moves_number):

                # Get the Stack object from which Crate will be moved
                start_stack = get_stack(stacks, id_stack_start)

                # Get the Crate to move
                crate = start_stack.pop()

                # Get the Stack object to which Crates will be moved
                end_stack = get_stack(stacks, id_stack_stop)

                # Put the Crate at the top of the destination Stack
                end_stack.add_top(crate)

    tops_crates = ''

    # Get the top Crates for each Stack
    for stack in stacks[1:]:
        tops_crates += (stack.peek())[0]

    return tops_crates


test_file = '05test.txt'
input_file = '05.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 'CMZ'

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %r' % answer)
