class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_map: dict[str, int] = {}
        s2_map: dict[str, int] = {}
        
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
            
        if s1_map == s2_map:
            return True
            
        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            s2_map[new_char] = s2_map.get(new_char, 0) + 1
            
            old_char = s2[i - len(s1)]
            if s2_map[old_char] == 1:
                del s2_map[old_char]
            else:
                s2_map[old_char] -= 1
                
            if s1_map == s2_map:
                return True
                
        return False
