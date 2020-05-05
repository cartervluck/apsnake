#Written by Carter Luck and David Carlip.
#All sections of code are written by the author of the code block unless specifically otherwise stated.
#Code blocks are specified in comments like so:
#START CODE BLOCK: CARTER LUCK
#{code}
#END CODE BLOCK
import pynput #Library 'pynput' by Moses Palmer

#START CODE BLOCK: CARTER LUCK
board = [['' for i in range(10)] for j in range(10)] #10 by 10 matrix of ''. Backwards indexing: board[y][x] to index board (just for ease of display)
fruitLocation = (0,0) #tuple for location of the fruit. (x,y)

def printBoard():
	print("|---------------------|")
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
	print("|---------------------|")
printBoard() #just to test
