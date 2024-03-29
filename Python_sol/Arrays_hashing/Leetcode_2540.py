class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0

        # Time complexity O(min(M,N)) and Space complexity O(1)
        while first<len(nums1) and second<len(nums2):
            if nums1[first]==nums2[second]:
                return nums1[first]
            elif nums1[first]>nums2[second]:
                second += 1
            else:
                first += 1
        
        return -1