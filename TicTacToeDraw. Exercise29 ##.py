game = [[' * ', ' * ', ' * '],
		[' * ', ' * ', ' * '],
		[' * ', ' * ', ' * ']]


def check_if_won():
	'''check draw'''
	D = 0
	zz = 0
	for i in range(3):
	
		x = game[zz].count(" X ")
		zz += 1	
		D += x
	if D >= 5:
		print("It's a Draw!!!")
		new_game()
	'''Horezontal'''
	if game[0][0] == game[0][1] == game[0][2] == ' X ':
		print("Player ONE have won 'Horizontal' ")
		new_game()
	if game[0][0] == game[0][1] == game[0][2] == ' O ':
		print("Player Two have won 'Horizontal' ")
		new_game()
	if game[1][0] == game[1][1] == game[1][2] == ' X ':
		print("Player ONE have won 'Horizontal' ")
		new_game()
	if game[1][0]  == game[1][1]  == game[1][2] == ' O ':
		print("Player Two have won 'Horizontal' ")
		new_game()
	if game[2][0] == game[2][1] == game[2][2] == ' X ':
		print("Player ONE have won 'Horizontal' ")
		new_game()
	if game[2][0]  == game[2][1]  == game[2][2] == ' O ':
		print("Player Two have won 'Horizontal' ")
		new_game()

	'''Vertical'''
	if game[0][0] == game[1][0] == game[2][0] == ' X ':
		print("Player ONE have won 'Vertical' ")
		new_game()
	if game[0][0] == game[1][0] == game[2][0] == ' O ':
		print("Player Two have won 'Vertical' ")
		new_game()

	if game[0][1] == game[1][1] == game[2][1] == ' X ':
		print("Player ONE have won 'Vertical' ")
		new_game()
	if game[0][1]  == game[1][1]  == game[2][1] == ' O ':
		print("Player Two have won 'Vertical' ")
		new_game()
		
	if game[0][2] == game[1][2] == game[2][2] == ' X ':
		print("Player ONE have won 'Vertical' ")
		new_game()
	if game[0][2]  == game[1][2]  == game[2][2] == ' O ':
		print("Player Two have won 'Vertical' ")
		new_game()

	'''Diagonal'''
	if game[0][0] == game[1][1] == game[2][2] == ' X ':
		print("Player ONE have won 'Diagonal' ")
		new_game()
	if game[0][0] == game[1][1] == game[2][2] == ' O ':
		print("Player Two have won 'Diagonal' ")
		new_game()

	if game[0][2] == game[1][1] == game[2][0] == ' X ':
		print("Player ONE have won 'Diagonal' ")
		new_game()
	if game[0][2]  == game[1][1]  == game[2][0] == ' O ':
		print("Player Two have won 'Diagonal' ")
		new_game()
		

def enter_XandO():
	
	times = 5
	while times > 0:
		row = int(input("Player ONE Enter (in the format row,col), ROW - "))
		col = int(input("Player ONE Enter (in the format row,col), COL - "))
		if game[row-1][col-1] != ' O ':
			game[row-1][col-1] = ' X '
		
		print(*game, sep = "\n")
		check_if_won()
		
		row = int(input("Player TWO Enter (in the format row,col), ROW - "))
		col = int(input("Player TWO Enter (in the format row,col), COL - "))
		if game[row-1][col-1] != ' X ':
			game[row-1][col-1] = ' O '
		print(*game, sep = "\n")
		check_if_won()
		
		times -= 1
	if times == 0:
		print("IT IS A DRAW")
		

def new_game():	
	game = [[' * ', ' * ', ' * '],
			[' * ', ' * ', ' * '],
			[' * ', ' * ', ' * ']]
	print('\n', '\n')
	print("New game have started! This is your game board")
	print(*game, sep = "\n")
	print("Welcome to Tic Tac Toe! Enter where you want to put your X or O")
	enter_XandO()
	
new_game()
