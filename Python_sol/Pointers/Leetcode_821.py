class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []

        for i in range(len(s)):
            dist = 0
            while True:
                if i-dist >= 0 and s[i-dist] == c or i+dist < len(s) and s[i+dist] == c:
                    ans.append(dist)
                    break
                dist += 1
        
        return ans