class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # Time complexity O(2N) Space complexity O(1)
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return nums[i]
            


# Using Floyd's Hare and Turtule algorithm
# More efficient
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        # Time complexity O(N) Space complexity O(1)
        # Find the intersection point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
