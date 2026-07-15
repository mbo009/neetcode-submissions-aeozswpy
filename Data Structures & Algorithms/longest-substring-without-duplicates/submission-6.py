class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = dict()
        start = 0
        length = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in substring:
                if substring[char] >= start:
                    start = substring[char] + 1
            substring[char] = i           
            max_length = max(max_length, i - start + 1)

        return max_length


