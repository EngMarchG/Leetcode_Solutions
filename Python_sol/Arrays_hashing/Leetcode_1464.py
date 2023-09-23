class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = p2 = 1

        for num in nums:
            if num >= p1:
                p2 = p1
                p1 = num
            elif num >= p2:
                p2 = num
        return (p1-1)*(p2-1)


## Another solution
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         return (nums[-1]-1)*(nums[-2]-1)