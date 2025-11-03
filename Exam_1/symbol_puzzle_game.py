import sys
import math

def validate(board, symbols):
    n = len(board)
    sub_board_size = int(math.sqrt(n))

    # Check rows & columns uniqueness
    for i in range(n):
        row_symbols = set()
        col_symbols = set()
        for j in range(n):
            # Check duplicates @ current row
            if board[i][j] != '.':
                if board[i][j] in row_symbols:
                    return False  # if found duplicate in row
                row_symbols.add(board[i][j])
            
            # Check duplicates at current column
            if board[j][i] != '.':
                if board[j][i] in col_symbols:
                    return False  # if found duplicate in column
                col_symbols.add(board[j][i])

    # Check sub-boards uniqueness
    # Iterate board in steps of sub_board_size, visit each sub-board
    for i in range(0, n, sub_board_size):
        for j in range(0, n, sub_board_size):
            sub_board_symbols = set()
            # Iterate through each cell of the sub-board
            for row in range(i, i + sub_board_size):
                for col in range(j, j + sub_board_size):
                    if board[row][col] != '.':
                        if board[row][col] in sub_board_symbols:
                            return False  # Found a duplicate in the sub-board
                        sub_board_symbols.add(board[row][col])
    
    return True # here the board is valid

# AI generated main and entry point for the script
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
