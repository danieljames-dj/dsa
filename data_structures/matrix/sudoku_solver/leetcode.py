class Solution:
    
    def __init__(self):
        self.size = 9
    
    def isRowCorrect(self, board, i, j):
        for k in range(self.size):
            if k != j and board[i][k] == board[i][j]:
                return False
        return True
    
    def isColCorrect(self, board, i, j):
        for k in range(self.size):
            if k != i and board[k][j] == board[i][j]:
                return False
        return True
    
    def isBoxCorrect(self, board, i, j):
        boxSize = 3
        rowRank = i // boxSize
        colRank = j // boxSize
        for ii in range(boxSize * rowRank, boxSize * (rowRank + 1)):
            for jj in range(boxSize * colRank, boxSize * (colRank + 1)):
                if ii != i and jj != j and board[ii][jj] == board[i][j]:
                    return False
        return True
    
    def solve(self, board, n):
        if n == self.size * self.size:
            return True
        i = n // self.size
        j = n % self.size
        if board[i][j] != '.':
            return self.solve(board, n+1)
        else:
            for k in range(1,self.size+1):
                board[i][j] = str(k)
                if (self.isRowCorrect(board, i, j) and self.isColCorrect(board, i, j)
                   and self.isBoxCorrect(board, i, j) and self.solve(board, n+1)):
                    return True
            board[i][j] = '.'
            return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board, 0)