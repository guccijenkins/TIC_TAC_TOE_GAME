board = [['','|','','|',''],
            ['-------'],
        ['','|','','|',''],
            ['-------'],
        ['','|','','|','']]

board_positions = [[[1,1],[0,0]],[[1,2],[0,2]],[[1,3],[0,4]],
                   [[2,1],[2,0]],[[2,2],[2,2]],[[2,3],[2,4]],
                   [[3,1],[4,0]],[[3,2],[4,2]],[[3,3],[4,4]]]

print('\n')
print("Player 1 is 'X' and Player 2 is 'O'\n")
for i in board:
    print(*i)
print('\n')

player_1_input = []
player_1_row = int(input("Player 1, Please enter a row number (1, 2, or 3): "))
player_1_input.append(player_1_row)
player_1_column = int(input("Player 1, Please enter a column number (1, 2, or 3): "))
player_1_input.append(player_1_column)

for i in board_positions:
    if player_1_input == i[0]:
        inputted = i[1]
        board[inputted[0]].insert(inputted[1],"X")
        board_positions.remove(i)
        for i in board:
            print(*i)


# player_2_row = input("Player 2, Please enter a row number (1, 2, or 3: ")
# player_2_column = input("Player 2, Please enter a column number (1, 2, or 3: ")

