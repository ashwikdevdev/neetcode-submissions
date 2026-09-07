class Solution:
    def trap(self, height: list[int]) -> int:
        # if not height:  # Edge case check
        #     return 0
            
        water_net = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])

        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1): 
            max_right[i] = max(height[i], max_right[i+1])  

       
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            if water_level > height[i]:
                water_net += water_level - height[i]

        return water_net
