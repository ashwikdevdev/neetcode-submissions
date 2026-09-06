class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area=0
        while i < j:
            print(i,j)
            area = (j-i)*min(heights[i],heights[j])
            # print(area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            if max_area < area:
                max_area = area
            # print(i,j,max_area)
            # print("="*20)
        return max_area