class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = ord(s[0])
        for char in s[1:]:
            curr = ord(char)
            score += abs(curr - prev)
            prev = curr
        return score