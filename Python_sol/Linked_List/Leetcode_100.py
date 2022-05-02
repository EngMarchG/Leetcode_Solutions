# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Time Complexity: O(2^min(p,q)), Space Complexity: O(2*min(p,q))
        # Takes in both trees (can call self instead)
        def recur(tree1, tree2):
            # If both nodes reach none at the same time its equal
            if not tree1 and not tree2:
                return True
            # Checking if they are equal (and not none)
            if tree1 and tree2 and tree1.val==tree2.val:
                    return recur(tree1.left, tree2.left) and recur(tree1.right, tree2.right)
            # If one of the is not empty and the other is, they aren't equal   
            else:
                return 0

        return recur(p, q)
                