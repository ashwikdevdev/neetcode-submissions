class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:  # Edge case check
            return 0
            
        water_net = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        # 1. Fill left max (No nested loops needed!)
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])

        # 2. Fill right max (Loop backwards correctly)
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):  # Starts at n-2, goes down to 0
            max_right[i] = max(height[i], max_right[i+1])  # Fixed typo: max_right instead of max_left

        # 3. Calculate total water
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            if water_level > height[i]:
                water_net += water_level - height[i]

        return water_net
