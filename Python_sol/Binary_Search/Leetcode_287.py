class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # Time complexity O(2N) Space complexity O(1)
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return nums[i]