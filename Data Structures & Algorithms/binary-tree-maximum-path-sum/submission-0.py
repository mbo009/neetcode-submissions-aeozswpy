# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_max_gain(root):
            if not root:
                return 0
            l_gain = max(get_max_gain(root.left), 0)
            r_gain = max(get_max_gain(root.right), 0)
            curr_sum = root.val + l_gain + r_gain
            self.max_sum = max(curr_sum, self.max_sum)

            return root.val + max(l_gain, r_gain)

        get_max_gain(root)
        return self.max_sum