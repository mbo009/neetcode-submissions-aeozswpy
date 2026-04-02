class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        intersect = set_n1.intersection(set_n2)
        
        return [list(set_n1 - intersect), list(set_n2 - intersect)]
        