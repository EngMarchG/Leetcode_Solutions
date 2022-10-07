class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        
        for x in range(3, n+1):
            if not memo.get(x, 0):
                memo[x] = memo[x-1] + memo[x-2]
        
        return memo[n]