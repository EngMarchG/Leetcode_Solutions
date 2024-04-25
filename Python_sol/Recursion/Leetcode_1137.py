class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}


        def recur(num):
            if num in memo:
                return memo[num]
            
            memo[num] = recur(num-3) + recur(num-2) + recur(num-1)
            
            return recur(num-3) + recur(num-2) + recur(num-1)

        return recur(n)