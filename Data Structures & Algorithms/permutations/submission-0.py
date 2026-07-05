class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,sol=[],[]
        n=len(nums)

        def bt():
            if len(sol)==n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    bt()
                    sol.pop()
        bt()
        return ans

        