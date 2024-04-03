class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = 0
        arr_tot = 0
        for i in range(len(nums)):
            tot += i+1
            arr_tot += nums[i]

        return tot - arr_tot