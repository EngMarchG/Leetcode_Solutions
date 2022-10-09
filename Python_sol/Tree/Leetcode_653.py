# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hmap = {}
        key = []
        
        def recur(tree):
            if not tree:
                return
            ans = k - tree.val
            
            if hmap.get(tree.val, "f") != "f":
                if hmap[tree.val] + tree.val == k:
                    key.append(ans)
            else:
                hmap[ans] = tree.val
            
            recur(tree.left)
            recur(tree.right)
            

        recur(root)
        
        if key:
            return True