# https://adventofcode.com/2022/day/7
# Day 7 - part 1

from collections import Counter


def input_puzzle(source_file):
     """ Get input files as list of lines. """

     with open(source_file) as file:
         puzzle = [line.rstrip() for line in file.readlines()]
         return puzzle


def print_tree(d, level=0):
    """ Present graphically tree with directories and files. """
    
    for key, value in d.items():
        
        # Print directories
        if isinstance(value, dict):
            print('|' * level, key,)
            print_tree(value, level + 1)
            
        # Print files
        else:
            print('-' * level, key, value)
            
            

def create_files_tree(input_puzzles):
    """ 
    Make strcture of files as nested dictonaries from input file.
    Find the total size of each directory
    """
    # Count total size of each directory
    directory_size = Counter()
    
    # Make tree structure of files as nested dict
    tree = {}

    # Add main directory and set it to current directory
    tree['/'] = {}
    main_dir = tree['/']
    current_dir = main_dir
    directory_path = ['/']
    
    for line in input_puzzles:

        if line.startswith('$ cd'):
            cd_arg = line.split('$ cd ')[1]

            if cd_arg == '/':
                # Switches the current directory to the outermost directory
                current_dir = main_dir
                directory_path = ['/']
        
            elif cd_arg == '..':
                # Moves out one level

                current_dir = tree
                directory_path = directory_path[:-1]

                if directory_path == []:
                    directory_path.append('/')

                for branch in directory_path:
                    current_dir = current_dir[branch]

            else:
                # moves in one level
                if cd_arg not in current_dir.keys():

                    # make directory if doesnt exist
                    current_dir[cd_arg] = {}

                current_dir = current_dir[cd_arg]
                directory_path.append(cd_arg)

        elif line.startswith('$ ls'):
            continue
        
        elif line.startswith('dir'):
            dir_arg = line.split('dir ')[1]
            current_dir[dir_arg] = {}
        
        else:
            line = line.split(' ')
            file_size = int(line[0])
            file_name = line[1]

            current_dir[file_name] = file_size

            for i in range(len(directory_path)):
                branch = '/'.join(directory_path[:i+1])

                directory_size[branch] += file_size
                
    return tree, directory_size


def solution(input_puzzles):
    """ 
    Find all of the directories with a total size of at most 100000. 
    What is the sum of the total sizes of those directories? 
    """

    # Make tree of files and cout directories sizes
    dir_tree, dir_size = create_files_tree(input_puzzles)

    # Sum of the total sizes of directories with a total size of at most 100000
    answer = sum([item for item in dir_size.values() if item<100000])

    return answer

test_file = '07test.txt'
input_file = '07.txt'

# Compare with the test example
assert solution(input_puzzle(test_file)) == 95437

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)

