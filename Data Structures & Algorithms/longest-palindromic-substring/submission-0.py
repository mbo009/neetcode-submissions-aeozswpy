class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest = ""

        def check_all_starting_at(i):
            if i == len(s):
                return
            
            for idx in range(i, len(s)):
                sub = s[i : idx + 1]
                if sub == sub[::-1]:
                    if len(sub) > len(self.longest):
                        self.longest = sub
            
            check_all_starting_at(i + 1)
    
        check_all_starting_at(0)
        return self.longest