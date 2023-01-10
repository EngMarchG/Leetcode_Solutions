class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Time complexity O(3N) Space Complexity O(1)
        if ord(word[0]) > 95:
            if word[1:] != word[1:].lower():
                return False
        else:
            if word[1:] == word[1:].lower():
                return True
            if word[1:] != word[1:].upper():
                return False
        return True
