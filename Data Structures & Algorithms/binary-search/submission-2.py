class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<target:
                l+=1
            elif nums[mid]==target:
                return mid
            else:
                r-=1
        return -1
                
        