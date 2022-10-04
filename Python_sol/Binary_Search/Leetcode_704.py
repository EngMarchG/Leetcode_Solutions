class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        # Time complexity O(log(N)) Space complexity O(1)
        while l < r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid
        return -1