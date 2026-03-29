import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(char.lower() for char in s if char.isalpha() or char.isdigit())
        
        i = 0
        j = len(filtered_s) - 1
        while i < j:
            print(filtered_s[i], filtered_s[j])
            if filtered_s[i] != filtered_s[j]:
                return False

            i += 1
            j -= 1

        return True