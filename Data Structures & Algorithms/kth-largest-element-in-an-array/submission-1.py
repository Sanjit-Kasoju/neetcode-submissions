class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        s=[0]
        for i in range(k):
            p=heapq.heappop(nums)
            s.append(p)
        
        return -s[-1]
