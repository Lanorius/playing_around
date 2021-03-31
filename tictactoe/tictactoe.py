import sys
import random #only for random_bot

#player switcher
def player_switcher(cp):
	if cp == "X":
		return("O")
	elif cp == "O":
		return("X")
	else:
		return(None)

#starting variables
current_player = "X"
win = 0
winner = "temp"
free_spots = [1,2,3,4,5,6,7,8,9]
starting_field = ["1","2","3","4","5","6","7","8","9"]
X_spots = []
O_spots = []
player_spots = []
bot_spots = []

bot = None
bot_player = None

while bot not in ["y","n"]:
	bot = input("Would you like to play against a bot? y/n\n")

if bot == "y":
	while bot_player not in ["X","O"]:
		bot_player = player_switcher(input("Do you want to have the first (X) or second (O) turn?\n"))
		current_player = player_switcher(bot_player)


#play agaist a bot


def show_field():
	for i in range(len(starting_field)):
		if (i+1) % 3 == 1:
			print(starting_field[i]+"|"+starting_field[i+1]+"|"+starting_field[i+2])




#win conndition

def winning(starting_field):
	if starting_field[0] == starting_field[1] == starting_field[2]:
		return([starting_field[0], 1])
	elif starting_field[3] == starting_field[4] == starting_field[5]:
		return([starting_field[3], 1])
	elif starting_field[6] == starting_field[7] == starting_field[8]:
		return([starting_field[6], 1])
	elif starting_field[0] == starting_field[3] == starting_field[6]:
		return([starting_field[0], 1])
	elif starting_field[1] == starting_field[4] == starting_field[7]:
		return([starting_field[1], 1])
	elif starting_field[2] == starting_field[5] == starting_field[8]:
		return([starting_field[2], 1])
	elif starting_field[0] == starting_field[4] == starting_field[8]:
		return([starting_field[0], 1])
	elif starting_field[2] == starting_field[4] == starting_field[6]:
		return([starting_field[2], 1])
	else:
		return(["temp", 0])


#runnig the game against a friend
while(len(free_spots) != 0 and win == 0 and bot == "n"):
	show_field()


	new_value = int(input("\n"+"Player "+current_player+" choose a field: "))

	while new_value not in free_spots:
		print("Wrong input or spot already taken.")
		new_value = int(input("\n"+"Player "+current_player+" choose a field: "))


	free_spots.remove(new_value)
	starting_field[new_value-1] = current_player
	if current_player == "X":
		X_spots.append(new_value)
	else: 
		O_spots.append(new_value)
	print(X_spots, O_spots)
	current_player = player_switcher(current_player)
	winner, win = winning(starting_field)



#runnig the game against a bot
def random_decision():
	return random.choice(free_spots)

def perfect_decision():
	#print(starting_field)
	if 5 in free_spots:
		return(5)
	elif len(free_spots) == 1:
		return(free_spots[0])
	elif starting_field[5] != "5" and len(free_spots) == 8:
		return(random.choice([1,3,7,9]))

	#deadlock preventions:
	elif all(elem in player_spots for elem in [1,9]) and 4 in free_spots:
		return(4)
	elif all(elem in player_spots for elem in [3,7]) and 4 in free_spots:
		return(4)

	#all horizontal wins
	elif all(elem in bot_spots for elem in [1,2]) and 3 in free_spots:
		return(3)
	elif all(elem in bot_spots for elem in [1,3]) and 2 in free_spots:
		return(2)
	elif all(elem in bot_spots for elem in [2,3]) and 1 in free_spots:
		return(1)
	elif all(elem in bot_spots for elem in [4,5]) and 6 in free_spots:
		return(6)
	elif all(elem in bot_spots for elem in [4,6]) and 5 in free_spots:
		return(5)
	elif all(elem in bot_spots for elem in [5,6]) and 4 in free_spots:
		return(4)
	elif all(elem in bot_spots for elem in [7,8]) and 9 in free_spots:
		return(9)
	elif all(elem in bot_spots for elem in [7,9]) and 8 in free_spots:
		return(8)
	elif all(elem in bot_spots for elem in [8,9]) and 7 in free_spots:
		return(7)

	#all vectical wins
	elif all(elem in bot_spots for elem in [1,4]) and 7 in free_spots:
		return(7)
	elif all(elem in bot_spots for elem in [1,7]) and 4 in free_spots:
		return(4)
	elif all(elem in bot_spots for elem in [4,7]) and 1 in free_spots:
		return(1)
	elif all(elem in bot_spots for elem in [2,5]) and 8 in free_spots:
		return(8)
	elif all(elem in bot_spots for elem in [2,8]) and 5 in free_spots:
		return(5)
	elif all(elem in bot_spots for elem in [5,8]) and 2 in free_spots:
		return(2)
	elif all(elem in bot_spots for elem in [3,6]) and 9 in free_spots:
		return(9)
	elif all(elem in bot_spots for elem in [3,9]) and 6 in free_spots:
		return(6)
	elif all(elem in bot_spots for elem in [6,9]) and 3 in free_spots:
		return(3)

	#all diagonal wins
	elif all(elem in bot_spots for elem in [1,5]) and 9 in free_spots:
		return(9)
	elif all(elem in bot_spots for elem in [1,9]) and 5 in free_spots:
		return(5)
	elif all(elem in bot_spots for elem in [5,9]) and 1 in free_spots:
		return(1)
	elif all(elem in bot_spots for elem in [3,5]) and 7 in free_spots:
		return(7)
	elif all(elem in bot_spots for elem in [3,7]) and 5 in free_spots:
		return(5)
	elif all(elem in bot_spots for elem in [5,7]) and 3 in free_spots:
		return(3)

	#all horizontal preventions:
	elif all(elem in player_spots for elem in [1,2]) and 3 in free_spots:
		return(3)
	elif all(elem in player_spots for elem in [1,3]) and 2 in free_spots:
		return(2)
	elif all(elem in player_spots for elem in [2,3]) and 1 in free_spots:
		return(1)
	elif all(elem in player_spots for elem in [4,5]) and 6 in free_spots:
		return(6)
	elif all(elem in player_spots for elem in [4,6]) and 5 in free_spots:
		return(5)
	elif all(elem in player_spots for elem in [5,6]) and 4 in free_spots:
		return(4)
	elif all(elem in player_spots for elem in [7,8]) and 9 in free_spots:
		return(9)
	elif all(elem in player_spots for elem in [7,9]) and 8 in free_spots:
		return(8)
	elif all(elem in player_spots for elem in [8,9]) and 7 in free_spots:
		return(7)

	#all vectical preventions
	elif all(elem in player_spots for elem in [1,4]) and 7 in free_spots:
		return(7)
	elif all(elem in player_spots for elem in [1,7]) and 4 in free_spots:
		return(4)
	elif all(elem in player_spots for elem in [4,7]) and 1 in free_spots:
		return(1)
	elif all(elem in player_spots for elem in [2,5]) and 8 in free_spots:
		return(8)
	elif all(elem in player_spots for elem in [2,8]) and 5 in free_spots:
		return(5)
	elif all(elem in player_spots for elem in [5,8]) and 2 in free_spots:
		return(2)
	elif all(elem in player_spots for elem in [3,6]) and 9 in free_spots:
		return(9)
	elif all(elem in player_spots for elem in [3,9]) and 6 in free_spots:
		return(6)
	elif all(elem in player_spots for elem in [6,9]) and 3 in free_spots:
		return(3)

	#all diagonal preventions
	elif all(elem in player_spots for elem in [1,5]) and 9 in free_spots:
		return(9)
	elif all(elem in player_spots for elem in [1,9]) and 5 in free_spots:
		return(5)
	elif all(elem in player_spots for elem in [5,9]) and 1 in free_spots:
		return(1)
	elif all(elem in player_spots for elem in [3,5]) and 7 in free_spots:
		return(7)
	elif all(elem in player_spots for elem in [3,7]) and 5 in free_spots:
		return(5)
	elif all(elem in player_spots for elem in [5,7]) and 3 in free_spots:
		return(3)

	else:
		(print("should never happen"))
		return(free_spots[0])



if current_player == "X":
	bot_turn = 1
else:
	bot_turn = 0

while(len(free_spots) != 0 and win == 0 and bot == "y"):
	show_field()

	if bot_turn == 0:
		print("\nThe Bots turn:")
		# new_value_bot = random_decision()
		new_value_bot=perfect_decision()
		bot_spots+=[new_value_bot]
		starting_field[new_value_bot-1] = bot_player
		free_spots.remove(new_value_bot)

		bot_turn += 1

	else:
		new_value = int(input("\n"+"Player "+current_player+" choose a field: "))

		while new_value not in free_spots:
			print("Wrong input or spot already taken.")
			new_value = int(input("\n"+"Player "+current_player+" choose a field: "))

		bot_turn -= 1
		player_spots+=[new_value]
		starting_field[new_value-1] = current_player
		free_spots.remove(new_value)

	winner, win = winning(starting_field)


print(bot_spots, player_spots)



#final lines
show_field()
if len(free_spots) == 0:
	print("Tie!")
else:
	print("The winner is "+winner+"!")