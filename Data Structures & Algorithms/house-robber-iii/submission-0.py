# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs_rob(root):
            if not root:
                return 0, 0

            l_rob, l_not_rob = dfs_rob(root.left)
            r_rob, r_not_rob = dfs_rob(root.right)

            robbed = root.val + l_not_rob + r_not_rob
            not_robbed = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)

            return robbed, not_robbed
        
        return max(dfs_rob(root))