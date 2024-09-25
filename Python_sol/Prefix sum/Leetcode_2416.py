class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hmap = {}

        for i in range(len(words)):
            for j in range(1, len(words[i]) + 1):
                hmap[words[i][:j]] = hmap.get(words[i][:j], 0) + 1
        
        ans = []
        for i in range(len(words)):
            temp = 0
            for j in range(1, len(words[i]) + 1):
                if hmap[words[i][:j]] > 1:
                    temp += hmap[words[i][:j]]
                else:
                    temp += len(words[i]) - j + 1
                    break
            
            ans.append(temp)

        return ans