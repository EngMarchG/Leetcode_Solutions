class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hmap = {}
        ans = []
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for i in range(1,len(nums)+1):
            if not hmap.get(i):
                ans.append(i)
        
        return ans