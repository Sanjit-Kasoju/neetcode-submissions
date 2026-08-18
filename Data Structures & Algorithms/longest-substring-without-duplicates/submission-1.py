class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=set()
        maxlen=0
        l=0

        for r in range(len(s)):
            while s[r] in n:
                n.remove(s[l])
                l+=1
            n.add(s[r])

            maxlen=max(maxlen,r-l+1)
        
        return maxlen
        