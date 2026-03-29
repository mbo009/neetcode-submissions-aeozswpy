class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums) and nums[i] < 0:
            i += 1

        j = i
        i -= 1

        while i >= 0 or j < len(nums):
            if i >= 0 and j < len(nums):
                if abs(nums[i]) < nums[j]:
                    res.append(nums[i] ** 2)
                    i -= 1
                else:
                    res.append(nums[j] ** 2)
                    j += 1
            elif i >= 0:
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1

        return res 



# [-4, -1, 0, 3, 10] i = 2
# Now we iterate through numsbers from 0 to 10
# if there is a negative numsber we compare it's absolute value with next natural numsber
# if it's smaller then we append the negative squared and move the i to the left
# else we append the squared natural
# we do that until all numsbers were added
        


