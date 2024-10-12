import os




def showBoard(grid):
	print(" 1  2  3  4  5  6  7")
	for line in grid:
		print(line)

def drop(slot, player, grid):


	if len(slot) > 1 or not slot.isnumeric() or int(slot)-1 >=7:
		return "Invalid input! Try again Player " + str(player)
	else:
		slot = int(slot)-1
		for i in range(6):
			if i == 0 and grid[i][slot] != 0:
				return "Column full! Try again Player " + str(player)

			else:
				
				if i == 5 and grid[i][slot] == 0:	# bottom of board and empty
					grid[i][slot] = player
				elif grid[i][slot] == 0 and grid[i+1][slot] != 0:	# current cell empty and next cell occupied
					grid[i][slot] = player
				else:
					continue

grid = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]



player = 0
details = "Player " + str(player + 1) + " turn"
while (1):
	os.system('cls' if os.name == 'nt' else 'clear')
	showBoard(grid)
	print(details)
	# print("Enter player #: ", end="")
	# player = int(input())	
	print("Enter slot #: ", end="")
	slot = str(input())
	details = drop(slot, player+1, grid)
	if details == None:
		player = (player + 1) % 2
		details = "Player " + str(player + 1) + " turn"




# ◜◝
# ◞

# ◠
# ◡
# ⚉

# ◯

#  ▮ ◾ ▗ ▖ ■ ∎ ▃ ▄ ▅ ▆ ▇ █ ▌ ▐ ▍ ▎ ▉ ▊ ▋ ❘ ❙ ❚ ▀ ▘ ▝ ▙ ▚ ▛ ▜ ▟ ▞
#   ▮ ◾ ▗ ▖ ■ ∎ ▃ ▄ ▅ ▆ ▇ █ ▌ ▐ ▍ ▎ ▉ ▊ ▋ ❘ ❙ ❚ ▀ ▘ ▝ ▙ ▚ ▛ ▜ ▟ ▞

#   ⋀ ⋁ ⋂ ⋃
#   ⋀ ⋁ ⋂ ⋃

#   ⋐ ⋑ ⋒ ⋓
#   ⋐ ⋑ ⋒ ⋓


#   ⎛ ⎠ ⎝ ⎞
#   ⎛ ⎠ ⎝ ⎞

#   ⎟ ⎢ ⎥ ⎪ ꞁ ⎮ ⎧ ⎫ ⎩ ⎭
#   ⎟ ⎢ ⎥ ⎪ ꞁ ⎮ ⎧ ⎫ ⎩ ⎭

#   ⁔ 

#   ⚂
#   ⚂⚂


#   ╦║╬

#   ═║╦	
#   ╩  ║

#   ╔





# a = '''
# ░░░░░ █████ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ░░░░░ █████ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ░░░░░ █████ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 

# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 

# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 

# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 

# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 

# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ 
# '''