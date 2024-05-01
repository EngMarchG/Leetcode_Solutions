class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        cur = ans = 0

        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            ans += count[cur]
            for i in range(10):
                ans += count[cur ^ (1 << i)]
            count[cur] += 1

        return ans