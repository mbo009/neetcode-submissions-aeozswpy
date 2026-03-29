class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        needed = set()
        triplet_set = set()
        triplets = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                if -(sorted_nums[i] + sorted_nums[j]) in needed:
                    triplet = [sorted_nums[i], sorted_nums[j], -(sorted_nums[i] + sorted_nums[j])]

                    if str(triplet) not in triplet_set:
                        triplets.append(triplet)
                        triplet_set.add(str(triplet))
                    
            needed.add(sorted_nums[i])
        
        return triplets
# -1 0 1 2 -1 -4
# -1 0 -> -1
# -1 1 -> 0