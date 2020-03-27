def implementacja(new_game_board):
	for y in range(3):
		for x in range(3):
			print("{:^5}".format(new_game_board[y][x]),end="")
			if x < 2:
				print("|",end="")
		if y<2:
			print("\n"+("-")*17)
		else:
			print()