class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if len(word) >= len(pref):
                ans += 1
                for pos, letter in enumerate(pref):
                    if word[pos] != letter:
                        ans -= 1
                        break
        return ans