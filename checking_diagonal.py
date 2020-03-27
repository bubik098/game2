def check_diagonal(new_game_board):
	if new_game_board[1][1]!= " ":
		if new_game_board[1][1]==new_game_board[0][0]==new_game_board[2][2]: 
			return new_game_board[1][1]
		elif new_game_board[1][1]==new_game_board[0][2]==new_game_board[2][0]:
			return new_game_board[1][1]