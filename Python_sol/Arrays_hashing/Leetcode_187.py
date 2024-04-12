class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap = {}

        for seq in range(len(s)-9):
            hmap[s[seq:seq+10]] = hmap.get(s[seq:seq+10], 0) + 1

        return [ans for ans in hmap.keys() if hmap[ans]>1]