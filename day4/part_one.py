# create a list class with negative indexing disabled
class NoNegativeIndexList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            raise IndexError("Negative indexing is not allowed in this list.")
        return super().__getitem__(index)

def probe(board, row, col):
    found = 0
    # xmas is spelled left-to-right
    try:
        if board[row][col+1] == "M" and board[row][col+2] == "A" and board[row][col+3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out right-to-left
    try:
        if board[row][col-1] == "M" and board[row][col-2] == "A" and board[row][col-3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out straight down
    try:
        if board[row+1][col] == "M" and board[row+2][col] == "A" and board[row+3][col] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out straight up
    try:
        if board[row-1][col] == "M" and board[row-2][col] == "A" and board[row-3][col] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out diagonally to the right (down)
    try:
        if board[row+1][col+1] == "M" and board[row+2][col+2] == "A" and board[row+3][col+3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out diagonally to the right (up)
    try:
        if board[row-1][col+1] == "M" and board[row-2][col+2] == "A" and board[row-3][col+3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out diagonally to the left (down)
    try:
        if board[row+1][col-1] == "M" and board[row+2][col-2] == "A" and board[row+3][col-3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    # xmas is spelled out diagonally to the left (up)
    try:
        if board[row-1][col-1] == "M" and board[row-2][col-2] == "A" and board[row-3][col-3] == "S":
            found += 1
    except IndexError:
        print("", end="")
    return found

def search(board, rows, cols):
    sum = 0
    for r in range(0, rows):
        for c in range(0, cols):
            try:
                if board[r][c] == "X":
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
            split_line = NoNegativeIndexList(line)
            board.append(split_line)

    rows = len(board)
    cols = len(board[0])

    sum = search(board, rows, cols)

    print(f"Sum: {sum}")
    return

main()