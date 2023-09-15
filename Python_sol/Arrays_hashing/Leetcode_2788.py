class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            temp = word.split(separator)
            temp = [x for x in temp if len(x)>0]
            ans.extend(temp)
        return ans