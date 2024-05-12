class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)-2
        loc_max = [[0]*size for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                loc_max[i][j] = max(max(grid[i+k][j:j+3]) for k in range(3))

        return loc_max