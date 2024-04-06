# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(left_side, right_side):
            if not left_side and not right_side:
                return True
            if not left_side or not right_side:
                return False
            
            
            if left_side.val == right_side.val:
                edges = recur(left_side.left, right_side.right)
                inner = recur(left_side.right, right_side.left)
                return edges and inner

        return recur(root.left, root.right)