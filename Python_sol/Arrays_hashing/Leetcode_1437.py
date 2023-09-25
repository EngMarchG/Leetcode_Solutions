class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = 0
        dist = k
        while pos < len(nums):
            if nums[pos] == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
            pos += 1
        return True

        