class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        ans = 0
        
        for i in range(len(num_str)-k+1):
            if not int(num_str[i:i+k]) % k:
                ans += 1

        return ans