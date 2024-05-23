class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hmap = {}

        for word in words:
            for letter in word:
                hmap[letter] = hmap.get(letter,0) + 1
        
        for key in hmap.keys():
            if hmap[key]%len(words) != 0:
                return False
        
        return True