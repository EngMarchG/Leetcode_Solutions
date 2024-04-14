class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.hmap = {}

        def recur(tree, row, col):
            if not tree:
                return

            if not self.hmap.get(col, 0):
                self.hmap[col] = {}
            if not self.hmap[col].get(row,0):
                self.hmap[col][row] = []

            self.hmap[col][row].append(tree.val)

            recur(tree.left, row+1, col-1)
            recur(tree.right, row+1,col+1)

        recur(root, 0, 0)

        ans = []
        for col in sorted(self.hmap.keys()):
            temp = []
            for row in sorted(self.hmap[col]):
                temp.extend(sorted(self.hmap[col][row]))
            ans.append(temp)
        return ans 