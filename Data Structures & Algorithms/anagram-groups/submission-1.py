class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            signature = self.DNA(word)
            if signature in seen:
                seen[signature].append(word)
            else:
                seen[signature] = [word]
        return list(seen.values())

    def DNA(self, str1: str):
        hash = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            hash.append(str1.count(char))
        return tuple(hash)
