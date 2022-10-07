class Solution:
    def climbStairs(self, n: int) -> int:
        hmap = {1:1, 2:2}
        
        for x in range(3, n+1):
            if not hmap.get(x, 0):
                hmap[x] = hmap[x-2] + hmap[x-1]
        return hmap[n]


"""Less elegent solution
class Solution:  
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        
        last = 2
        now = 3
        for i in range(4, n+1):
            temp = last + now
            last = now
            now = temp
        return temp
"""

"""Recursion
class Solution:  
    def climbStairs(self, n: int) -> int:
        
        def recur(num, hmap):
            if num == 1:
                return 1
            if num == 2:
                return 2
            if num not in hmap:
                hmap[num] = recur(num-1, hmap) + recur(num-2, hmap)
            
            return hmap[num]
        
        return recur(n, dict())
        
"""