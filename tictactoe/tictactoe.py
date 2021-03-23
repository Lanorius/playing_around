import sys
import random

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
def random_decision(f_s):
	return random.choice(f_s)

def perfect_decision(f_s=free_spots, X_s=X_spots, O_s=O_spots, b_p=bot_player):
	if 5 in f_s:
		return(5)
	elif

	
	else:
		return(f_s[0])

if current_player == "X":
	bot_turn = 1
else:
	bot_turn = 0

while(len(free_spots) != 0 and win == 0 and bot == "y"):
	show_field()

	if bot_turn == 0:
		print("\nThe Bots turn:")
		# new_value_bot = random_decision(free_spots)
		new_value_bot=perfect_decision(free_spots)
		starting_field[new_value_bot-1] = bot_player
		free_spots.remove(new_value_bot)

		bot_turn += 1

	else:
		new_value = int(input("\n"+"Player "+current_player+" choose a field: "))

		while new_value not in free_spots:
			print("Wrong input or spot already taken.")
			new_value = int(input("\n"+"Player "+current_player+" choose a field: "))

		bot_turn -= 1
		starting_field[new_value-1] = current_player
		free_spots.remove(new_value)

	winner, win = winning(starting_field)






#final lines
show_field()
if len(free_spots) == 0:
	print("Tie!")
else:
	print("The winner is "+winner+"!")