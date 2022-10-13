class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        total = len(strs)
        counter = 0
        ans = ""
        
        # Time complexity O(N^2) Space complexity O(N)
        try:
            while True:
                for x in range(total-1):
                    if not strs[x][counter] == strs[x+1][counter]:
                        return ans
                ans += strs[0][counter]
                counter += 1
        except IndexError:
            return ans