class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hmap = {}

        for word in dictionary:
            if not hmap.get(word[0],0):
                hmap[word[0]] = {}
            hmap[word[0]][word] = hmap[word[0]].get(word, 0) + 1
        
        sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            if hmap.get(word[0], 0):
                temp = 1
                while temp < len(word) and not hmap[word[0]].get(word[:temp],0):
                    temp += 1
                if hmap[word[0]].get(word[:temp],0):
                    sentence[i] = word[:temp]
        return " ".join(sentence)