# Introduction
This is a chess AI program written in Python. I worked on this project from Jan. 2018 to Apr. 2018 to complement my CSC190: Data Structures and Algorithms course studies. Concepts such as tree, pruning, minimax are explored. 

# Instructions
To play my chess AI in Player v. Computer mode:
  1. Download all files to the same folder. 
  2. Run chessPlayer_PlayerVComp.py (only supports python 2).
  3. Choose a side (see instructions displayed). 
  4. Select a piece to move by entering its location on the board ("0" for A1, "1" for B2, ... "8" for A2 ..., "63" for H8). 
  5. Enter its desitnation square (same rule as Step 4). 
  6. Wait for the Computer to make a move!

# Rules
To simplify the game a little, some rules are different from actual chess. 
  1. No castling. 
  2. Pawns in starting positions are not allowed to double-step (e.g. can only do e3, not e4 as starting move). 
  3. No promotion (i.e. pawns marched to the other end of the board are still pawns).
  4. No "en passant" (a special pawn capture resulting from a double-step pawn move).
  
# Limitations
  1. Entering invalid pieces or squares can freeze the program!
  2. Player cannot arrange a starting board position. 
  3. Slow computation time (esp. in open positions). 

