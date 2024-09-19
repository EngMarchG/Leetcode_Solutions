class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        sorted_keys = sorted(list(hmap.keys()))
        ans = 0

        for i in range(len(sorted_keys)-1):
            key1 = sorted_keys[i+1]
            key2 = sorted_keys[i] 
            if key1 - key2 == 1:
                ans = max(ans, hmap[key1]+hmap[key2])
        
        return ans

