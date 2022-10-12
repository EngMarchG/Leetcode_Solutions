class Solution:
    def isHappy(self, n: int) -> bool:
        ans = 0
        n = str(n)
        counter = 0

        # Time complexity O(N) Space Complexity O(1)
        while counter < 15:

            for num in range(len(n)-1,-1, -1):
                ans += int(n[num])**2
            
            n = str(ans)
            ans = 0 

            
            for x in n:
                if x == "1" or x == "0":
                     ans += int(x)
                else:
                    ans = 0
                    break
            if ans == 1:
                return 1
            else:
                ans = 0
            counter += 1
            