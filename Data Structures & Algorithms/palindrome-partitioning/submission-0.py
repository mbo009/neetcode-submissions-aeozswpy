class Solution:
    def is_palindrome(self, word):
        if not word:
            return False
        i = 0
        j = len(word) - 1

        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, curr_path):
            if i == len(s):
                res.append(curr_path[:])

            for idx in range(i, len(s)):
                sub = s[i : idx + 1]
                if self.is_palindrome(sub):
                    curr_path.append(sub)
                    backtrack(idx + 1, curr_path)
                    del curr_path[-1]
    
        backtrack(0, [])
        return res


# Solution
# We use backtracking similiar to making every possible substring
# - start from 0
# - iterate through characters in word 
# - lock 1 character in place and check if subword to the left and to the right is a palindrome