from random import randrange

def initialize_board():
    """
    Initialize the game board with numbers representing each position.
    """
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    return board

def print_board(board):
    """
    Print the current game board.
    """
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def check_win(board, mark):
    """
    Check if the specified mark has won the game.
    """
    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def is_board_full(board):
    """
    Check if the board is full (no more free cells).
    """
    for row in board:
        for cell in row:
            if cell.isdigit():
                return False
    return True

def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    current_mark = 'X'  

    while True:
        if current_mark == 'X':
            
            while True:
                computer_move = randrange(9) + 1  
                row = (computer_move - 1) // 3
                col = (computer_move - 1) % 3
                if board[row][col].isdigit():
                    board[row][col] = 'X'
                    break
        else:
            
            while True:
                try:
                    user_move = int(input("Enter your move (1-9): "))
                    if 1 <= user_move <= 9:
                        row = (user_move - 1) // 3
                        col = (user_move - 1) % 3
                        if board[row][col].isdigit():
                            board[row][col] = 'O'
                            break
                        else:
                            print("That spot is already taken!")
                    else:
                        print("Please enter a number between 1 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print_board(board)


        if check_win(board, current_mark):
            if current_mark == 'X':
                print("Computer won!")
            else:
                print("You won!")
            break

        
        if is_board_full(board):
            print("It's a tie!")
            break

       
        current_mark = 'O' if current_mark == 'X' else 'X'

if __name__ == "__main__":
    main()
