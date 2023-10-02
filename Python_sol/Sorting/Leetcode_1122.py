class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hmap = {}
        for num in arr1:
            hmap[num] = hmap.get(num, 0) + 1
        
        ans = []
        for num in arr2:
            ans.extend(hmap[num]*[num])
            hmap.pop(num)

        for num in sorted(hmap.keys()):
            ans.extend(hmap[num]*[num])
            hmap.pop(num)

        return ans