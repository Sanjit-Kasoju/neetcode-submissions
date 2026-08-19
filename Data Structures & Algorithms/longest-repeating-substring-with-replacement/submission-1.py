class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        l=0
        maxf=0
        res=0

        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1
            maxf=max(c[s[r]],maxf)

            while (r-l+1)-maxf>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)

        return res


        