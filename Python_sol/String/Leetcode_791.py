class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = {}

        # Time complexity O(2N+M+set(M)) Space complexity O(2M)
        for i in range(len(s)):
            if hmap.get(s[i],0):
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1

        arr = []
        for i in range(len(order)):
            if hmap.get(order[i],0):
                arr.append(order[i]*hmap[order[i]])
                hmap[order[i]] = 0
                
                
        return ("".join(arr) + "".join([hmap[x]*x for x in hmap.keys() if hmap[x]>0]))
