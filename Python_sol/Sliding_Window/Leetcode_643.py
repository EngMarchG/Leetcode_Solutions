class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sliding_avg = sum(nums[:k])
        max_avg = sliding_avg

        for i in range(k, len(nums)):
            sliding_avg = sliding_avg - nums[i-k] + nums[i]
            max_avg = max(max_avg, sliding_avg)

        return max_avg/k