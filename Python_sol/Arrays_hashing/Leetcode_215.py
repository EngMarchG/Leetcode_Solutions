class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickselect(self, nums, low, high, k):
        pivot = nums[low]
        l, r = low + 1, high
        while l <= r:
            if nums[l] > pivot and nums[r] < pivot:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] <= pivot:
                l += 1
            if nums[r] >= pivot:
                r -= 1
        nums[low], nums[r] = nums[r], nums[low]

        if r == k:
            return nums[r]
        elif r < k:
            return self.quickselect(nums, r + 1, high, k)
        else:
            return self.quickselect(nums, low, r - 1, k)