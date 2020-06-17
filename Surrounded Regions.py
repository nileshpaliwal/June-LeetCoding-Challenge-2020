#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
#A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#Example:
#
#X X X X
#X O O X
#X X O X
#X O X X
#After running your function, the board should be:
#
#X X X X
#X X X X
#X X X X
#X O X X
#Explanation:
#
#Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution(object):
    def solve(self, board):
        def dfs(board, i , j):
            if i>len(board)-1 or i<0 or j>len(board[0]) or j<0:
                return
            if board[i][j]=='O':
                board[i][j]= '*'

            if i>0 and board[i-1][j]=='O':
                print(1)
                dfs(board,i-1,j)
            if i<len(board)-1 and board[i+1][j]=='O':
                print(2)
                dfs(board,i+1,j)
            if j>0 and board[i][j-1]=='O':
                print(3)
                dfs(board,i,j-1)
            if j<len(board[0])-1 and board[i][j+1]=='O':
                print(4)
                dfs(board,i,j+1)
            return 
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            if board[i][0]=='O':
                dfs(board,i,0)
            if board[i][cols-1]=='O':
                dfs(board,i,cols-1)

        for j in range(cols):
            if board[0][j]=='O':
                dfs(board,0,j)
            if board[rows-1][j]=='O':
                dfs(board,rows-1,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='*':
                    board[i][j]='O'



