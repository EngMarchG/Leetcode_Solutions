# Find the difference between the current number and target
# Save the difference and its position in the hashmap
# If a term in the array is defined in the hashmap then it is the target
# Time Complexity: O(nums) ; Space Complexity: O(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            if hmap.get(nums[i], -1) != -1:
                return [hmap[nums[i]], i]
            else:
                hmap[target-nums[i]] = i




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        left = 0
        right = l-1
        hmap = dict()
        
        # Hashmap for positions
        for i in range(l):
            if hmap.get(nums[i],-1)!=-1:
                hmap[nums[i]].append(i)
            else:
                hmap[nums[i]] = [i]
        nums.sort()
        
        
        # Binary search and retrieve the positions from the hasmap list
        # Time complexity O(2n+log(n)) ; Space complexity O(2n)
        while left < right:
            total = nums[left] + nums[right]
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            elif nums[left]==nums[right] and total == target:
                return [hmap[nums[left]][0], hmap[nums[left]][1]]
            else:
                return [hmap[nums[left]][0], hmap[nums[right]][0]]