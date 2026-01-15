#a1p1.py

# Meredith Lo
# meredil3@uci.edu
# 47797296


def list_contents():
    # list the contents of a directory
    # if directory is empty, print nothing
    print()

def list_options(path, additional):
    if additional == "r":
        print()
        # output directory content recursively
    elif additional == "f":
        print()
        # output files, excluding directories in the results
    elif additional == "s":
        print()
        # output files that match a given name
    elif additional == "e":
        print()
        # output files that match an extension

def run():
    inp = input("COMMAND PATH -ADDITIONAL")
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