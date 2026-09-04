class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # # Convert t to a list so we can remove characters from it
        # t_list = list(t)
        
        # for i in range(len(s)):
        #     char_to_find = s[i]
            
        #     # Check if the character exists in our t_list
        #     if char_to_find in t_list:
        #         # Remove it so another character cannot reuse it
        #         t_list.remove(char_to_find)
        #     else:
        #         # If a character in s doesn't exist in t_list, it's not an anagram
        #         return False
                
        # # If we successfully matched and removed every single character
        # return True


        alphabet = "abcdefghijklmnopqrstuvwxyz" 
        for char in alphabet:
            if s.count(char) != t.count(char):
                return False
        return True 
