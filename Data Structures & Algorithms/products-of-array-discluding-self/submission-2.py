class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod: int = 1
        output = []
        zeroloc = set()  
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroloc.add(i)
                continue
            prod = prod * nums[i]
            
        if len(zeroloc) == 0:
            for i in range(len(nums)):
                output.append(prod // nums[i])
                
        elif len(zeroloc) == 1:
            output = [0] * len(nums)
            zero_index = zeroloc.pop()
            output[zero_index] = prod
            
        else:
            output = [0] * len(nums)
        
        return output
