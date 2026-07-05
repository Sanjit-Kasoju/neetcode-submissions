class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        
        heapq.heapify(stones)
        while len(stones)>1:
            l=heapq.heappop(stones)
            sl=heapq.heappop(stones)

            if l!=sl:
                heapq.heappush(stones,l-sl)

        if len(stones)==1:
            return -heapq.heappop(stones) 
        else:
            return 0
            
           

