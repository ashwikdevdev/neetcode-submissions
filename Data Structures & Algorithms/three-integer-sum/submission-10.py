class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hasmap={}
        # ansset = set()
        # n = len(nums)
        # matrix = [[0 for _ in range(n)] for _ in range(n)]
        # for r in range(n):
        #     for c in range(n):
        #         matrix[r][c] = nums[r] + nums [c]
        # for i in range(n):
        #     for r in range(n):
        #         for c in range(n):
        #             if i!=c and c!=r and r!=i:
        #                 if nums[i]+matrix[r][c] == 0:
        #                     ansset.add(tuple(sorted([nums[r],nums[c],nums[i]])))
        #                 continue
        #                 continue
        # return list(ansset) 


        # sorted: -4 -1 -1 0 1 2
        # sorted set(-4 -1 0 1 2)
        # i = 0 -4
        # j = 5 2
        # sum = -2
        # 
        
     
        lsout = set()
        nums = sorted(nums)
        
        # We only need to loop up to len(nums) - 2 because we need at least 3 elements
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element to speed it up
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Start the left pointer strictly AFTER i. 
            # This prevents using the same element twice and simplifies the logic.
            l, r = i + 1, len(nums) - 1
            target_diff = 0 - nums[i]

            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum < target_diff:
                    l += 1
                elif current_sum > target_diff:
                    r -= 1
                else:
                    # Match found! Since nums is sorted, [nums[i], nums[l], nums[r]] is already sorted
                    lsout.add((nums[i], nums[l], nums[r]))
                    
                    # Move both pointers to look for MORE pairs for this same nums[i]
                    l += 1
                    r -= 1
                    
        return list(lsout)


            