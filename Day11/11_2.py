# https://adventofcode.com/2022/day/11
# Day 11 - part 2


def input_puzzle(source_file):
     """ Get input files as list of lines. """

     with open(source_file) as file:
         puzzle = [line.rstrip() for line in file.readlines()]
         return puzzle


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.divider = None
        self.true_monkey = None
        self.false_monkey = None
        self.count_inspections = 0

    def first_item(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item
    
    def worry_level_operation(self, old):
        return eval(self.operation)
    
    def check_divisibility(self, item):
        if item % self.divider:
            return False
        return True
    
    def throw_monkey(self, diversibility):
        if diversibility:
            return self.true_monkey
        else:
            return self.false_monkey
        

    def inspect_item(self, modulo_factor):

        item = self.first_item()
        worry_item = self.worry_level_operation(item)
        bored_item = worry_item % modulo_factor
        diversibility = self.check_divisibility(bored_item)
        next_monkey = self.throw_monkey(diversibility)
        
        self.count_inspections += 1
        return(next_monkey, bored_item)
    
    def catch_item(self, item):
        self.items.append(item)

    def total_inspections(self):
        return self.count_inspections
    

def define_monkeys(input_puzzles):
    """ Create list of all monkeys with their attributes from input data. """
    
    monkeys = []

    for line in input_puzzles:
    
        if 'Monkey' in line:
            monkey = Monkey()

        elif 'Starting items' in line:
            starting_items = [int(item) for item in line.split(': ')[-1].split(', ')]
            monkey.items.extend(starting_items)

        elif 'Operation' in line:
            operation = line.split(' = ')[-1]
            monkey.operation = operation

        elif 'Test' in line:
            divider = int(line.split(' ')[-1])
            monkey.divider = divider

        elif 'true' in line:
            true_monkey = int(line.split(' ')[-1])
            monkey.true_monkey = true_monkey
        
        elif 'false' in line:
            false_monkey = int(line.split(' ')[-1])
            monkey.false_monkey = false_monkey
            monkeys.append(monkey)

        else:
            continue
    
    return monkeys


def solution(input_puzzles, rounds):
    """ What is the level of monkey business after 10000 rounds?"""
    monkeys = define_monkeys(input_puzzles)
    modulo_divider = 1

    for monkey in monkeys:
        modulo_divider *= monkey.divider

    for round in range(rounds):

        for monkey in monkeys:
            for i in range(len(monkey.items)):
                throw_to_monkey, item = monkey.inspect_item(modulo_divider)
                monkeys[throw_to_monkey].catch_item(item)

    inspection_times = [monkey.total_inspections() for monkey in monkeys]
    most_two = sorted(inspection_times)[-2:]
    answer = most_two[0] * most_two[1]
    return answer


test_file = '11test.txt'
input_file = '11.txt'

# Compare with the test example
assert solution(input_puzzle(test_file), 10000) == 2713310158

# Solve the problem
answer = solution(input_puzzle(input_file), 10000)
print('Puzzle answer: %d' % answer)
