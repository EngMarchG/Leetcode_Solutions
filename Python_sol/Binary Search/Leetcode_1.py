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


# Brute force method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = []

        # Time complexity O(n^n/2)m ; Space complexity O(n)
        for n, i in enumerate(nums):
            for j in range(n+1, len(nums)):
        
                if nums[n]+nums[j]==target:
                    used.append(i)
                    return [n,j]
                    
                if i in used:
                    continue