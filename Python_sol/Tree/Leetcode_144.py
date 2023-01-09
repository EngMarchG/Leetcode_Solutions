# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def trave(root):
            if not root:
                return trave
            arr.append(root.val)
            trave(root.left)
            trave(root.right)
            return trave
        trave(root)
        return arr