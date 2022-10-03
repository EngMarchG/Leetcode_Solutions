# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = {}
        
        # Navigate the tree using recursion
        # Mark each level with a counter that increases
        # through every call and use a hash map with an array to return the answer
        def recur(tree, counter):
            if not tree:
                return
            
            if hmap.get(counter, 0):
                hmap[counter].append(tree.val)
            else:
                hmap[counter] = [tree.val]
            
            recur(tree.left, counter + 1)
            recur(tree.right, counter + 1)
        
        recur(root, 1)
        return hmap.values()