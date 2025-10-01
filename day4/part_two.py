# create a list class with negative indexing disabled
class NoNegativeIndexList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            raise IndexError("Negative indexing is not allowed in this list.")
        return super().__getitem__(index)
    
def probe(board, row, col):
    found = 0
    ur = board[row-1][col+1]
    dl = board[row+1][col-1]
    ul = board[row-1][col-1]
    dr = board[row+1][col+1]
    bad_values = NoNegativeIndexList(["X","A"])
    slashes = NoNegativeIndexList([])

    if (ul != dr) and (ul not in bad_values) and (dr not in bad_values):
        slashes.append(True)
    if (ur != dl) and (ur not in bad_values) and (dl not in bad_values):
        slashes.append(True)
    if (slashes[0] is True) and (slashes[1] is True):
        found += 1
    return found
    
def search(board, rows, cols):
    sum = 0
    for r in range(0, rows):
        for c in range(0, cols):
            try:
                if board[r][c] == "A":
                    found = probe(board, r, c)
                    sum += found
            except IndexError:
                print("", end="")
    return sum
    
def main():
    board = NoNegativeIndexList([])

    # get puzzle_input as a 2d list to represent the word search
    with open("puzzle_input.txt", "r", encoding=None) as file:
        for line in file:
            split_line = NoNegativeIndexList(line.strip())
            board.append(split_line)

    rows = len(board)
    cols = len(board[0])

    sum = search(board, rows, cols)

    print(f"Sum: {sum}")
    return

main()