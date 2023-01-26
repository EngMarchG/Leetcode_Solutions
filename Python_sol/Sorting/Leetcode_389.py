class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap = {}
        
        # Time complexity O(2N) Space complexity O(1)
        for i in s:
            if hmap.get(i, 0):
                hmap[i] += 1
            else:
                hmap[i] = 1
        
        for j in t:
            if hmap.get(j, 0):
                hmap[j] -= 1
                if hmap[j]<0:
                    return j
            else:
                return j