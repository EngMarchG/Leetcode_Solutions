class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for x in range(len(s)):
            if s == goal:
                return True
            s = s[-1] + s[:-1]1