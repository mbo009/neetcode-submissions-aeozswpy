class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0

        for j in range(len(chars)):
            if chars[i] != chars[j]:
                curr_len = j - i
                chars[k] = chars[i]
                k += 1

                if curr_len > 1:
                    for num in str(curr_len):
                        chars[k] = num    
                        k += 1
            
                i = j

        curr_len = len(chars) - i
        chars[k] = chars[i]
        k += 1
        if curr_len > 1:
            for c in str(curr_len):
                chars[k] = c
                k += 1

        return k
