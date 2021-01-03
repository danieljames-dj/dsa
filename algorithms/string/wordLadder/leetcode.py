from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lookup = defaultdict(lambda: [])
        n = len(beginWord)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(n):
                lookup[word[:i] + '*' + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = set()
        while (queue):
            curWord, pathLength = queue.pop(0)
            for i in range(n):
                for word in lookup[curWord[:i] + '*' + curWord[i+1:]]:
                    if word == endWord:
                        return pathLength + 1
                    elif word not in visited:
                        visited.add(word)
                        queue.append((word, pathLength+1))
        return 0