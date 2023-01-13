class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi = -1
        mini = float(inf)
        diff = -1
        
        for i in nums:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
            if i != mini:
                diff = max(diff, i-mini)
        return diff

 """Similar solution with slight changes
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        diff = -1
        
        # Space complexity O(1) Time complexity O(N)
        for i in range(1,len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
            elif nums[i] <= mini:
                mini = nums[i]
                continue
            diff = max(diff, nums[i]-mini)
        return diff


"""