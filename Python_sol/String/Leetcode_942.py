class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        left, right = 0, len(s) 

        for i in range(len(s)):
            if s[i] == "I":
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans