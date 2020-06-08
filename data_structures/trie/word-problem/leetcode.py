class Trie:
    def __init__(self, val):
        self.val = val
        self.ch = {}

class Solution:
    
    def addToTrie(self, word, trie):
        node = trie
        for c in (word + '$'):
            if c not in node.ch:
                node.ch[c] = Trie(c)
            node = node.ch[c]
    
    def getStrings(self, s, i, dp, trie):
        if dp[i] == None:
            dp[i] = []
            if s[i] in trie.ch:
                node = trie.ch[s[i]]
                for j in range(i+1, len(s)+1):
                    if '$' in node.ch:
                        if j == len(s):
                            dp[i].append(s[i:j])
                        else:
                            for el in self.getStrings(s, j, dp, trie):
                                dp[i].append(s[i:j] + " " + el)
                    if j == len(s) or s[j] not in node.ch:
                        break
                    node = node.ch[s[j]]
        return dp[i]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie('^')
        for word in wordDict:
            self.addToTrie(word, trie)
        dp = [None] * len(s)
        return self.getStrings(s, 0, dp, trie)