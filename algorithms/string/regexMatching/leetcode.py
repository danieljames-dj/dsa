class Solution:
    
    def matches(self, s, p, si, pi):
        if pi == len(p):
            return si == len(s)
        else:
            if pi+1 < len(p) and p[pi+1] == '*':
                return (self.matches(s, p, si, pi+2) or
                        (si < len(s) and (s[si] == p[pi] or p[pi] == '.') and
                         self.matches(s, p, si+1, pi)))
            else:
                return (si < len(s) and (s[si] == p[pi] or p[pi] == '.')
                       and self.matches(s, p, si+1, pi+1))
    
    def isMatch(self, s: str, p: str) -> bool:
        return self.matches(s, p, 0, 0)