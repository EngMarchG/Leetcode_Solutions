class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_ele = max(nums)
        ans = []

        for i in range(len(nums)):
            temp = i+1
            if temp == len(nums):
                temp = 0
            if nums[i] == max_ele:
                ans.append(-1)
                continue

            while temp != i:
                if nums[temp] > nums[i]:
                    ans.append(nums[temp])
                    break
                
                temp += 1
                if temp == len(nums):
                    temp = 0

        return ans