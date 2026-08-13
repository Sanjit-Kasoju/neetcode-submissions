class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        longest=0


        for i in nums:
            if i-1 not in n:
                next_n=i+1
                length=1
                while next_n in n:
                    length+=1
                    next_n+=1
                
                longest=max(length,longest)
        return longest