class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        return (one_count - 1) * "1" + (len(s) - one_count) * "0" + "1"
        