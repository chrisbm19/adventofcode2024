import re
from operator import mul

def main():
    # declare variables
    sum = 0
    
    # read puzzle input into string
    with open("puzzle_input.txt", "r", encoding=None) as file:
        puzzle_input = file.read()

    # establish regex pattern to match against puzzle input
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    # get list of all matches
    matches = re.findall(pattern, puzzle_input)

    # loop over list of matches, evaluating each expression and adding the results to the sum
    for i in matches:
        sum += eval(i)
    
    print(f"SUM: {sum}")
    return

main()