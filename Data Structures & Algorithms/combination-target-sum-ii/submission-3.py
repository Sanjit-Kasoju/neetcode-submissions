class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        res,sol=[],[]
        n=len(nums)
        nums.sort()

        def backtrack(i,sum):
            if sum==target:
                res.append(sol[:])
                return
            
            if sum>target or i==n:
                return

            

            sol.append(nums[i])
            backtrack(i+1,sum+nums[i])
            sol.pop()

            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,sum)


        backtrack(0,0)
        return res
        