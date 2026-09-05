class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = {}
        for s in strs:
            sign = "".join(sorted(s))
            if sign in hashm:
                hashm[sign].append(s)
            else:
                hashm[sign] = [s]
                
        return list(hashm.values())

            

        

