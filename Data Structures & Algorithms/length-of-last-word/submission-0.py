class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        curr_len = 0
        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            curr_len += 1
            i -= 1
          
        return curr_len