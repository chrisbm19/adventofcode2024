def main():
    # set up lists
    one = []
    two = []
    distances = []

    # split the inputs into two separate lists
    with open("puzzle_input.txt", "r", encoding=None) as input:
        for line in input:
            temp = line.split()
            one.append(temp[0])
            two.append(temp[1])
    
    # convert each element of the lists from str to int
    for x in range(len(one)):
        one[x] = int(one[x])
    for y in range(len(two)):
        two[y] = int(two[y])
    
    # get the distance between the compared values, then remove the values from the lists, then
    # sum all of the distances to get the answer
    for i in range(len(one)):
        distances.append(abs(min(one)-min(two)))
        del one[one.index(min(one))]
        del two[two.index(min(two))]
    final_distance = sum(distances)

    print(f"Final Distance: {final_distance}")
    return

main()