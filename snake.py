#Written by Carter Luck and David Carlip.
#All sections of code are written by the author of the code block unless specifically otherwise stated.
#Code blocks are specified in comments like so:
#START CODE BLOCK: CARTER LUCK
#{code}
#END CODE BLOCK
import pynput #Library 'pynput' by Moses Palmer
import random #Library 'random' from python standard library by Python Software Foundation

#START CODE BLOCK: CARTER LUCK
board = [['' for i in range(20)] for j in range(20)] #10 by 10 matrix of ''. Backwards indexing: board[y][x] to index board (just for ease of display)
fruitLocation = (0,1) #tuple for location of the fruit. (x,y)

def printBoard():
	border = "-".join(["|"] + ["-" for i in range(len(board[0]))] + ["|"])
	print(border)
	for i in range(len(board)):
		printstring = ["|"]
		for j in range(len(board[i])):
			if fruitLocation == (j,i):
				printstring.append("O")
			else: #TODO: PRINT X IF PART OF SNAKE IS HERE
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
        fruitLocation = (random.randint(0, len(board)), random.randint(0, len(board)))
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
          xCoord in [snake[i][0] for i in range(len(snake))] or 
          yCoord in [snake[i][1] for i in range(len(snake))]):
        gameOver()


    snake.insert(0, (xCoord, yCoord))
    checkFruit()
    print(direction)
    print(xCoord)
    snake = snake[0:snakeLength]
    print(snake)
    
        

def onPress(key):
    global direction
    if key == pynput.keyboard.Key.esc:
        return False
    else:
        direction = key.__str__().split(".")[1]


#END CODE BLOCK

#TODO: Implement behavior
def gameOver():
    return


#TODO: Add to main game loop
#    updateSnake()
#    listener = pynput.keyboard.Listener(
#        on_press=onPress,
#        on_release=lambda x: None)
#    listener.start()
