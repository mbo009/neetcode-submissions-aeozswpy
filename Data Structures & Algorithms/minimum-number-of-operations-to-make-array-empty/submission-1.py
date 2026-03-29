from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        operations = 0

        for num, count in counter.items():
            curr_count = count
            while curr_count >= 5 or curr_count == 3:
                curr_count -= 3
                operations += 1
            while curr_count >= 2:
                curr_count -= 2
                operations += 1
            if curr_count != 0:
                return -1
        
        return operations 
            


# 10 - 3 = 7
# 10 - 3 = 4
# 10 - 3 = 1 X
# 10 - 2 = 2
# 10 - 2 = 0