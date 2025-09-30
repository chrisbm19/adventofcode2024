import re
from operator import mul

def find_closest_below(data_list, target_value):
    below_values = [x.start() for x in data_list if x.start() < target_value]
    if not below_values:
        return -1
    closest_below = max(below_values)
    return closest_below

def main():
    # declare variables
    sum = 0

    # read puzzle input into string
    with open("puzzle_input.txt", "r", encoding=None) as file:
        puzzle_input = file.read()

    # establish regex patterns to match against puzzle input
    mul_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # get lists of matches
    mul_matches = list(re.finditer(mul_pattern, puzzle_input))
    do_matches = list(re.finditer(do_pattern, puzzle_input))
    dont_matches = list(re.finditer(dont_pattern, puzzle_input))
    
    for i in mul_matches:
        # find closest do_match
        closest_do = find_closest_below(do_matches, i.start())

        # find closest dont_match
        closest_dont = find_closest_below(dont_matches, i.start())

        # if do is more recent OR neither have occurred (first mul) then evaluate the expression
        # if dont is more recent, skip that mul expression
        if(closest_do > closest_dont or closest_do == closest_dont):
            sum += eval(i.group())
        elif(closest_dont > closest_do):
            continue

    print(f"SUM: {sum}")
    return

main()