# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        arr = [0]
        def recur(tree, counter):
            if not tree:
                arr[0] = max(arr[0], counter)
                return
            
            recur(tree.left, counter+1)
            recur(tree.right, counter+1)

            
        recur(root, 0)
        
        return arr[0]

"""Better Sol
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],counter=0) -> int:
        if root:
            counter += 1

        else:
            return counter
        return max(self.maxDepth(root.right,counter),self.maxDepth(root.left,counter))
"""