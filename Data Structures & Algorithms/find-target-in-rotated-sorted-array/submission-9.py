class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1

        while l<r:
            m=(l+r)//2
            
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        min_m=l

        if min_m==0:
            l,r=0,n-1
        elif target>=nums[0] and target<=nums[min_m-1]:
            l,r=0,min_m-1
        else:
            l,r=min_m,n-1
            
        while l<=r:
            m=(l+r)//2

            if nums[m]==target:
                return m
                
            if nums[m]<target:
                l=m+1
            else:
                r=m-1


        return -1
        