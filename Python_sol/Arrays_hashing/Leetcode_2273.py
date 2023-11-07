class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        for i in range(len(words)-1):
            if not isinstance(words[i], int):
                temp = sorted(words[i])
            else:
                continue
            for j in range(i+1, len(words)):
                if words[j] == -1:
                     continue
                if sorted(words[j]) == temp:
                    words[j] = -1
                else:
                    break
                
        return [x for x in words if x != -1]