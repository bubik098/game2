def game_board(player1,player2,game):
	x=int(player1[0])
	y=int(player1[1])
	x1=int(player2[0])
	y1=int(player2[1])
	game[x-1][y-1]="X"
	game[x1-1][y1-1]="O"
	return game