class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap = {}
        words = s.split(" ")
        if len(set(pattern)) != len(set(words)) or len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if hmap.get(pattern[i], 0):
                if hmap[pattern[i]] == words[i]:
                    continue
                else:
                    return False
            hmap[pattern[i]] = words[i]
        
        return True