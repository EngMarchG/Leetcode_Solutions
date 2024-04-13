class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.hmap = {}
        def recur(tree, depth):
            if not tree:
                return
            if not self.hmap.get(depth,0):
                self.hmap[depth] = []
            self.hmap[depth].append(tree.val)

            recur(tree.left, depth+1)
            recur(tree.right, depth+1)

        recur(root,1)
        
        ans = []
        for i, arr in enumerate(self.hmap.values()):
            if not i%2:
                ans.append(arr)
            else:
                ans.append(arr[::-1])
        return ans