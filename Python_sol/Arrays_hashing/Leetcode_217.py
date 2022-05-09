class Solution:
    # Time complexity: O(len(nums)); Space complexity: O(len(nums))
    # Hashmap each value of the array and if it already exists return true
    def containsDuplicate(self, nums):
        hmap = {}
        for i in nums:
            if i in hmap:
                return -1
            else:
                hmap[i] = 1

# Time complexity: O(len(nums)); Space complexity: O(len(nums))
class Solution:
    def containsDuplicate(self, nums):
        if (len(set(nums)) == len(nums)):
            return False
        return True