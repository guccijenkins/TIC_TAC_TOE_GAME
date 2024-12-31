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

removed_positions = []

def print_board():
    print('\n')
    print("Player 1 is 'X' and Player 2 is 'O'\n")
    for i in board:
        print(*i)
    print('\n')

def player_1():
    global board
    global board_positions
    global removed_positions
    player_1_input = []
    player_1_row = int(input("Player 1, Please enter a row number (1, 2, or 3): "))
    player_1_input.append(player_1_row)
    player_1_column = int(input("Player 1, Please enter a column number (1, 2, or 3): "))
    player_1_input.append(player_1_column)

    for r in removed_positions:
        if r == player_1_input:
            print("That position is already taken on the board. Please re-enter a position.")
            player_1_input.clear()
            player_1()

    for i in board_positions:
        if player_1_input == i[0]:
            inputted = i[1]
            board[inputted[0]].insert(inputted[1], "X")
            board[inputted[0]].pop(inputted[1] + 1)
            removed_positions.append(player_1_input)

def player_2():
    global board
    global board_positions
    global removed_positions
    player_2_input = []
    player_2_row = int(input("Player 2, Please enter a row number (1, 2, or 3): "))
    player_2_input.append(player_2_row)
    player_2_column = int(input("Player 2, Please enter a column number (1, 2, or 3): "))
    player_2_input.append(player_2_column)

    for r in removed_positions:
        if r == player_2_input:
            print("That position is already taken on the board. Please re-enter a position.")
            player_2_input.clear()
            player_2()

    for i in board_positions:
        if player_2_input == i[0]:
            inputted = i[1]
            board[inputted[0]].insert(inputted[1], "O")
            board[inputted[0]].pop(inputted[1] + 1)
            removed_positions.append(player_2_input)

game_on = True
while game_on:
    print_board()
    player_1()
    print_board()
    player_2()