class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=1,1
        n=len(nums)

        l1=[0]*n
        r1=[0]*n
        
        for i in range(n):
            j=-i-1

            l1[i]=l
            r1[j]=r

            l*=nums[i]
            r*=nums[j]
        
        return [l*r for l,r in zip(l1,r1)]
