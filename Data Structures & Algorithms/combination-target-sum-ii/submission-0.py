class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans,sol=[],[]
        n=len(candidates)
        candidates.sort()

        def bt(i,curr,sum):
            if sum==target:
                ans.append(sol[:])
                return 
            
            if sum>target or i==n:
                return

            sol.append(candidates[i])
            bt(i+1,curr,sum+candidates[i])
            sol.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            bt(i+1,curr,sum)
        bt(0,[],0)
        return ans
        