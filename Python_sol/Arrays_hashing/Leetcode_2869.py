class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hmap = {}
        operations_done = 0
        for i in range(len(nums)-1, -1,-1):
            if nums[i] <= k and not hmap.get(nums[i], 0):
                hmap[nums[i]] = 1
                if len(hmap.keys()) == k:
                    return operations_done + 1
            operations_done += 1