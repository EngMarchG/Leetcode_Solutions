class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        hmap = {}

        def addNumber(arr, p):
            if hmap.get(arr[p][0], -1) == -1:
                    hmap[arr[p][0]] = arr[p][1]
            else:
                hmap[arr[p][0]] += arr[p][1]
            return p+1

        while p2 < len(nums2) and p1 < len(nums1):
            if nums1[p1] < nums2[p2]:
                p1 = addNumber(nums1, p1)
            else:
                p2 = addNumber(nums2, p2)
        
        while p1 < len(nums1):
            p1 = addNumber(nums1, p1)

        while p2 < len(nums2):
            p2 = addNumber(nums2, p2)

        return [[key, value] for key, value in hmap.items()]