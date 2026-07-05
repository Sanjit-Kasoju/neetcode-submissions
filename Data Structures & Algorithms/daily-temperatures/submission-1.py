class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)

        s=[0]*n

        m=[]

        for i in range(n):
            while m and temperatures[i]>temperatures[m[-1]]:
                idx=m.pop()
                s[idx]=i-idx

            m.append(i)
        return s