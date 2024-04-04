class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for x, word in enumerate(strs):
            strs[x] = str(sorted(word))
            if hmap.get(strs[x],0):
                hmap[strs[x]].append(word)
            else: 
                hmap[strs[x]] = [word]
        return hmap.values()