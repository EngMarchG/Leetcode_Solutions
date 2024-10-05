class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for letter in s1:
            hmap[letter] = hmap.get(letter, 0) + 1
        
        temp = hmap.copy()
        i = 0
        while i <= len(s2) - len(s1) + 1:
            min_char = 0
            for j in range(i, len(s2)):
                if temp.get(s2[j], 0):
                    temp[s2[j]] -= 1
                    min_char += 1
                    if min_char == len(s1) and sum(temp.values()) == 0:
                        return True
                else:
                    if not hmap.get(letter,0):
                        i = j+1
                    break
            temp = hmap.copy()
            i += 1