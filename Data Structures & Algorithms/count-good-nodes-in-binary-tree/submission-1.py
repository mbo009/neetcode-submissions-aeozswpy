# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, curr_max):
        res = 0
        if not root:
            return 0
        if root.val >= curr_max:
            res += 1

        new_max = max(curr_max, root.val)
        left_count = self.dfs(root.left, new_max)
        right_count = self.dfs(root.right, new_max)

        return res + left_count + right_count

    def goodNodes(self, root: TreeNode) -> int:
        curr_max = float('-inf')
        res = self.dfs(root, curr_max)
        return res
