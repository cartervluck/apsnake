#Written by Carter Luck and David Carlip.
#All sections of code are written by the author of the code block unless specifically otherwise stated.
#Code blocks are specified in comments like so:
#START CODE BLOCK: CARTER LUCK
#{code}
#END CODE BLOCK
import pynput #Library 'pynput' by Moses Palmer
import random #Library 'random' from python standard library by Python Software Foundation
import time #Library 'time' from python standard library by Python Software Foundation

#START CODE BLOCK: CARTER LUCK
board = [['' for i in range(20)] for j in range(20)] #10 by 10 matrix of ''. Backwards indexing: board[y][x] to index board (just for ease of display)
fruitLocation = (0,1) #tuple for location of the fruit. (x,y)
playing = True

def printBoard():
	global snake
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	border = "-".join(["|"] + ["-" for i in range(len(board[0]))] + ["|"])
	print(border)
	for i in range(len(board)):
		printstring = ["|"]
		for j in range(len(board[i])):
			if fruitLocation == (j,i):
				printstring.append("O")
			elif (j,i) in snake:
                                printstring.append("X")
			else: #TODO:
				printstring.append(" ")
		printstring.append("|")
		printstring = " ".join(printstring)
		print(printstring)
	print(border)
#END CODE BLOCK


#START CODE BLOCK: DAVID CARLIP

snakeLength = 1
direction = "up"
#snake consists of a list of coordinates (tuples) that the snake takes up, with the lower indices more recent
snake = [(len(board) / 2, len(board) / 2)]

def checkFruit():
    global snakeLength
    global fruitLocation
    if snake[0] == fruitLocation:
        fruitLocation = (random.randint(0, len(board)-1), random.randint(0, len(board)-1)) #LINE EDITED BY CARTER LUCK FOR LOGIC
        snakeLength += 1

def updateSnake():
    global snake
    xCoord = snake[0][0]
    yCoord = snake[0][1]
    if direction == "up":
        yCoord -= 1
    elif direction == "down":
        yCoord += 1
    elif direction == "left":
        xCoord -= 1
    elif direction == "right":
        xCoord += 1
    if (xCoord not in range(len(board)) or 
          yCoord not in range(len(board)) or
          (xCoord,yCoord) in [snake[i] for i in range(len(snake))]): #LINE EDITED BY CARTER LUCK FOR SLIGHT LOGIC FIX
        gameOver()


    snake.insert(0, (xCoord, yCoord))
    checkFruit()
    snake = snake[0:snakeLength]
    
        

def onPress(key):
    global direction
    if key == pynput.keyboard.Key.esc:
        return False
    else:
        direction = key.__str__().split(".")[1]


#END CODE BLOCK

#START CODE BLOCK: CARTER LUCK
#TODO: Implement behavior
def gameOver():
    global playing
    playing = False

listener = pynput.keyboard.Listener(
    on_press=onPress,
    on_release=lambda x: None)
listener.start()

#TODO: Add to main game loop
while playing:
    updateSnake()
    printBoard()
    time.sleep(0.25)

#game has ended, show end screen
endtext = ["|---------------------|",
"|                     |",
"|      GAME OVER      |",
"|                     |",
"".join(["|    YOUR SCORE: ",str(len(snake)),] + [" " for i in range(5-len(str(len(snake))))] + ["|"]),
"|                     |",
"|---------------------|"]

for j in range(len(endtext)):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for q in range(j+1):
        print(endtext[q])
    time.sleep(0.25)
