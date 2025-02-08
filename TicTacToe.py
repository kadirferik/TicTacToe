"""
Created on Thu Feb  6 14:21:37 2025

@author: kadirferik
"""

import numpy as np

def printBoard(board):
    print("-" * 9)
    for i in board:
        print(" | ".join(i))
        print("-" * 9)

def isWinner(board, mark):
    for i in range(3):
        if all([cell == mark for cell in board[i, :]]):
            return True
        if all([board[j, i] == mark for j in range(3)]):
            return True
    if board[0, 0] == mark and board[1, 1] == mark and board[2, 2] == mark:
        return True
    if board[0, 2] == mark and board[1, 1] == mark and board[2, 0] == mark:
        return True
    return False

def isDraw(board):
    return np.all(board != " ")

def availableMoves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == " "]

def minimax(board, depth, isMaximising):
    if isWinner(board, computer):
        return 10 - depth
    if isWinner(board, gamer):
        return depth - 10
    if isDraw(board):
        return 0
    
    if isMaximising:
        best_score = -float("inf")
        for (i, j) in availableMoves(board):
            board[i, j] = computer
            score = minimax(board, depth + 1, False)
            board[i, j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for (i, j) in availableMoves(board):
            board[i, j] = gamer
            score = minimax(board, depth + 1, True)
            board[i, j] = " "
            best_score = min(best_score, score)
        return best_score

def bestMove(board):
    best_score = -float("inf")
    move = None
    for (i, j) in availableMoves(board):
        board[i, j] = computer
        score = minimax(board, 0, False)
        board[i, j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

if __name__ == "__main__":
    board = np.full((3, 3), " ")
    select_mark = input("Please Select a Mark (x/o): ")

    if select_mark.lower() == "x":
        computer = "o"
        gamer = "x"
    elif select_mark.lower() == "o":
        computer = "x"
        gamer = "o"
    else:
        print("Your choice is wrong! Please select correct marks!")
        exit()
    
    current_queue = "x"
    printBoard(board)
    
    while True:
        if current_queue == gamer:
            move_i, move_j = map(int, input("Please enter your move (row,col): ").strip().split(","))
            if board[move_i, move_j] == " ":    
                board[move_i, move_j] = gamer
                printBoard(board)
                if isWinner(board, gamer):
                    print("Congratulations! You win!")
                    break
                elif isDraw(board):
                    print("It's a draw!")
                    break
                current_queue = computer
        
        if current_queue == computer:
            move_i, move_j = bestMove(board)
            board[move_i, move_j] = computer
            print("Computer's move:")
            printBoard(board)
            if isWinner(board, computer):
                print("Computer wins! Better luck next time.")
                break
            elif isDraw(board):
                print("It's a draw!")
                break
            current_queue = gamer
