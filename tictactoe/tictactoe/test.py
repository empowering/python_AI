from tictactoe import *

board = [[X, O, O],
         [EMPTY, EMPTY, EMPTY],
         [X, O, X]]

# for action in actions(board):
#     print(action)

print(minimax(board))