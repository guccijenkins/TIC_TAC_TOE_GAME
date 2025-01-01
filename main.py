from replit import clear
# set up the tic tac toe board
board = [['', '|', '', '|', ''],
            ['-------'],
        ['', '|', '', '|', ''],
            ['-------'],
        ['', '|', '', '|', '']]

# set up the player inputs for row and column, with accompanied list and index number.
# For example; [1,1],[0,0], where [1,1] is the player input for row and column number,
# and [0,0] is the list number and the index number for that list.
board_positions = [[[1,1],[0,0]],[[1,2],[0,2]],[[1,3],[0,4]],
                   [[2,1],[2,0]],[[2,2],[2,2]],[[2,3],[2,4]],
                   [[3,1],[4,0]],[[3,2],[4,2]],[[3,3],[4,4]]]

# list to capture all the positions removed from board_positions list
removed_positions = []

# function that prints the most current layout of the board
def print_board():
    print('\n')
    print("Player 1 is 'X' and Player 2 is 'O'\n")
    for i in board:
        print(*i)
    print('\n')

# function for player 1 input
def player_1():
    global board
    global board_positions
    global removed_positions
    player_1_input = []
    player_1_row = int(input("Player 1, Please enter a row number (1, 2, or 3): "))
    player_1_input.append(player_1_row)
    player_1_column = int(input("Player 1, Please enter a column number (1, 2, or 3): "))
    player_1_input.append(player_1_column)

    # for loop to see if a position on board is already taken
    for r in removed_positions:
        if r == player_1_input:
            print("That position is already taken on the board. Please re-enter a position.")
            player_1_input.clear()
            player_1()

    # for loop for inserting a position on the board
    for i in board_positions:
        if player_1_input == i[0]:
            inputted = i[1]
            board[inputted[0]].insert(inputted[1], "X")
            board[inputted[0]].pop(inputted[1] + 1)
            removed_positions.append(player_1_input)

    # if statement for an inputted position that is outside the range of the boards column and rows
    if player_1_row > 3 or player_1_column > 3 or player_1_row < 1 or player_1_column < 1:
        print("The position input does not exist. Please re-enter a position.")
        player_1_input.clear()
        player_1()

# function for player 1 input
def player_2():
    global board
    global board_positions
    global removed_positions
    player_2_input = []
    player_2_row = int(input("Player 2, Please enter a row number (1, 2, or 3): "))
    player_2_input.append(player_2_row)
    player_2_column = int(input("Player 2, Please enter a column number (1, 2, or 3): "))
    player_2_input.append(player_2_column)

    # for loop to see if a position on board is already taken
    for r in removed_positions:
        if r == player_2_input:
            print("That position is already taken on the board. Please re-enter a position.")
            player_2_input.clear()
            player_2()

    # for loop for inserting a position on the board
    for i in board_positions:
        if player_2_input == i[0]:
            inputted = i[1]
            board[inputted[0]].insert(inputted[1], "O")
            board[inputted[0]].pop(inputted[1] + 1)
            removed_positions.append(player_2_input)

    # if statement for an inputted position that is outside the range of the boards column and rows
    if player_2_row > 3 or player_2_column > 3 or player_2_row < 1 or player_2_column < 1:
        print("The position input does not exist. Please re-enter a position.")
        player_2_input.clear()
        player_2()

# while loop that checks if there is a winner based on the board layout of "X" and "O"
game_on = True
while game_on:
    print_board()
    player_1()
    if board[0][0] == "X" and board[0][2] == "X" and board[0][4] == "X" or board[2][0] == "X" and board[2][2] == "X" and board[2][4] == "X" or board[4][0] == "X" and board[4][2] == "X" and board[4][4] == "X":
        print_board()
        print("PLAYER 1 WINS. GAME OVER!")
        break
    elif board[0][0] == "X" and board[2][0] == "X" and board[4][0] == "X" or board[0][2] == "X" and board[2][2] == "X" and board[4][2] == "X" or board[4][0] == "X" and board[4][2] == "X" and board[4][4] == "X":
        print_board()
        print("PLAYER 1 WINS. GAME OVER!")
        break
    elif board[0][0] == "X" and board[2][2] == "X" and board[4][4] == "X" or board[0][4] == "X" and board[2][2] == "X" and board[4][0] == "X":
        print_board()
        print("PLAYER 1 WINS. GAME OVER!")
        break
    print_board()
    player_2()
    if board[0][0] == "O" and board[0][2] == "O" and board[0][4] == "O" or board[2][0] == "O" and board[2][2] == "O" and board[2][4] == "O" or board[4][0] == "O" and board[4][2] == "O" and board[4][4] == "O":
        print_board()
        print("PLAYER 2 WINS. GAME OVER!")
        break
    elif board[0][0] == "O" and board[2][0] == "O" and board[4][0] == "O" or board[0][2] == "O" and board[2][2] == "O" and board[4][2] == "O" or board[4][0] == "O" and board[4][2] == "O" and board[4][4] == "O":
        print_board()
        print("PLAYER 2 WINS. GAME OVER!")
        break
    elif board[0][0] == "O" and board[2][2] == "O" and board[4][4] == "O" or board[0][4] == "O" and board[2][2] == "O" and board[4][0] == "O":
        print_board()
        print("PLAYER 2 WINS. GAME OVER!")
        break
