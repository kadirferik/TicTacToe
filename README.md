# Tic-Tac-Toe Game with Minimax Algorithm

This Python application allows a human player to compete against an AI opponent in the classic Tic-Tac-Toe game using the Minimax algorithm.

## Features
- Play against a computer opponent that makes optimal moves.
- The user selects their mark (`X` or `O`) at the beginning of the game.
- Implements the Minimax algorithm to determine the best possible move for the computer.
- Detects win, loss, and draw conditions.
- Playable via command-line interface.

## Requirements
- Python 3.x
- NumPy library (`pip install numpy`)

## How to Play
1. Run the script:
   ```sh
   python tic_tac_toe.py
   ```
2. Choose your mark (`X` or `O`). The computer will take the opposite mark.
3. Players take turns placing their marks on a 3x3 grid by entering row and column indices (e.g., `1,2`).
4. The game continues until a player wins or all cells are filled (resulting in a draw).

## Game Rules
- Aligning three marks horizontally, vertically, or diagonally wins the game.
- If all cells are filled and no player wins, the game ends in a draw.
- The computer uses the Minimax algorithm to make optimal moves.

## Minimax Algorithm
The Minimax algorithm evaluates all possible moves and selects the one that maximizes the AI's chances of winning while minimizing the opponent's chances. The evaluation function assigns:
- `+10` for AI wins
- `-10` for player wins
- `0` for a draw

The AI recursively explores all available moves and chooses the one with the best outcome.

## Code Overview
- `printBoard(board)`: Displays the Tic-Tac-Toe board.
- `isWinner(board, mark)`: Checks if a player has won.
- `isDraw(board)`: Determines if the game is a draw.
- `availableMoves(board)`: Returns a list of available moves.
- `minimax(board, depth, isMaximising)`: Implements the Minimax algorithm.
- `bestMove(board)`: Determines the best move for the computer.
- The main game loop takes user input and alternates turns with the AI.

## Example Gameplay
```
Please select a mark (x/o): x
---------
  |   |  
---------
  |   |  
---------
  |   |  
---------
Please enter your move (row,col): 0,0
---------
x |   |  
---------
  |   |  
---------
  |   |  
---------
Computer's move:
---------
x |   |  
---------
  | o |  
---------
  |   |  
---------
```

## License
This project is open-source and can be freely used and modified.

