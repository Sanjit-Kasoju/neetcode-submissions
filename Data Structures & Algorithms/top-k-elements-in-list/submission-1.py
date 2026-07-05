from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        counter=Counter(nums)

        m=[0]*(n+1)

        for num,freq in counter.items():
            if m[freq]==0:
                m[freq]=[num]
            else:
                m[freq].append(num)
        
        ret=[]
        for i in range(n,-1,-1):
            if m[i]!=0:
                ret.extend(m[i])
            if len(ret)==k:
                break;
        return ret