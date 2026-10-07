class Solution:
    def search(self, nums: List[int], target: int) -> int:
         top = len(nums)
         bottom = 0
         nums.sort()
         i = 0 
         if target not in nums:
                return -1
         while bottom < top and i<math.log2(len(nums))+1:
            print("top: ",top,"bottom: ",bottom)
            
            if nums[int((bottom+top)/2)] < target:
                bottom = int((bottom+top)/2)
                i+=1
            if nums[int((bottom+top)/2)] > target:
                top = int((bottom+top)/2) 
                i+=1
            if nums[int((bottom+top)/2)] == target:
                return int((bottom+top)/2)
         return -1
