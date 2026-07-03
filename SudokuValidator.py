def valid_group(group):
    nums = [n for n in group if n != 0]
    return len(nums) == len(set(nums))

def get_rows(board):
    return board

def get_cols(board):
    return [[board[r][c] for r in range(9)] for c in range(9)]

def get_boxes(board):
    boxes = []
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for r in range(3):
                for c in range(3):
                    box.append(board[box_row * 3 + r][box_col * 3 + c])
            boxes.append(box)
    return boxes

def is_valid_sudoku(board):
    for group in get_rows(board):
        if not valid_group(group):
            return False
    for group in get_cols(board):
        if not valid_group(group):
            return False
    for group in get_boxes(board):
        if not valid_group(group):
            return False
    return True

def read_board():
    print("Enter 9 rows, 9 numbers each (0 for empty), space separated:")
    board = []
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

def main():
    board = read_board()
    if is_valid_sudoku(board):
        print("Valid Sudoku board")
    else:
        print("Invalid Sudoku board")

if __name__ == "__main__":
    main()
