class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hmap = {}
        max_num = -1

        for num in nums:
            if hmap.get(num,0):
                max_num = max(abs(num),max_num)
            hmap[-num] = num
        
        return max_num