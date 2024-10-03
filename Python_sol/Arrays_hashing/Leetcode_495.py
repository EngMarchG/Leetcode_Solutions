class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries) - 1):
            time_diff = timeSeries[i + 1] - timeSeries[i]
            ans += min(time_diff, duration)
            
        return ans + duration 