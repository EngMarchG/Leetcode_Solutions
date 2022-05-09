class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = nums[0]
        
        # If left is less than right then the start has been found
        while left < right:
            if nums[left]<nums[right]:
                ans = min(ans,nums[left])
                break
            else:
                ans = min(ans,nums[right])
            
            # Typical binary search
            # Time complexity: O(log(n)) ; Space complexity: O(1)
            mid = (left + right)//2
            if nums[mid]<nums[right]:
                right = mid - 1
            else: 
                left = mid + 1
            ans = min(ans,nums[mid])
        return ans