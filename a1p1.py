# a1p1.py

# Meredith Lo
# meredil3@uci.edu
# 47797296

from pathlib import Path


def recurse(path):
    items = []
    for item in path.iterdir():
        items.append(item)
        if item.is_dir():
            items.extend(recurse(item))
    return items


def list_options(path, commands, suffix_or_name):
    # Check for recursion
    if "-r" in commands:
        items = recurse(path)
    else:
        items = list(path.iterdir())
    results = []

    # Execute each command
    for item in items:
        # output files, excluding folders in the results
        if "-f" in commands and item.is_file():
            results.append(item)
        # output files that match a given name
        elif "-s" in commands and item.name == suffix_or_name:
            results.append(item)
        # output files that match an extension
        elif ("-e" in commands and
              item.suffix[1:] == suffix_or_name and
              item.is_file()):
            results.append(item)
        elif "-f" not in commands and "-e" not in commands:
            results.append(item)
    return results


def print_results(results):
    # Print results
    for item in results:
        print(item)


def split_input(inp):
    tokens = inp.split()
    # Collect pieces of the input
    control = tokens[0]
    path = tokens[1]

    commands = []
    final_command_index = 0
    for token in tokens:
        if token[0] == "-":
            commands.append(token)
            final_command_index = inp.index(token) + 3
    suffix_or_name = inp[final_command_index:]
    return control, path, commands, suffix_or_name


def run():
    try:
        control, path, commands, suffix_or_name = split_input(input())
        if control == "L":
            print_results(list_options(Path(path), commands, suffix_or_name))
            run()
    except IndexError:
        print("Goodbye")


if __name__ == "__main__":
    print("Assignment 1 part 1")
    run()
