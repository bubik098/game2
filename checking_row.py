def check_rows(new_game_board):
	for x in range(3):
		if new_game_board[x][0]==new_game_board[x][1]==new_game_board[x][2] and new_game_board[x][0]!=" ":
			return new_game_board[x][0]
			