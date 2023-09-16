class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        hmap = {"a":1, "e":1, "u":1, "i":1, "o":1}
        ans = 0
        
        for x in range(left, right+1):
            if hmap.get(words[x][0], 0) and hmap.get(words[x][-1], 0):
                ans +=1
        return ans