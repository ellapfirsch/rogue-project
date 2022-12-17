from os import system
import random
import time

import curses, time
class Information:
	def __init__(self):
		self.score = 0
		self.lives = 0
		
class Coordinates:
  def __init__(self):
    self.x = 0
    self.y = 0 

###################################################
def InputChar(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): 
                break
            time.sleep(0.05)
    finally:
        curses.endwin()
    return chr(ch)
###################################################
def CreateGrid():
	
	Grid = []
	Width = input("choose the width of the arena  :  ")
	while not(Width.isdigit()) or int(Width) < 5 or int(Width) > 10 or Width == "":
		Width = input("This number is not suitable, width of the grid :  ")
	Width = int(Width)
	Height = input("choose the height of the arena : ")
	while not(Height.isdigit()) or int(Height) < 5 or int(Height) > 10 or Height == "":
		Height = input("This number is not suitable, Height of the grid :  ")
	Height = int(Width)
	for i in range(Height):
		Grid.append([])
		for x in range(Width):
			Grid[i].append(" ")
	
	CreateMaze(Grid)

			
	Player = Coordinates()
	Player.x = random.randint(0, Width-1)
	Player.y = random.randint(0, Height-1)
	Grid[Player.y][Player.x] = "P"
 	
	system('clear')
	return Grid, Width, Height, Player

#############################################	
def CreateMaze(Grid):
	
	for i in range(len(Grid)- 1):
		for x in range(len(Grid[i])-1 ):
			if (x+ 1 != len(Grid[i]) ) and (i+1 < len(Grid)) and (i > 0):
				
				if ((Grid[i][x + 1] == " ") and (Grid[i+1][x] == " "))or ((Grid[i-1][x]== " ") and (Grid[i+1][x] == " ")) or (Grid[i-1][x] == " " or Grid[i][x+1] == " "):
					flag = random.randint(1,2)
					
					
					if flag == 1:
						print(flag)
						Grid[i][x] = "▪️"

	return Grid

########################################
def OutputGrid(Grid, Width, Height, PlayerInfo):
	
	print("score : " + str(PlayerInfo.score))
	print("lives : " + str(PlayerInfo.lives))
	print()
	
	print("|" + "🟩" * (len("|🟩|"+ "--"* (Width-1)+ "-" + "|🟩|") // 2) + " |")
	for row in range(0, Height , 1): 
		print( "|🟩|" + "--"* (Width-1)+ "-" + "|🟩|")
		print("|🟩|", end="")
		for column in range(0, Width , 1):
			if Grid[row][column] == " " :
				print((Grid[row][column]) + "|" , end='')
			else:
				print(Grid[row][column] + "|", end="")
		print("🟩|\n", end="")
	print("|🟩|" + "--"* (Width - 1) + "-" + "|🟩|")
	print("|" + "🟩" * (len("|🟩|"+ "--"* (Width-1)+ "-" + "|🟩|") // 2) + " |")

 
##############################################
def SetScore():
	PlayerInfo = Information()
	PlayerInfo.score = 0
	PlayerInfo.lives = 5
	return PlayerInfo
#################################################
def IncrementScore(PlayerInfo):
	PlayerInfo.score += 1
	return PlayerInfo

###############################################
def DecrementLives(PlayerInfo):
	PlayerInfo.lives -= 1
	return PlayerInfo

##############################################
def SetGold(Player, Width, Height, Grid):
	Gold = Coordinates()
	Gold.x = random.randint(0, Width-1)
	while Player.x ==  Gold.x:
		Gold.x = random.randint(0, Width-1)
	Gold.y = random.randint(0, Height-1)
	while Player.y == Gold.y:
		Gold.y = random.randint(0, Height-1)

	Grid[Gold.y][Gold.x] = "G"
	return Gold, Grid
		
			
################################################
def StartingPage():
	TextDelay("\033[1;32m Hello Player! welcome to \033[1;32m",)
	TextDelay(""" \033[1;32m _____   ____   _____ _    _ ______ 
 |  __ \ / __ \ / ____| |  | |  ____|
 | |__) | |  | | |  __| |  | | |__   
 |  _  /| |  | | | |_ | |  | |  __|  
 | | \ \| |__| | |__| | |__| | |____ 
 |_|  \_\\____/ \_____|\____/|______|
                                     \033[1;32m""")
	TextDelay("Come join forces with us to fight our evil space enemies")
	TextDelay("Press the letter 'Y' if you want to join us")
	Ready = input()
	if Ready.upper() == "Y":
		TextDelay("Ok, get ready becaue we are flying to rogue soon")
	file = open("topscores.txt", "r")
	print("!!!OUR TOP SCORES!!!")
	topscores = file.read()
	topscores = topscores.split(",")
	for x in range(0, len(topscores), 2):
		print(topscores[x] + (" " * (6 - len(topscores[x])) +": " + topscores[x + 1]))
		
	time.sleep(2)
	system('clear')
###############################################
def TextDelay(Text):
	for i in Text:
		print(i, end="" )
		time.sleep(0.01)
	print("")

#############################################

#######################################
def MovePlayer(Player, Grid, Width, Height, PlayerInfo, Gold):
	OutputGrid(Grid, Width, Height, PlayerInfo)
	
	Next = Coordinates() 
	
	Grid[Player.y][Player.x] = " "
	time.sleep(3)
	char = ""
	while char.lower() != "q":
		Next.y = Player.y
		Next.x = Player.x
		OutputGrid(Grid, Width, Height, PlayerInfo)
		char = (InputChar(""))
		
		Grid[Player.y][Player.x] = " "
		
		Grid[Player.y][Player.x] = " "
		if char.lower() == "w" and (Player.y ) != 0 and (Player.y - 1 == ' '):
			Player.y -= 1
		elif char.lower() == "w" and Player.y -1 != " " and Player.y != 0 : 
			Next.y = Player.y - 1
		elif char.lower() == "w":
			print("player cannot go above the grid")
		if char.lower() == "a" and Player.x != 0 and Player.x -1 == " ":
			Player.x -= 1
		elif char.lower() == "a":
			print("player cannot go to the left of the gid")
		if char.lower() == "s" and Player.y + 1 < Height and Player.y + 1 == " ":
			Player.y += 1
		elif char.lower() == "s":
			print("player cannot go bellow the grid")
		if char.lower() == "d" and Player.x + 1 < Width and Player + 1 == " ":
			Player.x += 1
		elif char.lower() == "d":
			print("Player cannot go to the right of the grid")
		
		
		if char.lower() != "w" and char.lower() != "a" and char.lower() != "s" and char.lower() != "d":
			print("invalid character")
			
		
		
		Grid[Player.y][Player.x] = "P"
		
		time.sleep(2)
		system('clear')

###########################################################
def CheckManhattanDistance(Player, Gold):
	xdifference = abs(Player.x - Gold.x)
	ydifference = abs(Player.y - Player.y)
	return xdifference, ydifference
	
#########################################################
def CheckNext(Player, Grid, Gold, key, Next ):
	if key == "w":
		if Player.y - 1 < 0:
			Player.y = Player.y
		elif Grid[Player.y - 1][Player.x] == 0
##################################################

def instructions():
	TextDelay("On the planet rogue an evil inlfluence has arrived ... ")
	print()
	TextDelay("Evil monsters are infiltrating our planet and it is your job as a hero to stop it")
	print()
	TextDelay("we need your help. Help us find out gold our enemies have stolen from us and defeat them.")
	print()
	TextDelay("Use the WASD keyboard to move the Player which is indicated with the letter P")
	time.sleep(5)
	system('clear')
	
###############################################Y
def main():
	StartingPage()
	instructions()
	PlayerInfo = SetScore()
	Grid, Width, Height, Player = CreateGrid()
	Gold, Grid = SetGold(Player, Width, Height, Grid)

	MovePlayer(Player, Grid, Width, Height, PlayerInfo, Gold)
main()

