class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned_text = "".join(char.lower() for char in s if char.isalpha() or char.isdigit())
        # inv = cleaned_text[::-1]
        # return inv == cleaned_text

        left , right = 0, len(s) - 1
        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -=1
        
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -= 1
        return True

