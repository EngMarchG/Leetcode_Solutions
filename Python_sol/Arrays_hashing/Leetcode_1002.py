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
    

# Solution without relying on python specific functions
class Solution:
    # More efficient solution
    def commonChars(self, words: List[str]) -> List[str]:
        hmap = {}

        for i, word in enumerate(words):
            temp = {}
            for letter in word:
                temp[letter] = temp.get(letter, 0) + 1
            
            if not hmap:
                if i != 0:
                    return []
                hmap = temp
            else:
                temp2 = {}
                for key in temp.keys():
                    if hmap.get(key, 0):
                        temp2[key] = min(hmap[key], temp[key])
                
                hmap = temp2
        
        return [key for key in hmap.keys() for val in range(hmap[key])] 