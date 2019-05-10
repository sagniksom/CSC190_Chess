from chessPlayer_chess import *

class queue(object):
	def __init__(self):
		self.store=[]
	def push(self,val):
		self.store=self.store+[val]
	def pop(self):
		temp=self.store[0]
		self.store=self.store[1:]
		return temp
	def printQ(self):
		print self.store
		return 0
	def empty(self):
		if self.store:
			return True
		else:
			return False

class treenode:
	def __init__(self, eval_score, move_list, board):
		self.eval = eval_score
		self.Successor = []
		self.board = board
		#Move needed to get to this state: [init_pos, final_pos pairs]
		self.move = move_list
		self.LegalMoves = []

	def addMove(self, init_fin_pos_pair):
		self.move = self.move + init_fin_pos_pair
		return True

	def getLegalMoves(self,player):
		out = []
		my_pos = GetPlayerPositions(self.board,player)
		for i in my_pos:
			i_moves = GetPieceLegalMoves(self.board,i)
			for j in i_moves:
				out = out + [[i,j]]
		self.LegalMoves = out
		return out

	def AddSuccessor(self,treenode):
		self.Successor = self.Successor + [treenode]
		return True
	def Print_DepthFirst(self, depth):
		#depth starts with 0: use print function by always passing in a 0 to it
		print depth * '    ' + str(self.eval)
		for i in range (0,len(self.Successor)):
			self.Successor[i].Print_DepthFirst(depth+1)
		return True
	def Get_LevelOrder(self):
		out = []
		Q = queue()
		Q.push(self)
		while len(Q.store)!=0:
			node = Q.pop()
			out.append(node.eval)
			for i in node.Successor:
				Q.push(i)
		return out


# x=treenode(30)
# y=treenode(50)
# y1=treenode(14)
# z=treenode(60)
# y.AddSuccessor(y1)
# x.AddSuccessor(y)
# x.AddSuccessor(z)
# print x.Successor
# x.Print_DepthFirst(0)
# print x.Get_LevelOrder()
