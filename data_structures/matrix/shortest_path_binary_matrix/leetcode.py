class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dim = len(grid)
        start = [0, 0]
        target = [dim-1, dim-1]
        if grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
            return -1
        if start[0] == target[0] and start[1] == target[1]:
            return 1
        curDis = 1
        curIndices = [start]
        visited = [[False for i in range(dim)] for j in range(dim)]
        visited[start[0]][start[1]] = True
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while curDis < dim * 2:
            curLength = len(curIndices)
            if curLength == 0:
                break
            for _ in range(curLength):
                index = curIndices.pop(0)
                for neighbor in neighbors:
                    newIndex = [index[0] + neighbor[0], index[1] + neighbor[1]]
                    if (newIndex[0] >= 0 and newIndex[1] >= 0 and
                    newIndex[0] < dim and newIndex[1] < dim and
                    grid[newIndex[0]][newIndex[1]] == 0 and not visited[newIndex[0]][newIndex[1]]):
                        if newIndex[0] == target[0] and newIndex[1] == target[1]:
                            return curDis + 1
                        curIndices.append(newIndex)
                        visited[newIndex[0]][newIndex[1]] = True
            curDis += 1
        return -1