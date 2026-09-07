class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalpha() or char.isdigit())
        inv = cleaned_text[::-1]
        return inv.lower() == cleaned_text.lower()

