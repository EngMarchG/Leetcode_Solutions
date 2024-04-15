class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recur(tree, arr):
            if not tree:
                return 0
            
            arr.append(str(tree.val))
            if not tree.left and not tree.right:
                sum = int("".join(arr))
            else:
                sum = recur(tree.left, arr) + recur(tree.right, arr)

            arr.pop()
            return sum
        
        return recur(root, [])