class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        temp = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        
        return max(ans,temp)