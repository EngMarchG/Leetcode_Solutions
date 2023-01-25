class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        content = 0
        steps = 0
        # Time complexity O(g + n + min(g,n)) Space complexity O(1)
        for i in range(len(g)):
            try:
                if g[i]<=s[i+steps]:
                    content +=1
                else:
                    while i+steps<len(s):
                        if g[i]<=s[i+steps]:
                            content +=1
                            break
                        steps += 1
            except IndexError:
                break
        return content