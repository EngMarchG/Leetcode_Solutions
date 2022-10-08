class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        ans = 10**5
        
        # Time complexity O(N^2) space complexity O(N)
        # Should seek a faster algorithm since the updated cases
        # Give the 2 solutions a pass sometimes
        for i in range(l-2):
            left = i + 1
            right = l - 1
            total = nums[i] + nums[left] + nums[right]
            while left < right:
                
                cake = target - total
                
                if abs(cake) < abs(target-ans):
                    ans = total
                
                if cake < 0:
                    total -= nums[right]
                    right -= 1
                    total += nums[right]
                else:
                    total -= nums[left]
                    left += 1
                    total += nums[left]
                    if not cake:
                        return target
                

        return ans

""" Old solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        nums.sort()
        ans = float(inf)
        
        if l == 3:
            return sum(nums)
        
        for i in range(l-2):
            left = i + 1
            right = l-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total <= target:
                    left += 1
                    if total-target == 0:
                        return total
                if abs(target-total)<=abs(target-ans):
                    ans = total
        
        return ans"""