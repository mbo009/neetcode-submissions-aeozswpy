from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, count1 = 0, 0
        cand2, count2 = 1, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                cand1 = num
            elif count2 == 0:
                count2 = 1
                cand2 = num
            else:
                count1 -= 1
                count2 -= 1
        
        final_count1 = nums.count(cand1)
        final_count2 = nums.count(cand2)
        res = []
        if final_count1 > len(nums) // 3:
            res.append(cand1)
        if final_count2 > len(nums) // 3:
            res.append(cand2)
        return res
