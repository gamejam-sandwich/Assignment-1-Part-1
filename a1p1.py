#a1p1.py

# Meredith Lo
# meredil3@uci.edu
# 47797296

from pathlib import Path


def list_options(path, additional):
    directory_path = Path(path)
    if additional == "-r":
        for item in directory_path.rglob("*"):
            print(item)
        # output directory content recursively
    elif additional == "-f":
        for item in directory_path.iterdir():
            if item.is_file(): print(item)
        # output files, excluding folders in the results
    elif additional == "-s":
        print()
        # output files that match a given name
    elif additional == "-e":
        print()
        # output files that match an extension

def run():
    inp = input("COMMAND PATH -ADDITIONAL ")
    user_input = inp.split()
    command = user_input[0]
    path = user_input[1]
    additional = user_input[2]
    if command == "L":
        list_options(path, additional)
        run()


if __name__ == "__main__":
    print("Assignment 1 part 1")
    run()