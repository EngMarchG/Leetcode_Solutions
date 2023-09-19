class Solution:
    def maxPower(self, s: str) -> int:
        ans = temp = 1
        for x in range(len(s)-1):
            if s[x] == s[x+1]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        return max(ans,temp)