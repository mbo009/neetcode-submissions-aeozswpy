class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = dict()
        for string in strings:
            base = string[0]
            diff = []
            for char in string:
                diff.append((ord(char) - ord(base)) % 26)
            
            diff_key = str(diff)
            if diff_key in groups:
                groups[diff_key].append(string)
            else:
                groups[diff_key] = [string]
        
        return list(groups.values())
            


# a->b = abs(97 - 98) = 1 but a->z abs(97 - 122) = 25
# 