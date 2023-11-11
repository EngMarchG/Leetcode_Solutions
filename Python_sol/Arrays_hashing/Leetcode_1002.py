class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        ans = []
        for letter in words[0]:
            if all(letter in word for word in words):
                ans.append(letter)
                words = [word.replace(letter, '', 1) for word in words]
        return ans
    
# More efficient solution
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        ans = []
        for letter in set(words[0]):
            if all(letter in word for word in words):
                ans.extend([letter] * min(word.count(letter) for word in words))
        return ans