class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp = 0
        ans = 0
        hmap = {"L": -1, "R": 1}
        for letter in s:
            if temp:
                temp += hmap[letter]
                if not temp:
                    ans += 1
            else:
                temp += hmap[letter]
        
        return ans