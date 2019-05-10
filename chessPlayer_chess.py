def printBoard(board):
	for i in range (7,-1,-1):
		index = ['(56)','(48)','(40)','(32)',\
				'(24)','(16)','(08)','(00)']
		row = index[7-i]+ ' ' + str(i+1) + ' | '
		for j in range (0,8):
			position = 8*i + j
			row = row + ' ' + key_to_str(board[position]) + ' '
		print row
	print '--------------------------------'
	print '       |  A  B  C  D  E  F  G  H'
	print '       |  0  1  2  3  4  5  6  7'
	return True


def key_to_str(piece_number):
	piece = [0,10,11,12,13,14,15,20,21,22,23,24,25]
	string = ['.','P','N','B','R','Q','K','p','n','b','r','q','k']
	for i in range (0,len(piece)):
		if piece_number==piece[i]:
			return string[i]
	return '_'

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

def Position_to_RowCol (position):
	row = position/8
	column = position - 8*row
	return [row,column]

def GetPieceLegalMoves(board,position):
	LegalMoves=[]
	if type(board)!=list: return False
	if len(board)!=64: return False
	if position not in range (0,64): return False
	if board[position]==0: return []
	#White Pawn Moves
	if board[position]==10:
		if position+8<64:
			if board[position+8]==0:
				LegalMoves.append(position+8)
		if position+7<64:
			if board[position+7] in range (20,30):
				LegalMoves.append(position+7)
		if position+9<64:
			if board[position+9] in range (20,30):
				LegalMoves.append(position+9)
	#Black Pawn Moves
	if board[position]==20:
		if position-8>=0:
			if board[position-8]==0:
				LegalMoves.append(position-8)
		if position-7>=0:
			if board[position-7] in range (10,20):
				LegalMoves.append(position-7)
		if position-9>=0:
			if board[position-9] in range (10,20):
				LegalMoves.append(position-9)
	#White Rook Moves
	if board[position]==13:
		#Going along column, towards black
		for i in range (1,9,1):
			if position+8*i>=64:
				break
			if board[position+8*i]==0:
				LegalMoves.append(position+8*i)
			if board[position+8*i] in range (20,30):
				LegalMoves.append(position+8*i)
				break
			if board[position+8*i] in range (10,20):
				break
		#Going along column, towards white
		for i in range (-1,-9,-1):
			if position+8*i<0:
				break
			if board[position+8*i]==0:
				LegalMoves.append(position+8*i)
			if board[position+8*i] in range (20,30):
				LegalMoves.append(position+8*i)
				break
			if board[position+8*i] in range (10,20):
				break
		#Going along row: obtain row information
		row = position/8
		row_min_pos = 8 * row
		row_max_pos = row_min_pos + 7
		#Going right along row (from white view)
		analyze_position = position + 1
		while analyze_position <= row_max_pos:
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
				analyze_position = analyze_position + 1
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
		#Going left along row (from white view)
		analyze_position = position - 1
		while analyze_position >= row_min_pos:
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
				analyze_position = analyze_position - 1
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
	#Black Rook Moves
	if board[position]==23:
		#Going up column, towards black
		for i in range (1,9,1):
			if position+8*i>=64:
				break
			if board[position+8*i]==0:
				LegalMoves.append(position+8*i)
			if board[position+8*i] in range (10,20):
				LegalMoves.append(position+8*i)
				break
			if board[position+8*i] in range (20,30):
				break
		#Going down column, towards white
		for i in range (-1,-9,-1):
			if position+8*i<0:
				break
			if board[position+8*i]==0:
				LegalMoves.append(position+8*i)
			if board[position+8*i] in range (10,20):
				LegalMoves.append(position+8*i)
				break
			if board[position+8*i] in range (20,30):
				break
		#Going along row: obtain row information
		row = position/8
		row_min_pos = 8 * row
		row_max_pos = row_min_pos + 7
		#Going right along row (from white view)
		analyze_position = position + 1
		while analyze_position < row_max_pos:
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
				analyze_position = analyze_position + 1
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
		#Going left along row (from white view)
		analyze_position = position - 1
		while analyze_position >= row_min_pos:
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
				analyze_position = analyze_position - 1
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
	#White Bishop Moves
	if board[position] == 12:
		#Obtain current column number and row number
		row = position / 8
		column = position - 8 * row
		#Movement allowance in four directions from white view
		right_allow = 7 - column
		left_allow = column
		forward_allow = 7 - row
		backward_allow = row
		analyze_position = position
		# -> ^ Movement
		for i in range (1,min(right_allow,forward_allow)+1):
			analyze_position = analyze_position + 9
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
		analyze_position = position
		# <- ^ Movement
		for i in range(1,min(left_allow,forward_allow)+1):
			analyze_position = analyze_position + 7
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
		analyze_position = position
		# -> v Movement
		for i in range(1,min(right_allow,backward_allow)+1):
			analyze_position = analyze_position - 7
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
		analyze_position = position
		# <- v Movement
		for i in range(1,min(left_allow,backward_allow)+1):
			analyze_position = analyze_position - 9
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (20,30):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (10,20):
				break
	#Black Bishop Moves
	if board[position] == 22:
		#Obtain current column number and row number
		row = position / 8
		column = position - 8 * row
		#Movement allowance in four directions from white view
		right_allow = 7 - column
		left_allow = column
		forward_allow = 7 - row
		backward_allow = row
		analyze_position = position	
		# -> ^ Movement
		for i in range (1,min(right_allow,forward_allow)+1):
			analyze_position = analyze_position + 9
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
		analyze_position = position
		# <- ^ Movement
		for i in range(1,min(left_allow,forward_allow)+1):
			analyze_position = analyze_position + 7
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
		analyze_position = position
		# -> v Movement
		for i in range(1,min(right_allow,backward_allow)+1):
			analyze_position = analyze_position - 7
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
		analyze_position = position
		# <- v Movement
		for i in range(1,min(left_allow,backward_allow)+1):
			analyze_position = analyze_position - 9
			if board[analyze_position]==0:
				LegalMoves.append(analyze_position)
			if board[analyze_position] in range (10,20):
				LegalMoves.append(analyze_position)
				break
			if board[analyze_position] in range (20,30):
				break
	#White Queen Moves
	if board[position] == 14:
		alt_board = list(board)
		#Copy of board where queen replaced with bishop
		alt_board[position] = 12
		LegalMoves = LegalMoves + GetPieceLegalMoves(alt_board,position)
		#Copy of board where queen replaced with rook
		alt_board[position] = 13
		LegalMoves = LegalMoves + GetPieceLegalMoves(alt_board,position)				
	#Black Queen Moves
	if board[position] == 24:
		alt_board = list(board)
		#Copy of board where queen replaced with bishop
		alt_board[position] = 22
		LegalMoves = LegalMoves + GetPieceLegalMoves(alt_board,position)
		#Copy of board where queen replaced with rook
		alt_board[position] = 23
		LegalMoves = LegalMoves + GetPieceLegalMoves(alt_board,position)
	#White Knight Moves
	if board[position] == 11:
		row = position / 8
		column = position - 8 * row
		right_allow = 7 - column
		left_allow = column
		forward_allow = 7 - row
		backward_allow = row
		#First go forward 2 steps
		if forward_allow >= 2:
			#Check right turn allowed
			if right_allow >= 1:
				if board[position+17]==0 or board[position+17] in range (20,30):
					LegalMoves.append(position+17)
			#Check left turn allowed
			if left_allow >= 1:
				if board[position+15]==0 or board[position+15] in range (20,30):
					LegalMoves.append(position+15)
		#First go backwards 2 steps
		if backward_allow >= 2:
			if right_allow >= 1:
				if board[position-15]==0 or board[position-15] in range (20,30):
					LegalMoves.append(position-15)
			if left_allow >= 1:
				if board[position-17]==0 or board[position-17] in range (20,30):
					LegalMoves.append(position-17)
		#Firt go left 2 steps
		if left_allow >= 2:
			if forward_allow >= 1:
				if board[position+6]==0 or board[position+6] in range (20,30):
					LegalMoves.append(position+6)
			if backward_allow >= 1:
				if board[position-10]==0 or board[position-10] in range (20,30):
					LegalMoves.append(position-10)
		#First go right 2 steps
		if right_allow >= 2:
			if forward_allow >= 1:
				if board[position+10]==0 or board[position+10] in range (20,30):
					LegalMoves.append(position+10)
			if backward_allow >= 1:
				if board[position-6]==0 or board[position-6] in range (20,30):
					LegalMoves.append(position-6)
	#Black Knight Moves
	if board[position] == 21:
		row = position / 8
		column = position - 8 * row
		right_allow = 7 - column
		left_allow = column
		forward_allow = 7 - row
		backward_allow = row
		#First go forward 2 steps
		if forward_allow >= 2:
			#Check right turn allowed
			if right_allow >= 1:
				if board[position+17]==0 or board[position+17] in range (10,20):
					LegalMoves.append(position+17)
			#Check left turn allowed
			if left_allow >= 1:
				if board[position+15]==0 or board[position+15] in range (10,20):
					LegalMoves.append(position+15)
		#First go backwards 2 steps
		if backward_allow >= 2:
			if right_allow >= 1:
				if board[position-15]==0 or board[position-15] in range (10,20):
					LegalMoves.append(position-15)
			if left_allow >= 1:
				if board[position-17]==0 or board[position-17] in range (10,20):
					LegalMoves.append(position-17)
		#Firt go left 2 steps
		if left_allow >= 2:
			if forward_allow >= 1:
				if board[position+6]==0 or board[position+6] in range (10,20):
					LegalMoves.append(position+6)
			if backward_allow >= 1:
				if board[position-10]==0 or board[position-10] in range (10,20):
					LegalMoves.append(position-10)
		#First go right 2 steps
		if right_allow >= 2:
			if forward_allow >= 1:
				if board[position+10]==0 or board[position+10] in range (10,20):
					LegalMoves.append(position+10)
			if backward_allow >= 1:
				if board[position-6]==0 or board[position-6] in range (10,20):
					LegalMoves.append(position-6)	
	#White King Moves
	if board[position]==15:
		row = position / 8
		column = position - 8*row
		allowed_row = [row-1,row,row+1]
		allowed_col = [column-1, column, column+1]
		alt_board = list(board)
		alt_board[position]=14
		queen_moves = GetPieceLegalMoves(alt_board,position)
		for i in queen_moves:
			rc = Position_to_RowCol(i)
			if rc[0] in allowed_row and rc[1] in allowed_col:
				LegalMoves.append(i)
	#Black King Moves	
	if board[position]==25:
		row = position / 8
		column = position - 8*row
		allowed_row = [row-1,row,row+1]
		allowed_col = [column-1, column, column+1]
		alt_board = list(board)
		alt_board[position]=24
		queen_moves = GetPieceLegalMoves(alt_board,position)
		for i in queen_moves:
			rc = Position_to_RowCol(i)
			if rc[0] in allowed_row and rc[1] in allowed_col:
				LegalMoves.append(i)				
	return LegalMoves

def IsPositionUnderThreat(board,position,player):
	enemy_positions = GetPlayerPositions(board,player%20+10)
	enemy_moves = []
	for i in enemy_positions:
		enemy_moves = enemy_moves + GetPieceLegalMoves(board,i)
	if position in enemy_moves:
		return True
	else:
		return False
