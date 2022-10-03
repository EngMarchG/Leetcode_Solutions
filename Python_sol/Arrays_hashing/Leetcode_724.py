# Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Using sum() runs in C, hence faster performance
        total = sum(nums)
        cur_sum = 0
        
        # Time complexity O(2N) Space complexity O(1)
        for x, num in enumerate(nums):
            if cur_sum == total - (cur_sum + num):
                return x
            cur_sum += num

        return -1