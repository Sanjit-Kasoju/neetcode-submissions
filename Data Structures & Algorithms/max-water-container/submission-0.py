class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r=0,len(heights)-1
        area=0
        while l<r:
            width=r-l
            h=min(heights[l],heights[r])          
            a=h*width
            area=max(area,a)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area

        