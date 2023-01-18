class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        max_ending_here = 0
        min_ending_here = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        
        # Time complexity O(N) Space complexity O(1)
        for num in nums:
            total_sum += num
            max_ending_here = max(max_ending_here + num, num)
            max_sum = max(max_sum, max_ending_here)
            min_ending_here = min(min_ending_here + num, num)
            min_sum = min(min_sum, min_ending_here)
        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum