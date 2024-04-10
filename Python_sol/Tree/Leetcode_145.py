class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stack = []
        def recur(tree):
            if not tree:
                return 
            self.stack.append(tree.val)
            left = recur(tree.left)
            right = recur(tree.right)

            return 

        recur(root.left)
        self.stack.append(root.val)
        ans = self.stack
        self.stack = 0