class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans,sol=[],[]
        n=len(nums)
        
        def bt(i,sum):
            if sum==target:
                ans.append(sol[:])
                return
                
            if sum>target or i==n:
                return 
            bt(i+1,sum)

            sol.append(nums[i])
            bt(i,sum+nums[i])
            sol.pop()
        bt(0,0)
        return ans
            

        