class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = 0
        while i < len(s):
            if len(s) - i > 2 and s[i+2] == "#":
                ans += chr(96 + int(s[i:i+2]))
                i += 3
            else:
                ans += chr(96 + int(s[i]))
                i += 1
        return "".join(ans)
