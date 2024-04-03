# Best Solution:
# Time complexity O(n+set(n)) Space complexity O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return
        
        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
            hmap[t[i]] = hmap.get(t[i], 0) - 1
        
        for value in hmap.values():
            if value:
                return
        return True

"""Better solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity O(slog(s)+tlog(t)) Space complexity O(1) 
        if sorted(s)==sorted(t):
            return 1
"""