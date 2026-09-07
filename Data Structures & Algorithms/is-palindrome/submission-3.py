class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = s.lower()
        cleaned_text = "".join(char for char in s_low if char.isalpha() or char.isdigit())
        inv = cleaned_text[::-1]
        return inv == cleaned_text

