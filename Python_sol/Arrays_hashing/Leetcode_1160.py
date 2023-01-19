class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hmap = {}
        for char in chars:
            if hmap.get(char,0):
                hmap[char] += 1
            else:
                hmap[char] = 1
        
        ans = 0
        for word in words:
            temp = hmap.copy()
            counts = 0
            for lett in word:
                if temp.get(lett,0):
                    counts += 1
                    temp[lett] -= 1
                else:
                    break
            if counts == len(word):
                ans +=counts
        return ans

        """To avoid using so much space temp can be done only when counts is triggered
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hmap = {}
        for char in chars:
            if hmap.get(char,0):
                hmap[char] += 1
            else:
                hmap[char] = 1
        
        ans = 0
        counts = 0
        temp = hmap.copy()
        # Time complexity O(N + N^2) Space complexity O(2N)
        for word in words:
            if counts:
                temp = hmap.copy()
            counts = 0
            for lett in word:
                if temp.get(lett,0):
                    counts += 1
                    temp[lett] -= 1
                else:
                    break
            if counts == len(word):
                ans +=counts
        return ans
        """