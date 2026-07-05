from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d=defaultdict(int)
        m=defaultdict(int)
        for i in range(len(s)):
            d[s[i]]+=1
            m[t[i]]+=1
        return d==m
        