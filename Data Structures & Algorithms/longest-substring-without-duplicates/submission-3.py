class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlen = 0
        sig = set()
        
        for r in range(len(s)):
            while s[r] in sig:
                sig.remove(s[l])
                l += 1
            sig.add(s[r])
            if r - l + 1 > maxlen:
                maxlen = r - l + 1
                
        return maxlen
            
            

            # print("maxlen: ", maxlen,"currlen: ",currlen)
            # print("l: ",l, "r: ",r)
        
        return maxlen

