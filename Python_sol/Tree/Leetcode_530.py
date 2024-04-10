class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = -1
        self.min_diff = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev >= 0:
                    self.min_diff = min(self.min_diff, node.val - self.prev)
                self.prev = node.val
                inorder(node.right)

        inorder(root)
        return self.min_diff