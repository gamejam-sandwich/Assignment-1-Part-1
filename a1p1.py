#a1p1.py

# Meredith Lo
# meredil3@uci.edu
# 47797296

from pathlib import Path


def list_options(path, commands, suffix_or_name):
    #directory_path = Path(path)
    
    # Execute each command
    for command in commands:
        if command == "-r":
            # output directory content recursively
            for item in path.rglob("*"):
                print(item)
        elif command == "-f":
            # output files, excluding folders in the results
            for item in path.iterdir():
                if item.is_file(): print(item)
        elif command == "-s":
            # output files that match a given name
            for item in path.iterdir():
                if item.name == suffix_or_name:
                    print(item)
        elif command == "-e":
            # output files that match an extension
            for item in path.iterdir():
                if item.suffix[1:] == suffix_or_name:
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
    control, path, commands, suffix_or_name = split_input(input("COMMAND PATH -ADDITIONAL "))
    path = Path(path)

    if control == "L":
        list_options(path, commands, suffix_or_name)
        run()


if __name__ == "__main__":
    print("Assignment 1 part 1")
    run()