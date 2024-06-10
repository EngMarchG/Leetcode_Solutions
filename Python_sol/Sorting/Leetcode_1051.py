class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if sort_heights[i] != heights[i]:
                ans += 1

        return ans