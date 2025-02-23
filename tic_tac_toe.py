from termcolor import colored

player1_input = "X"
player2_input = "O"

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    print(colored("\n  0 1 2", "cyan"))
    for i in range(3):
        print(colored(f"{i} ", "cyan"), end="")
        for j in range(3):
            if board[i][j] == "X":
                print(colored("X", "red"), end=" ")
            elif board[i][j] == "O":
                print(colored("O", "yellow"), end=" ")
            else:
                print(" ", end=" ")
            if j < 2:
                print("|", end=" ")
        print()
        if i < 2:
            print("  -+-+-")
    print()

def check_logic():
    # Check rows
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            return f"Player {'1' if board[i][0] == 'X' else '2'} Wins!"

    # Check columns
    for j in range(3):
        if board[0][j] != " " and board[0][j] == board[1][j] == board[2][j]:
            return f"Player {'1' if board[0][j] == 'X' else '2'} Wins!"

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return f"Player {'1' if board[0][0] == 'X' else '2'} Wins!"
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return f"Player {'1' if board[0][2] == 'X' else '2'} Wins!"

    # Check for tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "It's a Tie!"

    return None

def start_game():
    """Starts and runs the Tic Tac Toe game."""
    print(colored("Welcome, Let's play Tic Tac Toe!", "green"))
    current_player = player1_input
    player_num = 1

    while True:
        print_board()
        while True:
            try:
                row = int(
                    input(
                        colored(
                            f"Player {player_num} ({current_player}), enter row (0-2): ",
                            "blue",
                        )
                    )
                )
                col = int(
                    input(
                        colored(
                            f"Player {player_num} ({current_player}), enter column (0-2): ",
                            "blue",
                        )
                    )
                )
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print(colored("Invalid move! Try again.", "red"))
            except ValueError:
                print(colored("Please enter numbers between 0 and 2.", "red"))

        board[row][col] = current_player

        result = check_logic()
        if result:
            print_board()
            print(colored(result, "magenta"))
            break

        current_player = (
            player2_input if current_player == player1_input else player1_input
        )
        player_num = 2 if player_num == 1 else 1

start_game()