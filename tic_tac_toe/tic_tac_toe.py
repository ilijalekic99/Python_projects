from random import choice 
from time import sleep

print()

def Welcome():
	print('***** WELCOME TO TIC TAC TOE GAME *****')
	sleep(1)
	print()
	print('Computer will decide who will play first!')
	print()
	print('If you need a hint \npress any of these [Hint,hint,H,h]')
	sleep(1)
	print()

	print(''' *****Format of Game*****
		  |   |		  1	| 2 | 3
	       - - - - - -          - - - - - -
	    	  |   |		  4	| 5 | 6
	       - - - - - -          - - - - - -
	   	  |   |		     7 	| 8 | 9
				''')
def DrawBoard(board,NeedSleep=True):
	if NeedSleep:
		sleep(1)
	print()
	print(' 		'+board[1]+' 	|	'+board[2]+' 	|	'+board[3])
	print('			--------------------------------------------------')
	print(' 		'+board[4]+' 	|	'+board[5]+' 	|	'+board[6])
	print('			--------------------------------------------------')
	print(' 		'+board[7]+' 	|	'+board[8]+' 	|	'+board[9])
	print()

def InputPlayerLetter():
	letter=''
	while not(letter == 'X' or letter == 'O'):
		print('Do you want to be X or O')
		letter = input().upper()

	if letter == 'X':
		return ['X','O']
	if letter == 'O':
		return ['O','X']

def WhoFirst():
	opponents = ['computer','player']
	if choice(opponents) == 'computer':
		return 'computer'
	else:
		return 'player'

def PlayAgain():
	print('Do you want to play again (y or n)')
	playagain = input().lower().startswith('y')
	return playagain

def MakeMove(board,letter,move):
	board[move] = letter

def IsWinner(board,letter):
	return(  (board[7] == letter and board[8] == letter and board[9] == letter) or
			 (board[4] == letter and board[5] == letter and board[6] == letter) or
			 (board[1] == letter and board[2] == letter and board[3] == letter) or
			 (board[1] == letter and board[4] == letter and board[7] == letter) or
			 (board[2] == letter and board[5] == letter and board[8] == letter) or
			 (board[3] == letter and board[6] == letter and board[9] == letter) or
			 (board[1] == letter and board[5] == letter and board[9] == letter) or
			 (board[3] == letter and board[5] == letter and board[7] == letter) )

def GetBoardCopy(board):
	DupeBoard = []
	for i in board:
		DupeBoard.append(i)
	return DupeBoard

def IsSpaceFree(board,move):
	return board[move] == ''

def GetPlayerMove(board):
	move = ''

	while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board,int(move)):
		print('Enter your move (1-9)')
		move = input()
		if move in HintInput:
			return move
			break
		return int(move)

def ChooseRandomFromList(board,MoveList):
	PossibleMoves = []
	for i in MoveList:
		if IsSpaceFree(board,i):
			PossibleMoves.append(i)
	if len(PossibleMoves) != 0:
		return choice(PossibleMoves)
	else:
		return None

def GetComputerMove(board,ComputerLetter):
	if ComputerLetter == 'X':
		PlayerLetter = 'O'
	else:
		PlayerLetter = 'X'

	for i in range(1,10):
		copy = GetBoardCopy(board)
		if IsSpaceFree(copy,i):
			MakeMove(copy,ComputerLetter,i)
			if IsWinner(copy,PlayerLetter):
				return i
	for i in range(1,10):
		copy = GetBoardCopy(board)
		if IsSpaceFree(copy,i):
			MakeMove(copy,ComputerLetter,i)
			if IsWinner(copy,PlayerLetter):
				return i

	move = ChooseRandomFromList(board,[1,3,7,9])
	if move != None:
		return move

	if IsSpaceFree(board,5):
		return 5

	return ChooseRandomFromList(board,[2,4,6,8])

def IsBoardFull(board):
	for i in range(1,10):
		if IsSpaceFree(board,i):
			return False
	return True

def FinalBoard(board,NeedSleep=True):
	print('            |-------------|')
	DrawBoard(board,NeedSleep)
	print('            |-------------|')


Welcome()
while True:

	TheBoard = [' '] * 10
	PlayerLetter,ComputerLetter = InputPlayerLetter()
	turn = WhoFirst()
	print(f'The {turn} will go first')

	Playing = True
	while Playing:
		if turn == 'player':
			print(f"  Turn => {turn}")
			HintInput = ['Hint','hint','H','h']

			move = GetPlayerMove(TheBoard)

			while move in HintInput:
				HintBox.append(i)
				for i in TheBoard:
					HintBox.append(i)
				hint = GetComputerMove(HintBox,PlayerLetter)
				MakeMove(HintBox,PlayerLetter,hint)
				print(f'HINT : placing at {hint} is better')
				FinalBoard(HintBox,False)
				move = GetPlayerMove(TheBoard)
			MakeMove(TheBoard,PlayerLetter,move)

			if IsWinner(TheBoard,PlayerLetter):
				FinalBoard(TheBoard)
				print('You have WON the game')
				Playing = not Playing
			elif IsBoardFull(TheBoard):
				FinalBoard(TheBoard)
				print('The game is TIE\nIts good to PLAY untill you WIN')
				Playing = not Playing
			else:
				DrawBoard(TheBoard)
				turn = 'computer'
		else:
			print(f"  Turn => {turn}")
			print('Computer is thinking...')
			move = GetComputerMove(TheBoard,ComputerLetter)
			MakeMove(TheBoard,ComputerLetter,move)

			if IsWinner(TheBoard,ComputerLetter):
				FinalBoard(TheBoard)
				print('Try again bro you will win')
				Playing = not Playing
			elif IsBoardFull(TheBoard):
				FinalBoard(TheBoard)
				print('The game is TIE\nIts good to PLAY untill you WIN')

			else:
				DrawBoard(TheBoard)
				turn = 'player'

		if not PlayAgain():
			break