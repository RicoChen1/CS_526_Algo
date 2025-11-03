import sys
import math

def is_valid_board(board, symbols):
    n = len(board)
    # The size of the sub-board is the square root of n
    sub_board_size = int(math.sqrt(n))

    # This loop checks for uniqueness in rows and columns.
    # It iterates from i = 0 to n-1.
    for i in range(n):
        # These sets are used to keep track of the symbols encountered in the current row and column.
        # They are reset for each new row/column.
        row_symbols = set()
        col_symbols = set()
        for j in range(n):
            # Check for duplicates in the current row
            if board[i][j] != '.':
                if board[i][j] in row_symbols:
                    return False  # A duplicate is found in the current row
                row_symbols.add(board[i][j])
            
            # Check for duplicates in the current column
            if board[j][i] != '.':
                if board[j][i] in col_symbols:
                    return False  # A duplicate is found in the current column
                col_symbols.add(board[j][i])

    # This loop checks for uniqueness in each sub-board.
    # It iterates through the board in steps of sub_board_size, effectively visiting the top-left corner of each sub-board.
    for i in range(0, n, sub_board_size):
        for j in range(0, n, sub_board_size):
            sub_board_symbols = set()
            # This nested loop iterates through each cell of the current sub-board.
            for row in range(i, i + sub_board_size):
                for col in range(j, j + sub_board_size):
                    if board[row][col] != '.':
                        if board[row][col] in sub_board_symbols:
                            return False  # A duplicate is found in the sub-board
                        sub_board_symbols.add(board[row][col])
    
    return True # If all checks pass, the board is valid

# The main function reads the input file, parses the board, and calls the validation function.
def main():

    if len(sys.argv) != 2:
        print("Usage: python symbol_puzzle_game.py <input_file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            n = int(lines[0])
            symbols = set(lines[1].split(','))
            board = [line.split(',') for line in lines[2:]]

            # Validate the board and print the result
            if is_valid_board(board, symbols):
                print("The board is valid")
            else:
                print("The board is invalid")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}")
    except (IndexError, ValueError):
        print("Error: Input file is not in the correct format.")

if __name__ == "__main__":
    main()
