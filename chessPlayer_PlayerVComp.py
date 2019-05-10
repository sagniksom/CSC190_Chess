from chessPlayer_tree import *
from chessPlayer_prune import *
from chessPlayer_eval import *
from chessPlayer_chess import *

board = [13,11,12,14,15,12,11,13,\
		10,10,10,10,10,10,10,10,\
		0,0,0,0,0,0,0,0,\
		0,0,0,0,0,0,0,0,\
		0,0,0,0,0,0,0,0,\
		0,0,0,0,0,0,0,0,\
		20,20,20,20,20,20,20,20,\
		23,21,22,24,25,22,21,23]

def compMove(board,player):
	max_depth = 1
	eval_score = getScore(board,player)
	root = treenode(eval_score, [], board)	
	buildTree(root,player,0,max_depth)
	bestval = minimax(root,max_depth,0,True,-float("inf"),float("inf"))
	move = suggestMove(root, bestval)
	return move

print "INFO: Type in STOP to end program"
done = False
player = input("Select Player (10 for White; 20 for Black): ")
printBoard(board)
if int(player)==10:
	while True:
		start_pos = input('Enter Position of the Piece You Want to Move: ')
		if input=='STOP':
			break
		if board[start_pos] in range (player,player+10):
			if GetPieceLegalMoves(board,start_pos):
				end_pos = input('Enter Position You Want the Piece to Go: ')
				if end_pos in GetPieceLegalMoves(board,start_pos):
					board[end_pos] = board[start_pos]
					board[start_pos] = 0
					printBoard(board)
					break
		print 'Try Again'	

while not done:
	#Computer's Move
	move = compMove(board,player%20+10)
	board[move[1]]=board[move[0]]
	board[move[0]]=0
	printBoard(board)
	#Ask Player for Move
	while True:	
		start_pos = input('Enter Position of the Piece You Want to Move: ')
		if input=='STOP':
			break
		if board[start_pos] in range (player,player+10):
			if GetPieceLegalMoves(board,start_pos):
				end_pos = input('Enter Position You Want the Piece to Go: ')
				if end_pos in GetPieceLegalMoves(board,start_pos):
					board[end_pos] = board[start_pos]
					board[start_pos] = 0
					printBoard(board)
					break
		print 'Try Again'
