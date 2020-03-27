from input_coordinate import*
from game_board import*
from implementacja import*
from checking_row import*
from checking_col import*
from checking_diagonal import*
game=[[" "," "," "],[" "," "," "],[" "," "," "]]
# print(game)
list_spr=[]

licznik=0
while True:
	print("wprowadz dane dla player1")
	player1=input_coordinate()
	if player1 in list_spr:
		print("te dane juz były wprowadzane")
		continue
	else:
		list_spr.append(player1)
		print("wpowadz dane dla player2")
		player2=input_coordinate()
		if player2 in list_spr:
			print("te dane sie powtarzaja,zacznij od nowa")
			continue
		else:
			list_spr.append(player2)
		# print(list_spr)
	new_game_board=game_board(player1,player2,game)
	last_gamme_board=implementacja(new_game_board)
	print(last_gamme_board)
	winner=check_rows(new_game_board)
	winner1=check_columns(new_game_board)
	winner2=check_diagonal(new_game_board)
	if winner=="X" or winner1=="X" or winner2=="X":
		print("player1 has won!")
		exit=input("do you want to play again yes pr no?\n")
		if exit=="yes":
			list_spr=[]
			game=[[" "," "," "],[" "," "," "],[" "," "," "]]
			continue
		elif exit=="no":
			break
	elif winner=="O" or winner1=="O" or winner2=="O":
		print("player2 has won!")
		exit=input("do you want to play again yes or no?\n")
		if exit=="yes":
			list_spr=[]
			game=[[" "," "," "],[" "," "," "],[" "," "," "]]
			continue
		elif exit=="no":
			break
	

