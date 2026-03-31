# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, current_count):
            if node is None:
                return None, current_count

            res, current_count = inorder(node.left, current_count)
            
            if res is not None:
                return res, current_count

            current_count += 1
            if current_count == k:
                return node.val, current_count

            return inorder(node.right, current_count)

        result, _ = inorder(root, 0)
        return result# Solution: we iterate to smallest element, his parent is next smallest, right child is next smallest after parent
#                4    k = 3
#               / \ 
#     k = 2    3   5  k = 4
#             /
#     k = 1  2    