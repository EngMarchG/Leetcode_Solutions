class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        ftc = 0

        for word in words:
            if any(char in brokenLetters for char in word):
                continue  
            else:
                ftc += 1  

        return ftc