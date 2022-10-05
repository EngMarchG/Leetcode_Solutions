# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = []
        def recur(tree, total, target):
            if not tree:
                return
            
            total += tree.val
            if total == target and tree.left is None and tree.right is None:
                arr.append(total)
                return
            
            ans1=recur(tree.left, total, target)
            ans2=recur(tree.right, total, target)
            
        
        recur(root, 0, targetSum)
        if arr:
            return True
        return False