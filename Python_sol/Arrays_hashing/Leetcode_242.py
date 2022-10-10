class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Time Complexity O(5N)=O(N) space complexity O(2N)=O(N)
        if not len(s)==len(t):
            return 0
        arr1=[i for i in s]
        arr2=[j for j in t]
        arr1.sort()
        arr2.sort()
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return 0
        return 1

"""Better solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity O(4N) Space complexity O(2N) 
        if ''.join(sorted(s))==''.join(sorted(t)):
            return 1
"""

"""Best Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmap1 = {}
        hmap2 = {}
        counter = 0

        # Time Complexity O(N + set(N)) Space complexity O(2*set(N))
        while counter < len(s):
            if hmap1.get(s[counter], 0):
                hmap1[s[counter]] += 1
            else:
                hmap1[s[counter]] = 1
                
            if hmap2.get(t[counter], 0):
                hmap2[t[counter]] += 1
            else:
                hmap2[t[counter]] = 1
            
            counter += 1
        
        for lett in s:
            try:
                if hmap1[lett] != hmap2[lett]:
                    return False
            except KeyError:
                return False

        return True
"""