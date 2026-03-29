# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_count(self, root):
        if not root:
            return 0
        return self.dfs_count(root.left) + self.dfs_count(root.right) + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while True:
            left_count = self.dfs_count(curr.left)

            if left_count == k - 1:
                return curr.val
            
            if left_count >= k:
                curr = curr.left
            else:
                k -= (left_count + 1)
                curr = curr.right
        
        return -1



# Solution: we iterate to smallest element, his parent is next smallest, right child is next smallest after parent
#                4    k = 3
#               / \ 
#     k = 2    3   5  k = 4
#             /
#     k = 1  2    