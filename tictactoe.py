# Grid

above_line = '1|2|3'
center_line = '4|5|6'
last_line = '7|8|9'
dashes = '_ _ _'

#start

def start():
	print(' Tic-Tac-Toe ')
	print('  Welcome ')
	userinput = input('Do u want to play Tic-Tac-Toe[y/n]: ')

	if userinput.lower() == "y":
		print('you started')
		game(above_line, center_line, last_line,dashes)
	else:
		print('Byee!')

def game(above_line, center_line,last_line,dashes):
	print(above_line)
	print(dashes)
	print(center_line)
	print(dashes)
	print(last_line)




start()