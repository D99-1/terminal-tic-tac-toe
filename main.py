import os

def clear_terminal():
    os.system('clear')

def print_board(board):
    print("    0     1     2")
    print("  " + "     |     |    ")
    for row_index, row in enumerate(board):
        print(f"{row_index} ", end="")
        for col_index, cell in enumerate(row):
            if col_index < 2:
                print(f"  {cell}  |", end="")
            else:
                print(f"  {cell}  ")
        if row_index < 2:
            print("  " + "_____|_____|_____")
            print("  " + "     |     |    ")
        else:
            print("  " + "     |     |    ")

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        clear_terminal()
        print_board(board)
        try:
            row = int(input(f"Player {players[current_player]}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {players[current_player]}, enter the column (0, 1, 2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue

            if board[row][col] == " ":
                board[row][col] = players[current_player]
                if check_winner(board, players[current_player]):
                    clear_terminal()
                    print_board(board)
                    print(f"Player {players[current_player]} wins!")
                    break
                if is_full(board):
                    clear_terminal()
                    print_board(board)
                    print("The game is a tie!")
                    break
                current_player = (current_player + 1) % 2
            else:
                print("That spot is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers for row and column.")
main()
