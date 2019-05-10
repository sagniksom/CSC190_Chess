def GetPlayerPositions(board,player):
	positions = []
	if not (player==10 or player==20): return False
	if type(board)!=list: return False
	if len(board)!=64: return False
	for i in range (0,64):
		if player==10:
			if board[i] in range (10,20):
				positions.append(i)
		elif player==20:
			if board[i] in range (20,30):
				positions.append(i)
	return positions

def cnt_Piece(piece,board):
	count = 0
	for i in board:
		if i==piece:
			count+=1
	return count

def find_Piece(piece,board):
	pos = []
	for i in range(0,64):
		if board[i]==piece:
			pos.append(i)
	return pos

def Material_Score(board,player):
	score = 0.0
	enemy = player%20+10
	#Pawn Score Difference
	score = score + 100*(cnt_Piece(player,board)-cnt_Piece(enemy,board))
	#Knight Score Difference
	score = score + 320*(cnt_Piece(player+1,board)-cnt_Piece(enemy+1,board))
	#Bishop Score Difference
	score = score + 330*(cnt_Piece(player+2,board)-cnt_Piece(enemy+2,board))
	#Rook Score Difference
	score = score + 500*(cnt_Piece(player+3,board)-cnt_Piece(enemy+3,board))
	#Queen Score Difference
	score =	score + 900*(cnt_Piece(player+4,board)-cnt_Piece(enemy+4,board))
	#King Score Difference
	score = score + 20000*(cnt_Piece(player+5,board)-cnt_Piece(enemy+5,board))
	return score

def Pos_Score(board,player):
	score = 0.0
	pawn = [0,0,0,0,0,0,0,0,\
			5,10,10,-25,-25,10,10,5,\
			5,-5,-10,0,0,-10,-5,5,\
			0,0,0,20,20,0,0,0,\
			5,5,10,25,25,10,5,5,\
			5,-5,-10,0,0,-10,-5,5,\
			5,-5,-10,0,0,-10,-5,5,\
			0,0,0,0,0,0,0,0]
	if (player==10):
		pawn_pos = find_Piece(10,board)
		for i in pawn_pos:
			score = score + pawn[i]
	if (player==20):
		pawn_pos = find_Piece(20,board)
		for i in pawn_pos:
			score = score + pawn[63-i]
	knight = [-50,-40,-30,-30,-30,-30,-40,-50,\
			-40,-20,  0,  5,  5,  0,-20,-40,\
			-30,  5, 10, 15, 15, 10,  5,-30,\
			-30,  0, 15, 20, 20, 15,  0,-30,\
			-30,  5, 15, 20, 20, 15,  5,-30,\
			-30,  0, 10, 15, 15, 10,  0,-30,\
			-40,-20,  0,  0,  0,  0,-20,-40,\
			-50,-40,-30,-30,-30,-30,-40,-50]
	if (player==10):
		n_pos = find_Piece(11,board)
		for i in n_pos:
			score = score + knight[i]
	if (player==20):
		n_pos = find_Piece(21,board)
		for i in n_pos:
			score = score + knight[63-i]
	bishop = [-20,-10,-10,-10,-10,-10,-10,-20,\
			-10,  5,  0,  0,  0,  0,  5,-10,\
			-10, 10, 10, 10, 10, 10, 10,-10,\
			-10,  0, 10, 10, 10, 10,  0,-10,\
			-10,  5,  5, 10, 10,  5,  5,-10,\
			-10,  0,  5, 10, 10,  5,  0,-10,\
			-10,  0,  0,  0,  0,  0,  0,-10,\
			-20,-10,-10,-10,-10,-10,-10,-20]
	if (player==10):
		b_pos = find_Piece(12,board)
		for i in b_pos:
			score = score + bishop[i]
	if (player==20):
		b_pos = find_Piece(22,board)
		for i in b_pos:
			score = score + bishop[63-i]
	rook = [  0,  0,  0,  5,  5,  0,  0,  0,\
			 -5,  0,  0,  0,  0,  0,  0, -5,\
			 -5,  0,  0,  0,  0,  0,  0, -5,\
			 -5,  0,  0,  0,  0,  0,  0, -5,\
			 -5,  0,  0,  0,  0,  0,  0, -5,\
			 -5,  0,  0,  0,  0,  0,  0, -5,\
			  5, 10, 10, 10, 10, 10, 10,  5,\
			  0,  0,  0,  0,  0,  0,  0,  0]
	if (player==10):
		r_pos = find_Piece(13,board)
		for i in r_pos:
			score = score + rook[i]
	if (player==20):
		r_pos = find_Piece(23,board)
		for i in r_pos:
			score = score + rook[63-i]	
	queen = [-20,-10,-10, -5, -5,-10,-10,-20,\
			-10,  0,  5,  0,  0,  0,  0,-10,\
			-10,  5,  5,  5,  5,  5,  0,-10,\
			 0,  0,  5,  5,  5,  5,  0, -5,\
			-5,  0,  5,  5,  5,  5,  0, -5,\
			-10,  0,  5,  5,  5,  5,  0,-10,\
			-10,  0,  0,  0,  0,  0,  0,-10,\
			-20,-10,-10, -5, -5,-10,-10,-20]
	if (player==10):
		q_pos = find_Piece(14,board)
		for i in q_pos:
			score = score + queen[i]
	if (player==20):
		q_pos = find_Piece(24,board)
		for i in q_pos:
			score = score + queen[63-i]
	player_pos = GetPlayerPositions(board,player)
	enemy_pos = GetPlayerPositions(board,player%20+10)
	if (len(player_pos)<=5 and len(enemy_pos)<=5):
		king = [-50,-30,-30,-30,-30,-30,-30,-50,\
				-30,-30,  0,  0,  0,  0,-30,-30,\
				-30,-10, 20, 30, 30, 20,-10,-30,\
				-30,-10, 30, 40, 40, 30,-10,-30,\
				-30,-10, 30, 40, 40, 30,-10,-30,\
				-30,-10, 20, 30, 30, 20,-10,-30,\
				-30,-20,-10,  0,  0,-10,-20,-30,\
				-50,-40,-30,-20,-20,-30,-40,-50]
	else:
		king = [ 20, 30, 10,  0,  0, 10, 30, 20,\
				 20, 20,  0,  0,  0,  0, 20, 20,\
				 -10,-20,-20,-20,-20,-20,-20,-10,\
				 -20,-30,-30,-40,-40,-30,-30,-20,\
				 -30,-40,-40,-50,-50,-40,-40,-30,\
				 -30,-40,-40,-50,-50,-40,-40,-30,\
				 -30,-40,-40,-50,-50,-40,-40,-30,\
				 -30,-40,-40,-50,-50,-40,-40,-30]
	if (player==10):
		k_pos = find_Piece(15,board)
		for i in k_pos:
			score = score + king[i]
	if (player==20):
		k_pos = find_Piece(25,board)
		for i in k_pos:
			score = score + king[63-i]
	return score

def getScore(board,player):
	return Material_Score(board,player) + Pos_Score(board,player)
