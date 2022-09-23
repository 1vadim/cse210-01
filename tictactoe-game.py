'''
W02 Prove: Developer - Solo Code Submission
Author: Vadym Chemariev
'''

def main():
    board = create_board()
    player = next_player("")
    
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a position (1-9): "))
    while board[square-1] == "x" or board[square-1] == "o":
        print("Please, make another choice.")
        square = int(input(f"{player}'s turn to choose a position (1-9): "))
    else: board[square - 1] = player



if __name__ == "__main__":
    main()