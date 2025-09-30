def main():
    # set up lists
    one = []
    two = []

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

    freq = [0] * len(one)
    count = 0

    # count frequency of occurences of the same value
    for x in range(len(one)):
        for y in range(len(two)):
            if two[y] == one[x]:
                count += 1
        freq[x] = one[x] * count
        count = 0
    similarity = sum(freq)
    print(f"Similarity: {similarity}")
    return

main()