class Solution:
    def isValid(self, s: str) -> bool:
        si={'}':'{',']':'[',')':'('}
        n=[]
        for i in s:
            if i not in si:
                n.append(i)
            else:
                if not n:
                    return False
                else:
                    p=n.pop()
                    if p!=si[i]:
                        return False
        return not n

        