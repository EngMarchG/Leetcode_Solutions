class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        
        # Time complexity O(N) Space complexity O(2N)
        for pos in range(len(nums)):
            if hmap.get(nums[pos], -1) != -1:
                hmap[nums[pos]][1] = pos
                if hmap[nums[pos]][1] - hmap[nums[pos]][0] <= k:
                    return True
                hmap[nums[pos]][0] = pos
            else:
                hmap[nums[pos]] = [pos, pos]