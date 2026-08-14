class Solution:
    def isValid(self, s: str) -> bool:
        m={']':'[','}':'{',')':'('}
        n=[]

        for i in s:
            if i not in m:
                n.append(i)
            else:
                if not n:
                    return False
                
                p=n.pop()
                if p!=m[i]:
                    return False
        return not n
        