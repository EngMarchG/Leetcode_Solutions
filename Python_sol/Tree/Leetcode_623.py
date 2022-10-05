# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
        
        def recur(tree, val, depth, counter):
            if not tree or counter == depth:
                return
            
            if counter == depth - 1:
                temp = tree.left
                tree.left = TreeNode(val)
                tree.left.left = temp
                
                temp = tree.right
                tree.right = TreeNode(val)
                tree.right.right = temp
                
            
            recur(tree.left, val, depth, counter + 1)
            recur(tree.right, val, depth, counter + 1)
        
        recur(root, val, depth, 1)
        return root