class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else:
                r,l=s.pop(),s.pop()

                if i=="+":
                    s.append(l+r)
                elif i=="-":
                    s.append(l-r)
                elif i=="*":
                    s.append(l*r)
                elif i=="/":
                    s.append(int(l/r))
        return s[0]
            
        