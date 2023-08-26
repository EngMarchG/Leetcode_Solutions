# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n) Space Complexity: O(1) or O(h) if considering recursion stack
        def recur(tree, path):
            if not tree:
                return 0
            if path and not tree.left and not tree.right:
                return tree.val
            
            left_sum = recur(tree.left, 1)
            right_sum = recur(tree.right, 0)
            return left_sum + right_sum

        return recur(root, 0)