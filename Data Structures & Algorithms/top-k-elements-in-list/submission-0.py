class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        sorted_keys = sorted(seen.keys(), key=seen.get, reverse=True)
        
        return sorted_keys[:k]

            

        