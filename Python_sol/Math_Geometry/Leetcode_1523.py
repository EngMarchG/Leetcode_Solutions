class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        x = 0
        if low % 2:
            ans += 1
            x += 1
        if high % 2:
            ans += 1
            x += 1
        return ans + (high - low - x)//2