class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        smol = mid = large = float(inf)
        
        
        # Time complexity O(N) Space complexity O(1)
        for i in range(len(nums)):
            if nums[i] < smol:
                smol = nums[i]
            elif nums[i] > smol and nums[i]:
                mid = min(mid, nums[i])
            if nums[i] > mid:
                large = nums[i]
                
        # The last comparison is necessary to avoid false positives
        # in case the last case is never triggered
        # Alternatively, a try except statement and non-initialization
        # of large also works
        return smol < mid < large < float(inf)