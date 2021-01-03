class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = [-1 for _ in range(256)]
        tMap = [-1 for _ in range(256)]
        for i in range(len(s)):
            sCode = ord(s[i])
            tCode = ord(t[i])
            if sMap[sCode] != tMap[tCode]:
                return False
            sMap[sCode] = tMap[tCode] = i
        return True