class Solution:
    
    def lineArrayToString(self, lineArray, maxWidth, lineLength):
        n = len(lineArray) - 1
        if n == 0:
            return lineArray[0] + ' ' * (maxWidth - lineLength)
        uneq = (maxWidth - lineLength) % n
        eq = (maxWidth - lineLength) // n
        for i in range(uneq):
            lineArray[i] += (' ' * (eq + 1))
        for i in range(uneq, n):
            lineArray[i] += (' ' * eq)
        result = ''
        for i in range(n):
            result += lineArray[i] + ' '
        return result + lineArray[-1]
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        resultsArray = []
        lineArray = [words[0]]
        lineLength = len(words[0])
        for i in range(1, len(words)):
            if lineLength + len(words[i]) + 1 <= maxWidth:
                lineArray.append(words[i])
                lineLength += (len(words[i]) + 1)
            else:
                resultsArray.append(self.lineArrayToString(lineArray, maxWidth, lineLength))
                lineArray = [words[i]]
                lineLength = len(words[i])
        lastLine = ''
        for word in lineArray:
            lastLine += word + ' '
        lastLine = lastLine[:-1]
        lastLine += ' ' * (maxWidth - lineLength)
        resultsArray.append(lastLine)
        return resultsArray