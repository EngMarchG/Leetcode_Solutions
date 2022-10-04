# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = ans = n
        
        # Time complexity O(log(N)) Space complexity O(1)
        while l <= r:
            mid = (l+r)//2

            if isBadVersion(mid):
                ans = mid
                r = mid - 1

            else:
                l = mid + 1
            
        return ans
                