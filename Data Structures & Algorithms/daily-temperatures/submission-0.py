class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        t=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            while s and j>s[-1][0]:
                n,m=s.pop()
                t[m]=(i-m)
            s.append([j,i])
        return t

        