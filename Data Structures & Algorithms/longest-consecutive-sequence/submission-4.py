class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        arraysort = sorted(nums)
        max_count = 1
        count = 1 
        
        # Start at index 1 to safely compare against i - 1
        for i in range(1, len(arraysort)):
            # Skip duplicates (e.g., [1, 2, 2, 3] -> the second '2' is ignored)
            if arraysort[i] == arraysort[i-1]:
                continue
                
            # If consecutive, increase the current streak
            if arraysort[i] - arraysort[i-1] == 1:
                count += 1
            else:
                # Streak broken! Save the max and reset current count
                max_count = max(max_count, count)
                count = 1
                
        # Final check to catch the longest streak if it went all the way to the end
        return max(max_count, count)
