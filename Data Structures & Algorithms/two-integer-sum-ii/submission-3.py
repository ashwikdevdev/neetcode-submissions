class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) -1
        # if numbers[0] + numbers[n]<target:
        #     print("no valid pair possible")
        #     return []
        # else:
        i =0
        j =n
        while i < j:
            # print(i,j)
            if numbers[i]+numbers[j]>target:
                j -= 1
            elif numbers[i]+numbers[j]<target:
                i += 1
            elif numbers[i]+numbers[j] == target:
                return [i+1,j+1]
        return []

                
