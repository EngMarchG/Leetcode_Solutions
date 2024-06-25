class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = pairs = 0

        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                pairs += 1
                i += 1
            i += 1

        return [pairs, len(nums)-pairs*2]
    

        """
        # Using hashmap
        class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hmap = {}
        pair = 0

        for num in nums:
            if hmap.get(num, 0):
                hmap[num] -= 1
                pair += 1
            else:
                hmap[num] = 1
        
        return [pair, len(nums)-pair*2]
        """