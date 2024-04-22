class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")
        
        def recur(tree):
            if not tree:
                return 0
            
            left_sum = max(0, recur(tree.left))
            right_sum = max(0, recur(tree.right))

            self.max_sum = max(self.max_sum, left_sum + tree.val + right_sum)

            return max(left_sum, right_sum) + tree.val
        
        recur(root)
        
        return self.max_sum