class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        
        # Time complexity O(2N) Space complexity O(1)
        for i in s:
            if i =='1':
                ones += 1
        zeros = ones
        for i in range(len(s)-1,-1,-1):
            if s[i] =='1':
                ones -= 1
            else:
                ones += 1
            zeros = min(zeros,ones)
        return zeros