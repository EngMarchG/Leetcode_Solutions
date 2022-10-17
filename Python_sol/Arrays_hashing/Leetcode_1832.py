class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Time complexity O(N) Space complexity O(set(N))
        if len(set(sentence)) == 26:
            return True

""" Intended Solution
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hmap = {}
        # Time complexity O(N + set(N)) Space complexity O(set(N))
        for letter in sentence:
            if not hmap.get(letter, 0):
                hmap[letter] = 1
        if len(hmap.keys()) == 26:
            return True
"""