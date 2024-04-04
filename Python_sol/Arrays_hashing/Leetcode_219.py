class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}

        for i, num in enumerate(nums):
            if hmap.get(num,-1) != -1 and i-hmap[num] <= k:
                return True
            hmap[num] = i