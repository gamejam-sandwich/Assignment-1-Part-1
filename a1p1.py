#a1p1.py

# Meredith Lo
# meredil3@uci.edu
# 47797296

from pathlib import Path


def list_options(path, commands, suffix_or_name):
    # Check for recursion
    if "-r" in commands:
        items = path.rglob("*")
    else:
        items = path.iterdir()
    
    results = []

    # Execute each command
    for command in commands:
        # output files, excluding folders in the results
        if command == "-f":
            for item in items:
                if item.is_file():
                    results.append(item)
        
        # output files that match a given name
        elif command == "-s":
            for item in items:
                if item.name == suffix_or_name:
                    results.append(item)
        
        # output files that match an extension
        elif command == "-e":
            for item in items:
                if item.suffix[1:] == suffix_or_name:
                    results.append(item)
        
    return results

def print_results(results):
    # Print files first, then print directories
    files = []
    directories = []
    for item in results:
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            directories.append(item)

    results_final = files + directories
    for item in results_final:
        print(item)

def split_input(inp):    
    user_input = inp.split()
    # Collect pieces of the input
    commands = []
    final_command_index = 0
    for token in user_input:
        if token[0] == "-":
            commands.append(token)
            final_command_index = inp.index(token) + 3
    suffix_or_name = inp[final_command_index:]
    control = user_input[0]
    path = user_input[1]
    
    return control, path, commands, suffix_or_name

def run():
    control, path, commands, suffix_or_name = split_input(input())

    if control == "L":
        print_results(list_options(Path(path), commands, suffix_or_name))
        run()


if __name__ == "__main__":
    print("Assignment 1 part 1")
    run()