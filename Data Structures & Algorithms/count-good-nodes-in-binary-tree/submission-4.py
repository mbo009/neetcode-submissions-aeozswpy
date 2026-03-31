# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_count = 0

        def dfs(root, max_value):
            if root is None:
                return
            if root.val >= max_value:
                self.good_count += 1

            new_max = max(max_value, root.val)
            dfs(root.left, max(max_value, new_max))
            dfs(root.right, max(max_value, new_max))

        dfs(root, float('-inf'))
        return self.good_count    