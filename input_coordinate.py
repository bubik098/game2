def input_coordinate():
	while True:
		coordinate=input("input coordinates for ex. 1,2\n")
		lista=coordinate.split(",")
		if len(lista)==2:
			if 0<int(lista[0])<4 and 0<int(lista[1])<4:
				return lista
				break
			elif int(lista[0])==0 or int(lista[1])==0:
				print("nie moze byc 0")
				continue
		if len(lista)==2:
			if int(lista[0])>3 or int(lista[1])>3:
				print("to big numbers")
		elif len(lista)>2:
			print("wrong input")
		else:
			print("wrong input")