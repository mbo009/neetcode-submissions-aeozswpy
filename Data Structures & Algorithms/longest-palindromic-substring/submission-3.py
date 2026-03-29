class Solution:
    def expand_palindrome(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i + 1 : j]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd_str = self.expand_palindrome(i, i, s)
            even_str = self.expand_palindrome(i, i + 1, s)
        
            if len(odd_str) > len(res):
                res = odd_str
            if len(even_str) > len(res):
                res = even_str
                
        return res  