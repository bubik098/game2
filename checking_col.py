def check_columns(new_game_board):
	for x in range(3): 
		if new_game_board[0][x]==new_game_board[1][x]==new_game_board[2][x] and new_game_board[0][x]!= " ":
			return new_game_board[0][x]