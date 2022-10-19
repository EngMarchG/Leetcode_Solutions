# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(temp):
            if not temp:
                return
            temp.left, temp.right = temp.right, temp.left
            recur(temp.right)
            recur(temp.left)
        
        recur(root)
            
        return root

""" Same stuff just using the class directly instead of a function
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = Solution()
        if root:
            root.left, root.right = root.right, root.left
            tree.invertTree(root.left)
            tree.invertTree(root.right)
        return root
"""