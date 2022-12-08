# https://adventofcode.com/2022/day/7
# Day 7 - part 2

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
    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
    What is the total size of that directory? 
    """

    # Make tree of files and cout directories sizes
    dir_tree, dir_size = create_files_tree(input_puzzles)

    # The total size of the outermost directory
    total_size = dir_size.most_common(1)[0][1]

    # The total disk space available to the filesystem
    max_size = 70000000

    # The disk space required by the update
    update_size = 30000000

    # The disk space that must be delete
    unused_size = max_size - total_size
    space_to_delete = update_size - unused_size

    # The total space of the smallest directory that should be deleted.
    answer = min([size for size in dir_size.values() if size >= space_to_delete])

    return answer

test_file = '07test.txt'
input_file = '07.txt'


# Compare with the test example
assert solution(input_puzzle(test_file)) == 24933642

# Solve the problem
answer = solution(input_puzzle(input_file))
print('Puzzle answer: %d' % answer)

