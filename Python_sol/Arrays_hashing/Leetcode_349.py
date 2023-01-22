class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        arr = []

        # Space complexity O(2set(N)) Time complexity O(N+M)
        for num in nums1:
            if not hmap.get(num,0):
                hmap[num] = 1
        for num in nums2:
            if hmap.get(num,0):
                arr.append(num)
                hmap[num] = 0
        return arr