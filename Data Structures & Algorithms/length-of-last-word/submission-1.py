class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(" ").lstrip(" ").split(" ")[-1])