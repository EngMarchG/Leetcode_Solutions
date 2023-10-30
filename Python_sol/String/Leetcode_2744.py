class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        max_pairs = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    max_pairs += 1
        return max_pairs
    
# Slower solution since it checks the whole string
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        max_pairs = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1]:
                    max_pairs += 1
        return max_pairs