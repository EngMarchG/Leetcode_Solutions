"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        
        # Using recursion, loop through the children
        # and append any non null value 
        def recur(tree):
            if not tree:
                return 
            arr.append(tree.val)
            for node in tree.children:
                recur(node)
            return arr
        
        return recur(root)