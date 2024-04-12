class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = [float("inf")]*k

        def recur(tree):
            if not tree:
                return
                
            if tree.val <= self.arr[0]:
                self.arr[0] = tree.val
                pointer = 0
                while (pointer < len(self.arr)-1) and (self.arr[pointer] <= self.arr[pointer+1]):
                    self.arr[pointer],self.arr[pointer+1] = self.arr[pointer+1],self.arr[pointer]
                    pointer += 1
            
            recur(tree.left)
            recur(tree.right)
        
        recur(root)
        return self.arr[0]
                    