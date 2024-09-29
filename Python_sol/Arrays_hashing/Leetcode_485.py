class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, temp = 0, 0

        for num in nums:
            if num:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        
        return max(ans, temp)