def object_empty(item):
    # Check if item which can be added to the Stack isn't empty
    if item == ' ':
        return True
    return False


def decode_movement(input_line):
    """ Get from input line number of items_to_move, start_stack, end_stack"""
    input_line = input_line.split()
    items_to_move = int(input_line[1])
    from_stack = int(input_line[3])
    to_stack = int(input_line[5])
    return items_to_move, from_stack, to_stack


class Stack:
    def __init__(self):
        self.stack = []

    def add_top(self, item):
        # insert an object at the top of the Stack
        self.stack.append(item)

    def add_bottom(self, item):
        # insert an object at the bottom of the Stack
        self.stack = [item] + self.stack

    def pop(self):
        # removes and returns the object at the top of the Stack
        top = self.stack.pop()
        return top

    def peek(self):
        # returns the object at the top of the Stack without removing it
        return self.stack[-1]

    def elements(self):
        # return items in the Stack
        return self.stack


def get_stack(stacks_list, stack_number):
    # return object for current stack
    if stack_number < len(stacks_list):
        # If Stack exist, return it
        current_stack = stacks_list[stack_number]
    else:
        # If Stack wasn't created yet, do it
        current_stack = Stack()
        stacks_list.append(current_stack)
        print('Stack with number %d is created.' % stack_number)

    return current_stack


source_file = '05test.txt'
source_file = '05.txt'

# list with Stacks, counted from 1'st position of the list
stacks = [0, ]

with open(source_file) as file:
    input_data = [line.rstrip() for line in file]

for line in input_data:
    if '[' in line:
        # get schema of crates in stacks

        for position in range(1, len(line), 4):
            # get crates ID from current input line

            stack_id = int((position - 1) / 4 + 1)
            crate_id = line[position]

            # Stack object for selected stack_id
            selected_stack = get_stack(stacks, stack_id)

            if not object_empty(crate_id):
                selected_stack.add_bottom(crate_id)

    if 'move' in line:
        # get how many crates you need to move and from which to which stack
        moves_number, id_stack_start, id_stack_stop = decode_movement(line)

        # move items like in description
        for i in range(moves_number):

            # Get the object for stack from which crate will be moved
            start_stack = get_stack(stacks, id_stack_start)
            # Get the crate to move
            crate = start_stack.pop()
            # Get the object to which crate will be moved
            end_stack = get_stack(stacks, id_stack_stop)
            # Put the object at the top of tge stack
            end_stack.add_top(crate)


# Display top crates for each stack
for stack in stacks[1:]:
    print(stack.peek(), end='')
