class Solution:
    
    def getLevel(self, input):
        level = 0
        for i in range(len(input)):
            if input[i] == '\t':
                level += 1
            else:
                break
        return level
    
    def isFile(self, input):
        return '.' in input
        
    def lengthLongestPath(self, input: str) -> int:
        contents = input.split('\n')
        longestPath = 0
        curPath = []
        for line in contents:
            level = self.getLevel(line)
            length = len(line) - level
            if self.isFile(line):
                curLength = length
                for i in range(level):
                    curLength += curPath[i] + 1
                longestPath = max(longestPath, curLength)
            elif level < len(curPath):
                curPath[level] = length
            else:
                curPath.append(length)
        return longestPath