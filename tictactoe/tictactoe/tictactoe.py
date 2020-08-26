"""
Tic Tac Toe Player

Things to do
player && minimax
"""

import math
import copy
from itertools import cycle

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    CntX = 0
    CntO = 0

    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                CntX += 1
            elif (board[i][j] == O):
                CntO += 1

    if board == initial_state():
        return X
    elif CntX == CntO :
        return X
    else :
        return O

           
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    loc = set()

    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                loc.add((i,j))

    return loc


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # If action is not a valid action for the board, 
    # your program should raise an exception.
    # if action not in actions(board):
    #     raise Exception("Invalid Action")
    
    newboard = copy.deepcopy(board)
    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    
    for i in range(3):
        bingo = False
        if bingo :
            break
        if (board[i][0]==board[i][1]==board[i][2]):
            winner = board[i][0]
            bingo = True
        if (board[0][i]==board[1][i]==board[2][i]):
            winner = board[0][i]
            bingo = True
            
    if (board[0][0]==board[1][1]==board[2][2]) :
        winner = board[0][0]
        
    if (board[0][2]==board[1][1]==board[2][0]) :
        winner = board[0][2]

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    status = False
    
    # if winner exists
    if not winner(board) is None :
        status = True

    # if the board is full
    full = True
    for i in range(3):
        for j in range(3):
            if board[i][j] is None :
                full = False
    
    if full is True :
        status = True

    return status


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # X is maxmimizing the score
    if winner(board) == X :
        result = 1
    # O is minimizing the score
    elif winner(board) == O :
        result = -1
    else :
        result = 0
    
    return result



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    Max = float("-inf")
    Min = float("inf")

    if terminal(board):
        return None
    
    if player(board) == X:
        result = max_value(board, Max, Min)[1]
    else :
        result = min_value(board, Max, Min)[1]
    
    return result


"""
Recursive functions will be implemented 
until the board is terminal state
"""

def max_value(board, alpha, beta):
    """
    Returns the choice of which value is maximum at given board
    under the condition that the opponent is tryting to minimize the score
    """
    if terminal(board):
        return [utility(board), None]

    v = float("-inf")
    move = None
    for action in actions(board):
        test = min_value(result(board, action), alpha, beta)[0]
        alpha = max(alpha, test)
        if test > v :
            v = test
            move = action
        # β cut-off
        # 자신이 상대방보다 유리하여, 상대방이 그 경우를 선택하지 않을 확률이 높을 때 불필요한 연산을 잘라내는 것
        if alpha >= beta:
            break
    return [v, move]
        

def min_value(board, alpha, beta):
    """
    Returns the choice of which value is minimum at given board
    under the condition that the opponent is tryting to maximize the score
    """

    if terminal(board):
        return [utility(board), None]

    v = float("inf")
    move = None
    for action in actions(board):
        # recursion implemented until 
        # the outcome of given action is presented
        test = max_value(result(board, action), alpha, beta)[0]
        beta = min(beta, test)
        if test < v :
            v = test
            move = action
        # α cut-off
        # 자신이 상대방보다 불리하여, 자신이 그 경우를 선택하지 않을 때 불필요한 연산을 잘라내는 것
        if alpha >= beta:
            break
    return [v, move]