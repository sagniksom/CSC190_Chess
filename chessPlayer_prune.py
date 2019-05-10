from chessPlayer_eval import *
from chessPlayer_tree import * 
def max(a,b):
	if a>=b:
		return a
	else: 
		return b

def min(a,b):
	if a<=b:
		return a
	else:
		return b

def buildTree(node, player, depth, max_depth):
	if depth==max_depth:
		return True
	if node.LegalMoves == []:
		node.getLegalMoves(player)
	for i in node.LegalMoves:
		new_board = list(node.board)
		new_board[i[1]] = new_board[i[0]]
		new_board[i[0]] = 0
		eval_score = getScore(new_board,player)
		SuccessorNode = treenode(eval_score, node.move, new_board)
		SuccessorNode.addMove(i)
		node.AddSuccessor(SuccessorNode)
		buildTree(SuccessorNode, player, depth+1, max_depth)
	return True




def minimax(node, max_depth, depth, isMaximizingPlayer, alpha, beta):
	if node.LegalMoves == []: #this is leaf node
		return node.eval
	if depth==max_depth:
		return node.eval
	if isMaximizingPlayer:
		bestVal = -float("inf")
		for i in node.Successor:
			value = minimax(i,max_depth, depth+1, False, alpha, beta)
			bestVal = max(bestVal, value)
			alpha = max(alpha, bestVal)
			i.eval = bestVal
			if beta <= alpha:
				break
		return bestVal
	else:
		bestVal = +float("inf")
		for i in node.Successor:
			value = minimax(i,max_depth, depth+1, True, alpha, beta)
			bestVal = min(bestVal, value)
			beta = min(beta, bestVal)
			i.eval = bestVal
			if beta <= alpha:
				break
		return bestVal

#Use suggestMove after tree built, minimax score obtained
def suggestMove(node, minimax_score):
	for i in node.Successor:
		if i.eval==minimax_score:
			return i.move
	return False

