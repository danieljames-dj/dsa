class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[None for i in range(n)] for j in range(n)]
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curDir = 0
        row = 0
        col = 0
        for x in range(1,n*n+1):
            mat[row][col] = x
            x += 1
            nextRow = row + dir[curDir][0]
            nextCol = col + dir[curDir][1]
            if nextRow >= n or nextRow < 0 or nextCol >= n or nextCol < 0 or mat[nextRow][nextCol]:
                curDir = (curDir + 1) % 4
            row += dir[curDir][0]
            col += dir[curDir][1]
        return mat