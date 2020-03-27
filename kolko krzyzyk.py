from input_coordinate import*
from game_board import*
from implementacja import*
game=[[" "," "," "],[" "," "," "],[" "," "," "]]
# print(game)
list_spr=[]
licznik=0
while licznik<3:
	print("wprowadz dane dla player1")
	player1=input_coordinate()
	if player1 in list_spr:
		print("te dane juz były wprowadzane")
		continue
	else:
		list_spr.append(player1)
		print("wpowadz dane dla gracza2")
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
	licznik+=1

