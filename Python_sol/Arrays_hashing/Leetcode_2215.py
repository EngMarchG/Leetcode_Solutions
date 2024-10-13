class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hmap = {}
        nums2 = set(nums2)
        ans = [[],[]]
        for num in nums1:
            hmap[num] = hmap.get(num, 0) + 1
        
        for num in nums2:
            if not hmap.get(num,0):
                ans[1].append(num)
            elif hmap.get(num,0):
                hmap[num] = 0

        for num in hmap.keys():
            if hmap[num]:
                ans[0].append(num)

        return ans
