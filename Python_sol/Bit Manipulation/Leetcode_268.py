class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)
        
        # Time Complexity: O(n) ; Space Complexity: O(1)
        for i in range(len(nums)):
            total += i-nums[i]
        return total