class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        m=[0]*(n+1)
        m[1],m[2]=1,2
        for i in range(3,n+1):
            m[i]=m[i-1]+m[i-2]
        

        return m[n]