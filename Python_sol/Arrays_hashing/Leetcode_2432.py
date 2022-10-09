class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = logs[0][0]
        maxi = logs[0][1]
        
        # Time complexity O(N) Space complexity O(1)
        for i in range(1, len(logs)):
            
            if logs[i][1] - logs[i-1][1] > maxi:
                maxi = logs[i][1] - logs[i-1][1]
                ans = logs[i][0]
            
            elif logs[i][1] - logs[i-1][1] == maxi and logs[i][0] < ans:
                maxi = logs[i][1] - logs[i-1][1]
                ans = logs[i][0]
                
        return ans