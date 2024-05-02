class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, letter in enumerate(word):
            if letter == ch:
                return word[i::-1] + word[i+1:]
        
        return word