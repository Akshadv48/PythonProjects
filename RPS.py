from random import randint

def main():
	player = input('Stone(r),Paper(p) OR Scissors(s): ')
	chosen = randint(1,3)
	if chosen == 1:
		computer = 's'
	elif chosen == 2:
		computer = 'r'
	else:
		computer = 'p'

	if computer == player:
		print('Draw')
	elif computer == 's' and player == 'r' or computer == 'r' and player == 'p' or computer == 'p' and player == 's':
		print('Player Wins')
	else:
		print('Computer Wins')	
if __name__ == '__main__':
	main()





	