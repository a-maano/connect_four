import os
import assets as a

def showBoard(grid):
	print(" 1  2  3  4  5  6  7")
	for line in grid:
		print(line)

def resizeTerminal(row,col):
	print('\x1b[8;{0};{1}t'.format(row, col), end='', flush=True)

def drop(slot, player, grid):
	if len(slot) > 1 or not slot.isnumeric() or int(slot)-1 >= 7:
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


def checkWinner(grid, player, slot):
	y = int(slot)-1
	x = -1
	colstr = ""

	# get column and getting the x
	for i in range(6):
		colstr = colstr + str(grid[i][y])
		if grid[i][y] != player:
			continue
		elif x == -1 and grid[i][y] == player:
			x = i
	# get row
	rowstr = ''.join(map(str,grid[x]))

	# get \ diag
	adiag = ""
	smaller = min(x,y)
	xs = x-smaller
	ys = y-smaller
	while(1):
		adiag = adiag + str(grid[xs][ys])
		xs = xs + 1
		ys = ys + 1

		if xs > 5 or ys > 6:
			break

	# get / diag
	bdiag = "" 	# /
	yz = x + y
	xz = 0
	if yz > 6:
		xz = yz - 6
		yz = 6
	while(1):
		bdiag = bdiag + str(grid[xz][yz])
		xz = xz + 1
		yz = yz - 1

		if xz > 5 or yz < 0:
			break

	# check if 4 consecutive exists
	win = str(player)*4
	if (win in rowstr) or (win in colstr) or (win in adiag) or (win in bdiag):
		return True
	else:
		return False
	# print("row: ", rowstr)
	# print("col: ", colstr)
	# print("adiag: ", adiag)
	# print("bdiag: ", bdiag)


def designBoard(grid):

	print(a.title)
	print(a.number_label)
	for line in grid:
		for c in range(3):
			for cell in line:
				print("\t", end="")
				if cell == 1:
					print(a.p1[c], end=" ")
				elif cell == 2:
					print(a.p2[c], end=" ")
				else:
					print(a.p0, end=" ")
			print()
		print()
	



grid = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
player = 0
details = "Player " + str(player + 1) + " turn"
result = False
resizeTerminal(40,69) #row, col
while (1):
	os.system('cls' if os.name == 'nt' else 'clear')
	# showBoard(grid)
	designBoard(grid)
	print(details)
	if result: break
	print("Enter slot #: ", end="")
	slot = str(input())
	details = drop(slot, player+1, grid)

	if details == None:
		result = checkWinner(grid, player+1, slot)
		if result == False:
			player = (player + 1) % 2
			details = "Player " + str(player + 1) + " turn"
		else:
			details = "Player " + str(player + 1) + " wins!"
