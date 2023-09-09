class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # Use 3 variables to store the first, second and third largest number
        # Space complexity: O(1), Time complexity: O(n)
        first = second = third = float('-inf')

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num

        return third if third != float('-inf') else max(nums)
