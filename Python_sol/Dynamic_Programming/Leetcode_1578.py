class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        
        # Time complexity O(N) Space complexity O(1)
        while r < len(colors):
            if colors[l] == colors[r]:
                
                if neededTime[l] < neededTime[r]:
                    ans += neededTime[l]
                    l = r
                else:
                    ans += neededTime[r]
                    
            else:
                l = r
            r += 1

        return ans