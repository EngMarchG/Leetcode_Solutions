class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.arr = []
        hmap = {i:chr(i+97) for i in range(26)}

        def recur(tree, arr):
            if not tree:
                return
            arr.append(hmap[tree.val])
            
            if not tree.left and not tree.right:
                self.arr.append("".join(arr[::-1]))
            else:
                recur(tree.left, arr)
                recur(tree.right, arr)
            
            arr.pop()

        recur(root, [])
        self.arr.sort()

        return self.arr[0]